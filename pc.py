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
        project.create_new()

        if arguments.use_javafx:
            project.configure_javafx()
    else:
        if arguments.compile:
            project.compile_project()
        
        if arguments.execute:
            project.execute()

if __name__ == "__main__":
    main()