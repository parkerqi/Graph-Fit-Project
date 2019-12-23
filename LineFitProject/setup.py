from cx_Freeze import setup, Executable

setup(name = "twoDLinearLineFitGUI" ,
      version = "0.1" ,
      description = "find the linear best fit line in 2d" ,
      executables = [Executable("twoDLinearLineFitGUI.py")])

