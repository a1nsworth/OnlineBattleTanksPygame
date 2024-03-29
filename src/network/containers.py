from dependency_injector import containers, providers
from . import network


class Container(containers.DeclarativeContainer):
    config = providers.Configuration(strict=True, )

    client_singleton = providers.Singleton(
        network.Client,
        ipv4=config.server.host,
        port=config.server.port.as_int(),
    )

    server_singleton = providers.Singleton(
        network.Server,
        ipv4=config.server.host,
        port=config.server.port.as_int(),
    )
