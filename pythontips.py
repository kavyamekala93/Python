# virtual environments in Python enable to use multiple versions of Python on the same machine, we can use different versions of python for different python projects on the same machine
# pip install virtualenv

# Creating virtual environments:
# virtualenv <env_name>
# virtualenv --python = python3.5 pluralsight(project name)
# Activate Virtual environment:
  source pythonprojectpath/bin/activate
# "prompt" message is popped up
# debugging code: run in debug mode, step over and Evaluate functionalities

# to create Executable file: use pyinstaller
# pip install pyinstaller
# refer pyinstaller.org to see various features
# To create .exe file: navigate to the main code file path in the command prompt, type "pyinstaller main.py"
# build and dist folders are created, navigate to the dist folder and you will be able to see th e.exe file along with dll and pyd files
# to run the exe : navigate to the exe path and type  :\main.exe
# tp package all files (exe, dll, pyd and other files) into only one folder: type:  "pyinstaller --onefile .\main.py"

# setup wizard: download and use innosetup