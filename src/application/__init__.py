from .containers import Container

container = Container()
container.config.from_yaml("application/config.yml")
