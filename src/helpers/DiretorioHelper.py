import sys
from os import makedirs, walk, scandir, path, getenv
from pathlib import Path

# from logging import debug


class Diretorio:
    """
    Manipula a criação de diretórios.

    :param: self.__diretorio - Diretório a ser criado.
    :param: self.__abs_path - Diretório absoluto do projeto
    """

    def __init__(self, custom_path: str):
        self.__path = custom_path
        self.__define_diretorio_projeto()

    def __define_diretorio_projeto(self):
        diretorio_padrao = getenv('DIRETORIO_PROJETO')

        if diretorio_padrao is not None:
            self.__abs_path = diretorio_padrao

        else:
            self.__abs_path = sys.path[0]

    def cria_path(self):
        """ Cria diretório apartir de um caminho """

        # Verifica se o caminho existe
        if not path.exists(self.__path):
            # debug(f'Criando diretório {self.__path}...')
            makedirs(self.__path)

    def cria_path_abs(self) -> str:
        """ Cria diretório apartir do caminho absoluto do projeto """

        diretorio = f'{self.__abs_path}\\{self.__path}'

        # Verifica se o caminho existe
        if not path.exists(diretorio):
            # debug(f'Criando diretório {diretorio}...')
            makedirs(diretorio)

        return diretorio

    def lista_todos_arquivos(self) -> list:
        """
        Retorna uma lista contendo todos os arquivos nas pastas e subpastas do diretório padrão.
        Essa lista contem um dicionário com o caminho e o nome do arquivo.

        :return -> list: Lista contendo o caminho completo bem como o nome do arquivo.
        """

        lista_arquivos = []

        for root, dirs, files in walk(self.__path):
            for filename in files:
                lista_arquivos.append({
                    'caminho': root,
                    'arquivo': filename
                })

        return lista_arquivos

    def lista_arquivos_por_diretorio(self):
        """ Lista os arquivos por pasta """

        with scandir(self.__path) as entries:
            entries = Path(self.__path)

            for entry in entries.iterdir():
                print(entry.name)
                if entry is Path:
                    with scandir(entry) as _dir:
                        for files in _dir:
                            print(files.name)

    @property
    def path(self):
        return self.__path

    @property
    def abs_path(self):
        return self.__abs_path
