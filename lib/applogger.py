import logging
import inspect
from appconfig import AppConfig, ProductionAppConfig


class AppLogger:
    
    def __init__(self, module, appconfig):
        self.log = logging.getLogger(module)
    
        # set formatter
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
        handler.setFormatter(formatter)
        self.log.addHandler(handler)
        
        # set loglevel
        loglevel = logging.INFO
        if appconfig.ENV != 'PROD':
            loglevel = logging.DEBUG
        self.log.setLevel(loglevel)
        loglevelName = logging.getLevelName( loglevel )
            
        self.log.debug("AppLogger instanciated for module <%s> and loglevel <%s>" % (module, loglevelName))
    
    @staticmethod
    def caller_name():
        frm = inspect.stack()[2]
        mod = inspect.getmodule(frm[0])
        return mod.__name__

    @staticmethod
    def create_instance(module=None, appconfig=AppConfig().create_instance() ):
        if module == None:
            module = AppLogger.caller_name()
        result = AppLogger(module, appconfig)
            
        return result    
    
    def error(self, msg):
        self.log.error(msg)
    
    def warn(self, msg):
        self.log.warn(msg)
    
    def info(self, msg):
        self.log.info(msg)
        
    def debug(self, msg):
        self.log.debug(msg)
    