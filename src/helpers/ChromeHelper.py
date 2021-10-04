#pip install chromedriver-binary-auto

from selenium import webdriver
from selenium.common.exceptions import SessionNotCreatedException
from selenium.webdriver.chrome.options import Options
from logging import info
# from fake_useragent import UserAgent
from json import dumps
from pathlib import Path
import chromedriver_binary


class ChromeDriver:

    def __init__(self, root_dir: str, port: str, mode):
        self.__chrome_options = Options()
        self.__root_dir = root_dir
        self.__chrome_options.add_experimental_option('debuggerAddress', f'localhost:{port}')
        self.__mode = mode

        self.__prefs = {"download": {
            "default_directory": str(Path(self.__root_dir, 'documents', 'downloads')),
            "directory_upgrade": True,
            "extensions_to_open": ""
        }}

    def driver(self) -> webdriver.Chrome:
        try:
            if self.__mode == 0:
                driver = webdriver.Chrome(chrome_options=self.__chrome_options)
            else:
                options = Options()
                options.add_experimental_option("prefs", self.__prefs)
                # options.add_argument("--disable-popup-blocking")
                # options.add_argument("--start-maximized")
                # options.add_argument('--kiosk-printing')

                # ua = UserAgent()
                # user_agent = ua.random
                # print(user_agent)
                # options.add_argument(f'user-agent={user_agent}')

                driver = webdriver.Chrome(options=options)

        except SessionNotCreatedException:
            raise Exception('Versão do Chrome incompatível com a do driver')

        except Exception:
            raise Exception('Não foi possível inicializar o Chrome Driver do Selenium')

        else:
            info('Sessão do Chrome iniciada com sucesso!')

            return driver
