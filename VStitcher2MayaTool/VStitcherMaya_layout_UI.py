import sys
from importlib import reload
import maya.cmds as cmds
import mtoa.utils as utils
import webbrowser

path = r"C:\Users\Kayla\Desktop\VStitcher2MayaTool" #YOUR PYTHON FILE PATH
sys.path.append(path)
IMG_PATH = path + "/img/"


def UI():
    window = cmds.window(title= "VStitcherToMaya Tool", widthHeight = (600, 600))

    cmds.columnLayout(adjustableColumn=True, w = 600)
    cmds.rowColumnLayout(numberOfColumns = 2,columnWidth = [(1, 300), (2, 300)], columnSpacing = [(2,10)])
    cmds.button(label = "Import Mesh",
                command = ("import VStitcherMaya_mesh;reload(VStitcherMaya_mesh);VStitcherMaya_mesh.set_Import()"))
    cmds.button(label= "Help",
    command = ("import VStitcherMaya_documentation;reload(VStitcherMaya_documentation);VStitcherMaya_documentation.myWebsite()"))
    cmds.columnLayout(adjustableColumn = True, w=600)

    cmds.separator()

    cmds.rowColumnLayout(numberOfColumns = 3,columnWidth = [(1, 100), (2, 300), (3,200)])
    cmds.text("Shader Name:",  align ='left' )
    cmds.textField('name', text = "AiShader")
    
    cmds.button(label = "Create Shader",
                command = ("import VStitcherMaya_mesh;reload(VStitcherMaya_mesh);VStitcherMaya_mesh.shader_creation()"))
    cmds.columnLayout(adjustableColumn = True, w = 600)

    cmds.separator()

    cmds.button(label = 'Create Camera',width = 150,
                command = ("import VStitcherMaya_camera; reload(VStitcherMaya_camera);VStitcherMaya_camera.create_render_cam()"))

    cmds.separator()

    cmds.rowColumnLayout(numberOfColumns = 4,columnWidth = [(1, 150), (2, 150), (3, 150), (4, 150)])
    cmds.text("Camera Up/Down")
    
    tranY = cmds.floatField("translateY", height = 30,value = 8, 
        cc = ("import VStitcherMaya_camera; reload(VStitcherMaya_camera);VStitcherMaya_camera.Y_axis()"))
    cmds.text("Camera Zoom In/Out")

    tranZ = cmds.floatField("translateZ", height = 30, value = 24, 
        cc = ("import VStitcherMaya_camera; reload(VStitcherMaya_camera);VStitcherMaya_camera.Z_axis()"))
    cmds.columnLayout(adjustableColumn = True, w = 600)

    cmds.separator()

    cmds.rowColumnLayout(numberOfColumns = 2,columnWidth = [(1, 300), (2, 300)], columnSpacing = [(2,10)])
    cmds.button(label= "Create HDRI",
                command = ("import VStitcherMaya_hdri; reload(VStitcherMaya_hdri); VStitcherMaya_hdri.create_hdri()"))
    cmds.button(label= "Delete HDRI",
                command = ("import VStitcherMaya_hdri; reload(VStitcherMaya_hdri); VStitcherMaya_hdri.delete_hdri_dialog()"))
    cmds.columnLayout(adjustableColumn = True, w = 600)

    cmds.separator()

    cmds.rowColumnLayout(numberOfColumns = 2,columnWidth = [(1, 300), (2, 300)], columnSpacing = [(2,10)])
    cmds.button(label= "Create Turntable",
                command = ("import VStitcherMaya_turntable; reload(VStitcherMaya_turntable); VStitcherMaya_turntable.create_turntable_animation()"))
    cmds.button(label= "Delete Turntable",
                command = ("import VStitcherMaya_turntable; reload(VStitcherMaya_turntable); VStitcherMaya_turntable.delete_turntable_dialog()"))
  
    cmds.showWindow(window)
