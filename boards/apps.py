from django.apps import AppConfig
from suit.apps import DjangoSuitConfig


class BoardsConfig(AppConfig):
    name = 'boards'


class SuitConfig(DjangoSuitConfig):
    layout = 'vertical'
