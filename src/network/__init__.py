from dotenv import load_dotenv, find_dotenv

from .containers import Container

load_dotenv(find_dotenv())

container = Container()
container.config.server.host.from_env("HOST", as_=str)
container.config.server.port.from_env("PORT", as_=int)

