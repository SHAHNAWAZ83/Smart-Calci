import sys
from cx_Freeze import setup,Executable

import os

PYTHON_INSTALL_DIR=os.path.dirname(sys.executable)
os.environ['TCL_LIBRARY']=os.path.join(PYTHON_INSTALL_DIR,'tcl','tcl8.6')
os.environ['TK_LIBRARY']=os.path.join(PYTHON_INSTALL_DIR,'tcl','tk8.6')

include_files=[(os.path.join(PYTHON_INSTALL_DIR,'DLLS','tk86t.dll'),os.path.join('lib','tk86.dll')),
               (os.path.join(PYTHON_INSTALL_DIR,'DLLS','tcl86t.dll'),os.path.join('lib','tcl86.dll'))]

base=None

if sys.platform=='win32':
    base="win32GUI"

executables = [Executable('smartcalculater.py',base=base , icon=r"C:\Users\Shahnawaz\PycharmProjects\CALCULATOR\calu.ico.ico",
                          shortcutName=" Smart Calci",
                          shortcutDir="DesktopFolder")]
setup(name="latest calculator Installer",
      version='0.1',
      author='Khan shahnawaz',
      description="MY FISRT GUI INSTALLER",
      options={'build_exe':{'include_files':include_files}},
      executables=executables)