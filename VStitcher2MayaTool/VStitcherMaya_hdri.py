#light
import maya.cmds as cmds
import mtoa.utils as utils
def create_hdri():

    aiLightList = []
    light_list = cmds.ls(type = "shape")
    for light in light_list:
        if light.startswith("ai"):
            light_string = str(light)
            aiLightList.append(string)
            


    if len(aiLightList) < 1:
        hdri_path = cmds.fileDialog(m = 0, dm="*.png;*.jpg;*.tiff;*.exr;*.hdr;")
        Dome_Light = utils.createLocator("aiSkyDomeLight", asLight = True)
        hdri_UV_node = cmds.shadingNode('place2dTexture', n= "hdri_UV", au =True)
        hdri_map = cmds.shadingNode( 'file',n = "HDRI", at =True )

        cmds.connectAttr(str(hdri_UV_node) + ".outUV", str(hdri_map) + ".uvCoord", f = True)
        cmds.connectAttr(str(hdri_UV_node) + ".offset", str(hdri_map) + ".offset", f= True)
        cmds.connectAttr(str(hdri_UV_node) + ".repeatUV", str(hdri_map) + ".repeatUV", f = True)
        cmds.connectAttr(str(hdri_UV_node) + ".rotateUV", str(hdri_map) + ".rotateUV", f = True)

        cmds.connectAttr(str(hdri_map) + ".outAlpha", Dome_Light[0] + ".intensity")

        cmds.setAttr(str(hdri_map) + ".fileTextureName", hdri_path, type = "string") 
    else:
        cmds.warning("You can ONLY create one Domelight. Click DELETE button if you want to recreate")  
       
        cmds.delete(aiLightList[1:])

#delete HDRI
def delete_hdri():

    aiLightList = []
    light_list = cmds.ls(type = "shape")

    for light in light_list:
        if light.startswith("ai"):

            light_string = str(light)
            aiLightList.append(light_string)
            
            aiLight_transform_list = cmds.listRelatives(light_string,parent=True)

            cmds.delete(light_string)
            cmds.delete(aiLight_transform_list)

def delete_hdri_dialog():
    confirm_function = cmds.confirmDialog(title="Are you sure?",
                                    message ="Are you sure you want to delete the hdri?",
                                    button = ["Yes", "No"],
                                    cancelButton = "Yes")
    if confirm_function == "Yes":
        delete_hdri()

