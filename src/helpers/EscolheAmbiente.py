from os import getenv


class EscolheAmbiente:

    @staticmethod
    def env(env):
        if env is not None:
            return env

        elif getenv('ENV'):
            return True

        elif getenv('ENV') == '':
            return False

        else:
            raise Exception('Env não definida!')
