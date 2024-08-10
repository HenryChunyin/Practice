
from win32com.client import Dispatch
def createshortcut(shortcut_path, target_path):
    shortcut_path=shortcut_path.split(".")[0]+'.lnk'
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortcut(shortcut_path)
    shortcut.Targetpath = target_path
    shortcut.Save()

