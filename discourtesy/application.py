import importlib

from nacl.signing import VerifyKey
from starlette.applications import Starlette

from .command import Command
from .component import Component
from .dispatch import Dispatch
from .routes import IndexRoute, InteractionRoute

version = "0.1.0"


class Application(Starlette):
    def __init__(self):
        super().__init__(routes=[IndexRoute(), InteractionRoute()])

        self.dispatch = Dispatch()

        self.add_plugin("__main__")

        self.public_key = None
        self.verify_key = None

    def set_public_key(self, public_key):
        self.public_key = bytes.fromhex(public_key)
        self.verify_key = VerifyKey(self.public_key)

    def add_plugin(self, path):
        module = importlib.import_module(path)

        for name in dir(module):
            attribute = getattr(module, name)

            if isinstance(attribute, Command):
                self.dispatch.add_command(attribute)

            if isinstance(attribute, Component):
                self.dispatch.add_component(attribute)
