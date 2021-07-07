import pathlib    
import os
import logging
import tornado.web

from mopidy import config, ext

__version__ = "1.1.5"

logger = logging.getLogger(__name__)

class MyRequestHandler(tornado.web.RequestHandler):
    def initialize(self, core):
        self.core = core

    def get(self):
        self.write(
            'Hello, world! This is Mopidy %s' %
            self.core.get_version().get())

def factory(config, core):
    return [
        ('/', MyRequestHandler, {'core': core})
    ]


class Extension(ext.Extension):
    
    dist_name = "Mopidy-Code-Control"
    ext_name = "codecontrol"
    version = __version__

    def get_default_config(self):
        return config.read(pathlib.Path(__file__).parent / "ext.conf")

    def get_config_schema(self):
        schema = super().get_config_schema()
        schema["ip"] = config.Hostname(optional=True)
        schema["port"] = config.Port(optional=True)
        schema["device_name"] = config.String(optional=True)
        return schema

    def setup(self, registry):
        registry.add(
            'http:app', {'name': self.ext_name, 'factory': factory}
        )
