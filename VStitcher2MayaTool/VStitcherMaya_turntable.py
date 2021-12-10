import maya.cmds as cmds
def create_turntable_animation():

    locator_list = cmds.ls(type = "locator")
    locator_transform_list = cmds.listRelatives(locator_list,parent=True)
    if locator_list:
        cmds.setKeyframe(locator_transform_list[0], v= 0, attribute = "rotateY", t = ['0sec'])
        cmds.setKeyframe(locator_transform_list[0], v= 360, attribute = "rotateY", t = ['5sec'])
        cmds.keyTangent(locator_transform_list[0], itt= "linear", ott = "linear", time=('0sec', '5sec'))
    else:
        cmds.warning("you must select ONE locator")


def delete_turntable_animation():
    locator_list = cmds.ls(type = "locator")
    locator_transform_list = cmds.listRelatives(locator_list,parent=True)
    cmds.cutKey(locator_transform_list[0], s=True)

def delete_turntable_dialog():
    confirm_function = cmds.confirmDialog(title="Are you sure?",
                                    message ="Are you sure you want to delete the turntable?",
                                    button = ["Yes", "No"],
                                    cancelButton = "Yes")
    if confirm_function == "Yes":
        delete_turntable_animation()

