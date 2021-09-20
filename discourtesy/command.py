class Command:
    def __init__(self, name, coroutine, input_type):
        self.name = name
        self.coroutine = coroutine
        self.input_type = input_type


def command(name, input_type=1):
    def decorator(coroutine):
        return Command(name, coroutine, input_type)

    return decorator
