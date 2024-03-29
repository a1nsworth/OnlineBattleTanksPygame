import pygame
from dependency_injector import containers, providers
from . import application


class Container(containers.DeclarativeContainer):
    config = providers.Configuration(
        strict=True,
    )

    window_fabric = providers.Factory(
        application.Window,
        height=config.app.window.height,
        width=config.app.window.width,
        title=config.app.window.title,
        bg_color=pygame.Color("black"),
    )

    application_singleton = providers.Singleton(
        application.Application,
        window=window_fabric,
    )
