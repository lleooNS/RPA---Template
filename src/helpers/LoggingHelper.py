import logging
from datetime import datetime

from src.helpers.DiretorioHelper import Diretorio


class ExceptionFormatter(logging.Formatter):

	def formatException(self, exc_info) -> str:
		result = super().formatException(exc_info)
		return self.__formata_linha(result.splitlines())

	def format(self, record) -> str:
		result = super().format(record)
		return result

	def __formata_linha(self, str_list: list):

		# O código a baixo é mágica. E um mágico nunca revela seus segredos ...

		lines = str_list
		max_length = max([len(line) for line in lines])
		result = "{0:*{align}{width}}\n".format('', align='^', width=max_length + 4)

		for line in lines:
			result += "* " + "{:{align}{width}}".format(line, align='', width=max_length) + " *\n"

		result += "{0:*{align}{width}}\n".format('', align='^', width=max_length + 4)

		return result


class CustomLogging:
	"""
	Log de execução customizado.
	Para iniciar a classe sem fazer confusão na chamada com a biblioteca logging,
	basta fazer a chamada da váriavel logo no início do código dessa forma:

	logging = CustomLogging()

	Com isso o log vai ter sido formatado sem precisar se preocupar em como faze-lo
	"""

	def __init__(self):
		self.__logging = logging.getLogger()

		self.__data = datetime.now()
		self.__dir = Diretorio(fr'logs\{self.__data.year}\{self.__data:%m}').cria_path_abs()
		self.__dir_log_app = fr'{Diretorio("logs").cria_path_abs()}\app.log'
		self.__dir_log = fr"{self.__dir}\app_{self.__data:%d}.log"

		self.__logging.setLevel(logging.DEBUG)

	def create_stream(self, filename: str = None):

		if filename is None:
			filename = self.__dir_log_app

		file_handler, handler = self.__format_stream(filename)

		self.__logging.addHandler(file_handler)
		self.__logging.addHandler(handler)

	def create_debug(self, filename: str = None):

		if filename is None:
			filename = self.__dir_log

		self.__logging.addHandler(self.__format_debug(filename))
		self.__inicia_log(filename)

	def __inicia_log(self, filename):
		with open(filename, encoding='UTF-8') as f, open(filename, 'a',  encoding='UTF-8') as log:
			if f.read().endswith('\n'):
				log.write('\n\n\n')

	def __format_stream(self, filename):
		formatter = self.__formater()[1]

		handler = logging.StreamHandler()
		handler.setFormatter(formatter)
		handler.setLevel(logging.INFO)

		file_handler = logging.FileHandler(filename=filename, mode='w', encoding='UTF-8')
		file_handler.setFormatter(formatter)
		file_handler.setLevel(logging.INFO)

		return file_handler, handler

	def __format_debug(self, filename):
		formatter = self.__formater()[0]

		file_handler = logging.FileHandler(filename=filename, encoding='utf-8')
		file_handler.setFormatter(formatter)
		file_handler.setLevel(logging.DEBUG)

		return file_handler

	def __formater(self) -> list:
		standard_formater = ExceptionFormatter('%(asctime)s %(filename)s %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
		info_formater = ExceptionFormatter('%(asctime)s %(levelname)s - %(message)s', datefmt='%H:%M:%S')

		return [standard_formater, info_formater]

	@property
	def logging(self):
		""":rtype: logging"""

		return self.__logging

	@property
	def diretorio_log(self) -> str:
		return self.__dir_log
