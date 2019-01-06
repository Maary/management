import os
import configparser


class Config:
    _config = None
    current_path = os.getcwd()

    def __init__(self, file=None):
        if file is None:
            conf_path = "%s/app.conf" % os.getcwd()
        else:
            conf_path = os.path.normpath(os.path.join(os.getcwd(), file))
        conf = configparser.ConfigParser()
        conf.read(conf_path)
        self._config = conf

    def _get(self, sec, name):
        val = self._config.get(sec, name)
        return val.replace("\'", "")

    def get_string(self, sec, name):
        value = self._get(sec, name)
        return str(value)

    def get_int(self, sec, name):
        value = self._get(sec, name)
        return int(value)

    def get_strings(self, sec, name):
        values = self.get_string(sec, name)
        return values.split(",")

