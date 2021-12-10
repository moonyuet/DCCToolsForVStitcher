import maya.cmds as cmds

def set_Import():

    locator = cmds.spaceLocator(n = "Transform_MASTER_Only_1")
    locator_list = cmds.ls(type = "locator")
    locator_transform_list = cmds.listRelatives(locator_list,parent=True)
    if not len(locator_list) > 1:
        geo_path = cmds.fileDialog(m = 0, dm="*.obj;*.fbx;")
        cmds.file(geo_path, i = True, mergeNamespacesOnClash= False)
        objs = cmds.ls(type = "mesh")
        obj_grp = cmds.group(objs, n="garment_MASTER")
        cmds.parent(obj_grp, locator)
        cmds.setAttr(locator_transform_list[0] + ".scaleX", 0.1)
        cmds.setAttr(locator_transform_list[0] + ".scaleY", 0.1)
        cmds.setAttr(locator_transform_list[0] + ".scaleZ", 0.1)
    else:
        
        cmds.delete(locator_list[1:])
        cmds.delete(locator_transform_list[1:])
        cmds.warning("You can only import ONE object")

def shader_creation(version = 0):
    #select a mesh 
    current_obj = cmds.ls(selection = True)
    current_obj_shape = cmds.listRelatives(current_obj,parent=True)
    if not current_obj:
        cmds.warning("You must select ONE mesh to assign material")
        return
        
    #open file dialog 
    file_path = cmds.fileDialog(m = 0, dm="*.png;*.jpg;*.tiff")

    file_split = file_path.split("_")
    extension_split = file_split[1].split(".")

    pbr_path = []
    pbr_path.append(file_path)
    cmds.textField('name', query = True, text= True)


    pbr_list = ["ROUGH","NRM", "MTL"]

    for p in pbr_list:
        name_split = file_split[1].replace(extension_split[0], p)
        map_path = file_path.replace(file_split[1], name_split)
        pbr_path.append(map_path)
        

    ###create pbr shader
    new_aiShader = cmds.createNode('aiStandardSurface')
    shader_grp = cmds.sets(name=new_aiShader + "DISP",
                             empty=True,
                             renderable=True,
                             noSurfaceShader=True)
    
    version += 1
    new_version = 'v{:03}'.format(version)
    
    cmds.connectAttr(new_aiShader + ".outColor", shader_grp + ".surfaceShader")

    diffuse_map = cmds.shadingNode( 'file',n = "BaseColor_Map" + "." + new_version, at =True )
    cmds.connectAttr(diffuse_map + ".outColor", new_aiShader + ".baseColor")

    roughness_map = cmds.shadingNode( 'file',n = "Roughness_Map"+ "." + new_version, at =True )
    cmds.connectAttr(roughness_map + ".outAlpha", new_aiShader + ".specularRoughness")
    metallic_map = cmds.shadingNode( 'file',n = "Metallic_Map" + "." + new_version, at =True )
    cmds.connectAttr(metallic_map + ".outAlpha", new_aiShader + ".metalness")

    normal_map = cmds.shadingNode( 'file',n = "Normal_Map" + "." + new_version, at =True )
    #convert normal_map to bump_map
    bump_2d_node = cmds.shadingNode('bump2d', n= "normal_bump_parameter" + "." + new_version, au =True)
    cmds.setAttr(bump_2d_node + ".bumpInterp", 1)
    cmds.connectAttr(normal_map + ".outAlpha", bump_2d_node + ".bumpValue")
    cmds.connectAttr(bump_2d_node + ".outNormal", new_aiShader + ".normalCamera")

    textureCoord = cmds.shadingNode('place2dTexture', n= "Mapping Transform" + "." + new_version, au = True)

    file_list = cmds.ls(type= ["file"])
    Coord_list = cmds.ls(type= ["place2dTexture"])
    count = len(Coord_list) 

    for f in file_list:
        for j in range (0, count):     
            cmds.connectAttr(Coord_list[j] + ".outUV", f + ".uvCoord", f = True)
            cmds.connectAttr(Coord_list[j] + ".offset", f + ".offset", f= True)
            cmds.connectAttr(Coord_list[j] + ".repeatUV", f + ".repeatUV", f = True)
            cmds.connectAttr(Coord_list[j] + ".rotateUV", f + ".rotateUV", f = True)
            if not cmds.isConnected(Coord_list[j] + ".outUV", f + ".uvCoord"):
                cmds.delete(Coord_list[j])

    cmds.setAttr(str(diffuse_map) + ".fileTextureName", pbr_path[0], type = "string")
    cmds.setAttr(str(roughness_map) + ".fileTextureName", pbr_path[1], type = "string")
    cmds.setAttr(str(normal_map) + ".fileTextureName", pbr_path[2], type = "string")
    cmds.setAttr(str(metallic_map) + ".fileTextureName", pbr_path[3], type = "string")   
    
    
    cmds.sets(current_obj_shape, forceElement = str(shader_grp))
    return file_path
