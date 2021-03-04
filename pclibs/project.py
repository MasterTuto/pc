import os
import re
import sys
import json
import base64
import shutil
import pathlib
import zipfile
from datetime import datetime as dt

from .arguments import Arguments
from .boilerplates import *
from .emaillib import Email

class Project:
    def __init__(self, arguments: Arguments, config: dict):
        self.arguments = arguments
        self.config = config
        self.current_path = self.__get_current_path().parent

    def __get_current_path(self) -> pathlib.Path:
        if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
            bundle_dir = pathlib.Path(sys._MEIPASS)
        else:
            bundle_dir = pathlib.Path(__file__).parent
        
        return pathlib.Path.cwd() / bundle_dir
    
    def __is_project_folder(self, folder: str) -> bool:
        return re.match(r'^pc_trabalho\d{2,2}_\d{9,9}$', folder)
    
    def __create_file_structure(self) -> pathlib.Path:
        number_of_existing_projects = 0
        for dir_item in self.current_path.iterdir():
            if self.__is_project_folder(dir_item.name):
                number_of_existing_projects += 1      

        number_of_existing_projects += 1 # if there is no, first folder must be 01

        project_number = str(number_of_existing_projects) if number_of_existing_projects > 9 else "0" + str(number_of_existing_projects)
        folder_name = f'pc_trabalho{project_number}_{self.config["enrollment"]}'
        self.package = f"trabalho{project_number}"

        self.project_root_folder = self.current_path / folder_name
        pathlib.Path( self.project_root_folder ).mkdir()

        return self.project_root_folder
    
    def __copy_itself_to_src(self) -> None:
        source      = self.current_path / sys.argv[0]
        destination = self.project_root_folder
        shutil.copy(source, destination)

    def __add_config(self, values: dict) -> None:
        destination = self.project_root_folder / "config.json"

        with destination.open("r", encoding="utf-8") as configfile:
            json_o = json.load(configfile)
        
        json_o.update(values)
        
        return json_o

    def __copy_config_to_src(self) -> None:
        source      = self.current_path / "config.json"
        destination = self.project_root_folder / "config.json"

        shutil.copy(source, destination)
        
        new_config = self.__add_config({
            'package': self.package
        })

        with destination.open("w", encoding="utf-8") as configfile:
            configfile.write( json.dumps(new_config, indent=4) )

    def create_new(self) -> str:
        if self.__is_project_folder( self.current_path.name ):
            return

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
        if self.__is_project_folder( self.current_path.name ):
            return
        
        self.project_root_folder.joinpath("assets").mkdir()
        self.project_root_folder.joinpath("assets", "styles").mkdir()
        self.project_root_folder.joinpath("assets", "images").mkdir()
        self.project_root_folder.joinpath("assets", "sounds").mkdir()

        self.project_root_folder.joinpath("controller").mkdir()
        self.project_root_folder.joinpath("view").mkdir()
        self.project_root_folder.joinpath("models").mkdir()
        
        with self.project_root_folder.joinpath("Principal.java").open("w", encoding="utf-8") as main_java_file:
            new_boilerplate = JAVAFX_BOILERPLATE.replace("$author$", self.config['author'])
            new_boilerplate = new_boilerplate.replace('$beginning$', dt.now().strftime("%d/%m/%Y %H:%M:%S"))
            new_boilerplate = new_boilerplate.replace('$software_name$', self.arguments.software_name)
            new_boilerplate = new_boilerplate.replace('$description$', self.arguments.description)
            new_boilerplate = new_boilerplate.replace('$package$', "com." + self.package)
            new_boilerplate = new_boilerplate.replace('$package_without_com$', self.package)

            main_java_file.write( new_boilerplate )
        
        with self.project_root_folder.joinpath("view", "main_view.fxml").open("w", encoding="utf-8") as main_java_file:
            main_java_file.write(MAIN_VIEW_BOILERPLATE)
        
        with self.project_root_folder.joinpath("controller", "MainController.java").open("w", encoding="utf-8") as main_controller_file:
            main_controller_file.write(MAIN_CONTROLLER_BOILERPLATE)
        
        with self.project_root_folder.joinpath("assets", "styles", "main_style.css").open("w", encoding="utf-8") as main_style_file:
            main_style_file.write(MAIN_STYLE_BOILERPLATE)
        
        with self.project_root_folder.joinpath("assets", "images", "corner.png").open("wb") as corner_image_file:
            corner_image_file.write( base64.standard_b64decode( CORNER_IMAGE ) )
    
    def compile_project(self) -> None:
        os.system(f"javac Principal.java")

    def execute(self) -> None:
        os.system(f"java Principal")
    
    def __delete_class_files_recurse(self, pathitem : pathlib.Path):
        for item in pathitem.iterdir():
            if item.is_dir():
                self.__delete_class_files_recurse(item)
            
            elif item.is_file():
                if item.name.endswith(".class"):
                    print("Arquivo apagado: " + item.name)
                    item.unlink()

    def delete_class_files(self) -> None:
        if self.__is_project_folder( self.current_path.name ):
            self.__delete_class_files_recurse( self.current_path )
    
    def __add_file_to_zip_recurse(self, zipfile: zipfile.ZipFile, pathitem: pathlib.Path, from_depth: int) -> None:
        if pathitem.name != "pc.py" and pathitem.name != "config.json" and not pathitem.name.endswith(".class"):
            if pathitem.is_dir():
                for item in pathitem.iterdir():
                    self.__add_file_to_zip_recurse(zipfile, item, from_depth)
            elif pathitem.is_file():
                print("\\".join(pathitem.parts[from_depth:]))
                zipfile.write(pathitem, "\\".join(pathitem.parts[from_depth:]))
    
    def zip_project(self) -> None:
        if self.__is_project_folder( self.current_path.name ):
            zipname = f'pc_{self.config["package"]}_{self.config["enrollment"]}.zip'
            zipfilename = self.current_path.parent.joinpath(zipname)
            
            with zipfile.ZipFile(zipfilename, "w") as zipf:
                self.__add_file_to_zip_recurse( zipf, self.current_path, len(self.current_path.parts)-1)
            
            print("Arquivo zip salvo em: " + '\\'.join(zipfilename.resolve().parts) )

    def send_email(self) -> None:
        if not self.__is_project_folder( self.current_path.name ):
            return

        print("[*] Conectando ao servidor...")
        email = Email(
            self.config['email'],
            self.config['password']
        )
        print("[^] Conectado ao servidor!")

        print("[*] Tentando fazer login...")
        if not email.login():
            print("[!] " + email.error_message)
            return
        print("[^] Logado com sucesso!")

        print("[*] Anexando arquivo .zip")
        zipname = f'pc_{self.config["package"]}_{self.config["enrollment"]}.zip'
        zipfilename = self.current_path.parent.joinpath(zipname)
        if not email.attach_zip( zipfilename ):
            print("[!] " + email.error_message)
            return
        print("[^] Anexado com sucesso!")
        
        
        print("[*] Enviando email para " + self.config['to'] + "..." )
        if input("\tTem certeza? [s/n] ")[0].lower() != 's':
            print("[!] Processo interrompido pelo usuario!")
            return

        subject = f"[pc][{self.config['package']}][{self.config['enrollment']}]"
        if not email.send_email(self.config['to'], subject):
            print(email.error_message)
            return
        print("[!] Email enviado com sucesso")        
