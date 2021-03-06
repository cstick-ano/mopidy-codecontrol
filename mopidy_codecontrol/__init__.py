import pathlib    
import os
import logging
import tornado.web

from mopidy import config, ext, core

__version__ = "1.1.5"

logger = logging.getLogger(__name__)

class MyRequestHandler(tornado.web.RequestHandler):
    def initialize(self, core):
        self.core = core

    def get(self):
        self.write(
            'Hello, world! This is Mopidy %s' %
            self.core.get_version().get())
        self.write(
            'Now playing %s' %
            self.core.playback.get_current_tl_track())

class PlayRequestHandler(tornado.web.RequestHandler):
    def initialize(self, core):
        self.core = core
    def get(self):
        self.core.playback.play()
        
class PauseRequestHandler(tornado.web.RequestHandler):
    def initialize(self, core):
        self.core = core
    def get(self):
        self.core.playback.pause()
        
class NextRequestHandler(tornado.web.RequestHandler):
    def initialize(self, core):
        self.core = core
    def get(self):
        self.core.playback.next()
        
class PreviousRequestHandler(tornado.web.RequestHandler):
    def initialize(self, core):
        self.core = core
    def get(self):
        self.core.playback.previous()        

def factory(config, core):
    return [
        ('/', MyRequestHandler, {'core': core}),
        ('/play', PlayRequestHandler, {'core':core}),
        ('/pause', PauseRequestHandler, {'core':core}),
        ('/next', NextRequestHandler, {'core':core}),
        ('/previous', PreviousRequestHandler, {'core':core})
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
        schema["device_name"] = config.String()
        return schema

    def setup(self, registry):
        registry.add(
            'http:app', {'name': self.ext_name, 'factory': factory}
        )
