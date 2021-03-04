import shutil
import json

with open("pc.py", "r", encoding="utf-8") as pc_file:
    pc_py = pc_file.read()

with open("pclibs\\arguments.py", "r", encoding="utf-8") as pc_file:
    arguments_py = pc_file.read()

with open("pclibs\\boilerplates.py", "r", encoding="utf-8") as pc_file:
    boilerplates_py = pc_file.read()

with open("pclibs\\emaillib.py", "r", encoding="utf-8") as pc_file:
    emaillib_py = pc_file.read()

with open("pclibs\\project.py", "r", encoding="utf-8") as pc_file:
    project_py = pc_file.read()

pc_py = pc_py.replace("from pclibs.arguments import Arguments", "").replace("from pclibs.project import Project", "")
project_py = project_py.replace("from .arguments import Arguments", "").replace("from .boilerplates import *", "")
project_py = project_py.replace("from .emaillib import Email", "")
project_py = project_py.replace("self.current_path = self.__get_current_path().parent", "self.current_path = self.__get_current_path()")

bundle_py = emaillib_py + "\n\n" + boilerplates_py + "\n\n" + arguments_py + "\n\n" + project_py + "\n\n" + pc_py

with open("dist\\pc.py", "w", encoding="utf-8") as bundle_file:
    bundle_file.write(bundle_py)

shutil.copy("config.json", "dist\\config.json")
