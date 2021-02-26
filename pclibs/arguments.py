#coding: utf-8
import argparse

class Arguments:
    argument_list = [
        {
            'names': ['-create'],
            'attributes': {
                'help': 'Cria novo projeto na pasta atual, so pode ser usado com argumento "--use-javafx"',
                'action': 'store_true'
            }
        },
        {
            'names': ['-jfx', '--use-javafx'],
            'attributes': {
                'help': 'Ao criar novo projeto, adiciona boilerplate necessário para programas com JavaFX',
                'action': 'store_true',
                'dest': 'use_javafx'
            }
        },
        {
            'names': ['--javafx-version', '-jfxv'],
            'attributes': {
                'help': 'Mudar versão do JavaFX para baixar',
                'nargs': '?',
                'const': '11.0.2',
                'default': '11.0.2'
            }
        },
        {
            'names': ['--project-name', '-pn'],
            'attributes': {
                'help': 'Nome do programa',
                'default': 'Nome do programa',
                'dest': 'software_name'
            }
        },
        {
            'names': ['--project-description', '-desc'],
            'attributes': {
                'help': 'Descrição do programa',
                'default': 'Descrição do programa',
                'dest': 'description'
            }
        },
        {
            'names': ['-compile'],
            'attributes': {
                'help': 'Compilar codigo Java para *.class',
                'action': 'store_true',
            }
        },
        {
            'names': ['-execute', '-ex'],
            'attributes': {
                'help': 'Executar código .class (a partir da classe Principal.java)',
                'action': 'store_true',
                'dest': 'execute'
            }
        },
        {
            'names': ['-clean'],
            'attributes': {
                'help': 'Limpar os arquivos *.class (automatico com opção enviar)',
                'action': 'store_true'
            }
        },
        {
            'names': ['-send', '-submit'],
            'attributes': {
                'help': "Envia arquivo compactado por email, para email especificado no config.json",
                'action': 'store_true'
            }
        }
    ]

    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description="Gerencie, compile, limpe os *.class, compacte e envie seus projetos para disciplina de Concorrentes"
        )

        self.fill_arguments()
        self.parsed_arguments = vars(self.parser.parse_args())
    
    def __getitem__(self, item: str):
        return self.parsed_arguments[item]

    def __getattr__(self, item: str):
        return self.parsed_arguments[item]
    
    def fill_arguments(self) -> None:
        for argument in self.argument_list:
            self.parser.add_argument(*argument['names'], **argument['attributes'])