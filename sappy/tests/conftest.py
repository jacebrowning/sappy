"""Unit tests configuration file."""

import log


def pytest_configure(config):
    log.init(debug=True)

    terminal = config.pluginmanager.getplugin("terminal")
    terminal.TerminalReporter.showfspath = False
