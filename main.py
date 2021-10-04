import configs.config
from src.helpers.ChromeHelper import ChromeDriver

from glob import glob
from time import sleep
from pathlib import Path
from os import system, getcwd, path
from logging import exception, info, debug
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.support import expected_conditions as e_c


ROOT_DIR = str(Path(getcwd()))
CHROME_PORT = '9222'
# environ['FILE_XLSX'] = str(Path(ROOT_DIR, 'documents', 'downloads', 'PROCV.xlsx'))


def create_profile():

    call_start_chrome = r'start "Chrome" chrome.exe'
    call_port = fr'--remote-debugging-port={CHROME_PORT}'
    chrome_profile = fr'{ROOT_DIR}\bin\chromeprofile'
    call_data_dir = fr'--user-data-dir="{chrome_profile}"'

    comm = fr'{call_start_chrome} {call_port} {call_data_dir}'

    system(comm)


def main(url, mode):

    if mode == 0:
        create_profile()

    try:
        pass

    except Exception:
        exception('Erro no projeto')




if __name__ == '__main__':

    # MODE igual a 0 -> Chrome Selenium Debug
    # MODE diferente de 0 -> Chrome Selenium Normal
    main('https://portalservicos.denatran.serpro.gov.br/#/home', 1)




