from loguru import logger

from discourtesy.utils import simple_message


class Dispatch:
    def __init__(self):
        self.commands = dict()
        self.components = dict()

    def add_command(self, command):
        self.commands[command.name] = command

    def add_component(self, component):
        self.components[component.name] = component

    async def execute_command(self, application, interaction):
        command_name = interaction["data"]["name"]

        try:
            command = self.commands[command_name]
        except KeyError:
            logger.warning(f"Command {command_name} could not be found.")

            return simple_message("This command is currently not available.")

        return await command(application, interaction)

    async def execute_component(self, application, interaction):
        component_name = interaction["data"]["custom_id"]

        try:
            component = self.components[component_name]
        except KeyError:
            logger.warning(f"Component {component_name} could not be found.")

            return

        return await component(application, interaction)
