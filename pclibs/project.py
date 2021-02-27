import os
import re
import sys
import json
import shutil
import pathlib
from datetime import datetime as dt

from .arguments import Arguments
from .javafx_manager import JavaFXManager
from .boilerplates import *

class Project:
    def __init__(self, arguments: Arguments, config: dict):
        self.arguments = arguments
        self.config = config
        self.current_path = self.__get_current_path().parent

    def __get_current_path(self):
        if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
            bundle_dir = pathlib.Path(sys._MEIPASS)
        else:
            bundle_dir = pathlib.Path(__file__).parent
        
        return pathlib.Path.cwd() / bundle_dir
    
    def __create_file_structure(self) -> pathlib.Path:
        number_of_existing_projects = 0
        for dir_item in self.current_path.iterdir():
            if re.match(r'^pc_trabalho[0-9]{2,2}_[0-9]{9,9}$', dir_item.name):
                number_of_existing_projects += 1      

        number_of_existing_projects += 1 # if there is no, first folder must be 01

        project_number = str(number_of_existing_projects) if number_of_existing_projects > 9 else "0" + str(number_of_existing_projects)
        folder_name = f'pc_trabalho{project_number}_{self.config["enrollment"]}'
        self.package = f"trabalho{project_number}"

        self.project_root_folder = self.current_path / folder_name

        self.project_root_folder.joinpath("src", "com", self.package).mkdir(parents=True)

        self.project_root_folder.joinpath("assets").mkdir()

        return self.project_root_folder / "src" / "com" / self.package
    
    def __copy_itself_to_src(self) -> None:
        if sys.argv[0].endswith(".py"):
            source      = self.current_path / sys.argv[0]
            destination = self.project_root_folder / "src"
            shutil.copy(source, destination)

        else:
            file_name = sys.argv[0]
            if not sys.argv[0].endswith(".exe"):
                file_name += file_name
            source      = self.current_path / file_name
            destination = self.project_root_folder / "src"
            shutil.copy(source, destination)

        shutil.copytree(self.current_path / "pclibs", destination / "pclibs")

    def __add_config(self, values: dict) -> None:
        destination = self.project_root_folder / "src" / "config.json"

        with destination.open("r", encoding="utf-8") as configfile:
            json_o = json.load(configfile)
        
        json_o.update(values)
        
        return json_o

    def __copy_config_to_src(self) -> None:
        source      = self.current_path / "config.json"
        destination = self.project_root_folder / "src" / "config.json"

        shutil.copy(source, destination)
        
        new_config = self.__add_config({
            'use_javafx': False,
            'package': self.package
        })

        with destination.open("w", encoding="utf-8") as configfile:
            configfile.write( json.dumps(new_config, indent=4) )

    def create_new(self) -> str:
        code_folder = self.__create_file_structure()

        with code_folder.joinpath('Principal.java').open('w', encoding='utf-8') as main_java_file:
            new_boilerplate = JAVA_BOILERPLATE.replace("$author$", self.config['author'])
            new_boilerplate = new_boilerplate.replace('$beginning$', dt.now().strftime("%d/%m/%Y %H:%M:%S"))
            new_boilerplate = new_boilerplate.replace('$software_name$', self.arguments.software_name)
            new_boilerplate = new_boilerplate.replace('$description$', self.arguments.description)
            new_boilerplate = new_boilerplate.replace('$package$', "com." + self.package)

            main_java_file.write( new_boilerplate )
        
        self.__copy_itself_to_src()
        self.__copy_config_to_src()
        
        return self.project_root_folder.parts[-1]
    
    def configure_javafx(self) -> None:
        if not self.project_root_folder.joinpath("lib").exists():
            self.project_root_folder.joinpath("lib").mkdir()
        
        if not self.project_root_folder.joinpath("bin").exists():
            self.project_root_folder.joinpath("bin").mkdir()
        
        if not self.project_root_folder.joinpath("assets").exists():
            self.project_root_folder.joinpath("assets").mkdir()
        
        if not self.project_root_folder.joinpath("src", "com", self.package, "view").exists():
            self.project_root_folder.joinpath("src", "com", self.package, "view").mkdir()
        
        with self.project_root_folder.joinpath("src", "com", self.package, "Principal.java").open("w", encoding="utf-8") as main_java_file:
            new_boilerplate = JAVAFX_BOILERPLATE.replace("$author$", self.config['author'])
            new_boilerplate = new_boilerplate.replace('$beginning$', dt.now().strftime("%d/%m/%Y %H:%M:%S"))
            new_boilerplate = new_boilerplate.replace('$software_name$', self.arguments.software_name)
            new_boilerplate = new_boilerplate.replace('$description$', self.arguments.description)
            new_boilerplate = new_boilerplate.replace('$package$', "com." + self.package)
            new_boilerplate = new_boilerplate.replace('$package_without_com$', self.package)

            main_java_file.write( new_boilerplate )
        
        with self.project_root_folder.joinpath("src", "com", self.package, "view", "main_view.fxml").open("w", encoding="utf-8") as main_java_file:
            main_java_file.write(MAIN_VIEW_BOILERPLATE)

        jfx_manager = JavaFXManager()
        for message in jfx_manager.download():
            sys.stdout.write(message)
        
        print() # só adiciona nova linha
        
        jfx_manager.extract_to(self.project_root_folder)
            
    
    def compile_project(self) -> None:
        if self.config['use_javafx']:
            command = f"{self.config['javahome']}\\bin\\javac --module-path ..\\lib --add-modules javafx.fxml,javafx.controls com/{self.config['package']}/Principal.java"
            os.system(command)
        
        else:
            os.system(f"{self.config['javahome']}\\bin\\javac com/{self.config['package']}/Principal.java")

    def execute(self) -> None:
        if self.config['use_javafx']:
            command = f"{self.config['javahome']}\\bin\\java --module-path ..\\lib --add-modules javafx.fxml,javafx.controls com/{self.config['package']}/Principal"
            os.system(command)
        
        else:
            os.system(f"{self.config['javahome']}\\bin\\java com/{self.config['package']}/Principal")
    
    def zip_project(self) -> None:
        pass

    def send_email(self) -> None:
        pass