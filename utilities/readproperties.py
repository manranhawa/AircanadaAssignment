import configparser

config = configparser.RawConfigParser()
config.read(".\\configurtion/config.ini")

class ReadConfig():
    @staticmethod
    def getapplicationURL():
       url = config.get('common info','baseURL')
       return url