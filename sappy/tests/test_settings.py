# pylint: disable=missing-docstring,unused-variable,expression-not-assigned

from importlib import reload

from expecter import expect

from sappy import settings


def describe_get_address():

    def it_loads_host_from_env(monkeypatch):
        monkeypatch.setenv('SAPPY_HOST', "foobar")
        reload(settings)

        expect(settings.get_address()) == ("foobar", 8080)

    def it_loads_port_from_env(monkeypatch):
        monkeypatch.setenv('SAPPY_PORT', "1234")
        reload(settings)

        expect(settings.get_address()) == ("", 1234)
