import maya.cmds as cmds

def create_render_cam():
        
    cam_list = cmds.ls(type="camera")
    cam_transform_list = cmds.listRelatives(cam_list,parent=True)
    if len(cam_list) < 5:
        render_cam = cmds.camera()
        cmds.setAttr(render_cam[0] + ".translateY", 8)
        cmds.setAttr(render_cam[0] + ".translateZ", 24)
    else:
        cmds.delete(cam_list[1:2])
        cmds.delete(cam_transform_list[1:2])    
        cmds.warning("only one RENDER CAMERA is allowed. Please delete your Render Camera and create the new one")


def set_cam_trans(axis):
    cam_list = cmds.ls(type="camera")
    cam_transform_list = cmds.listRelatives(cam_list,parent=True)
    transZ = cmds.floatField("translate" + axis, query = True, value = True)
    cmds.setAttr(cam_transform_list[0] + ".translate" + axis, transZ) 
    
def Y_axis():
    set_cam_trans("Y")

def Z_axis():
    set_cam_trans("Z")