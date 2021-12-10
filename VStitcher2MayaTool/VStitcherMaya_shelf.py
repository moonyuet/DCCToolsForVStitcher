import sys
from importlib import reload
import maya.cmds as cmds
import mtoa.utils as utils
import webbrowser

path = r"C:\Users\Kayla\Desktop\VStitcher2MayaTool"
sys.path.append(path)
IMG_PATH = path + "/img/"


MENU = "VStitche2Maya"

def delete_plugin_shelf():
    if cmds.shelfLayout(MENU, exists=True):
        cmds.deleteUI(MENU)


def plugin_shelf():
    delete_plugin_shelf()
    cmds.shelfLayout(MENU, parent="ShelfLayout")
    cmds.shelfButton(parent=MENU, annotation='Vstitcher2Maya',
                     command='import VStitcherMaya_layout_UI;reload(VStitcherMaya_layout_UI);VStitcherMaya_layout_UI.UI()')
plugin_shelf()