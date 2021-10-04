import json

from logging import exception
from yaml import load, FullLoader
from os import environ, getenv, getcwd
from pathlib import Path

from src.helpers.LoggingHelper import CustomLogging


def config():
    """
    Script contendo as configurações inicias do projeto

    Alguns paramentros globais armazenados no arquivo yml do projeto. Para invocalos basta chamar a
    função os.getenv('param')
    """

    # environ['DIRETORIO_PROJETO'] = str(Path('.').absolute())
    environ['DIRETORIO_PROJETO'] = str(Path(getcwd()))

    logs = CustomLogging()

    logs.create_stream()
    logs.create_debug()

    # Lê o arquivo yml do projeto e cria as variáveis globais do projeto.
    try:

        with open(f'{getenv("DIRETORIO_PROJETO")}/configs/.config.yml', encoding='UTF-8') as f:
            data = load(f, Loader=FullLoader)

        # Define o tipo de ambiente.
        if data['ENV'] == 'PRODUCAO':
            environ['ENV'] = 'PRODUCAO'
            environ['EMAIL'] = json.dumps(data['email_prod'])

        elif data['ENV'] == 'DESENVOLVIMENTO':
            environ['ENV'] = ''
            environ['EMAIL'] = json.dumps(data['email_teste'])

        # Lista de emails.
        environ['EMAIL_PROD'] = json.dumps(data['email_prod'])
        environ['EMAIL_TESTE'] = json.dumps(data['email_teste'])

        # Lista de processos.
        environ['PROCESSOS'] = json.dumps(data['processos'])

        # Lista de empresas com suas informações.
        environ['EMPRESAS'] = json.dumps(data['empresas'])

    except Exception:
        exception('Não foi possível ler o arquivo .gitlab-ci.yml')


config()
