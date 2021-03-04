import json
from pclibs.arguments import Arguments
from pclibs.project import Project

def main():
    arguments = Arguments()
    config = None
    with open("config.json", "r", encoding="utf-8") as configfile:
        config = json.load(configfile)

    project = Project(arguments, config)

    if arguments.create:
        print("Criando projeto...")
        project_folder = project.create_new()

        if arguments.use_javafx:
            print("Configurando JavaFX...")
            project.configure_javafx()
        
        print("Projeto criado em " + project_folder)
    else:
        if arguments.compile:
            print("Compilando projeto...")
            project.compile_project()
        
        if arguments.execute:
            print("Executando projeto...")
            project.execute()
        
        if arguments.clean:
            print("Limpando arquivos *.class...")
            project.delete_class_files()
        
        if arguments.zip:
            print("Compactando arquivo no .zip...")
            project.zip_project()
        
        if arguments.submit:
            print("Iniciando processo de envio do email...")
            project.send_email()

if __name__ == "__main__":
    main()
