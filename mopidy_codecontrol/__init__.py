    
import os

import tornado.web

from mopidy import config, ext

__version__="1.1.5"
logger - logging.getLogger(__name__)

class MyRequestHandler(tornado.web.RequestHandler):
    def initialize(self, core):
        self.core = core

    def get(self):
        self.write(
            'Hello, world! This is Mopidy %s' %
            self.core.get_version().get())


def my_app_factory(config, core):
    return [
        ('/', MyRequestHandler, {'core': core})
    ]


class MyWebClientExtension(ext.Extension):
    ext_name = 'mywebclient'

    def setup(self, registry):
        registry.add('http:app', {
            'name': self.ext_name,
            'factory': my_app_factory,
        })
