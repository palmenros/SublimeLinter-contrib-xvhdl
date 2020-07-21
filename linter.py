#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Bruno JJE
# Copyright (c) 2015 Bruno JJE
#
# License: MIT
#

"""This module exports the Xvhdl plugin class."""

from SublimeLinter.lint import Linter


class Xvhdl(Linter):

    """Provides an interface to xvhdl (from Xilinx Vivado Simulator)."""

    name = 'xvhdl'
    cmd = 'xvhdl_sublime_wrapper.bat ${folder} ${file} ${temp_file}'
    defaults = {
        'selector': 'source.vhdl',
    }

    tempfile_suffix = 'xvhdl.temp'

    # the following attributes are marked useless for SL4
    #version_args = '--version --nolog'
    #version_re = r'Vivado Simulator (?P<version>\d+\.\d+)'
    #version_requirement = '>= 2014.4'
    #tempfile_suffix = 'vhd'

    # Here is a sample xvhdl error output:
    # ----8<------------
    # ERROR: [VRFC 10-91] td_logic is not declared [/home/BrunoJJE/src/filtre8.vhd:35]
    # ----8<------------

    regex = (
        r"^((?P<error>ERROR: )|(?P<warning>WARNING: ))(?P<message>\[.*\].*)"
        r"\[(?P<path>.*):(?P<line>[0-9]+)\]"
    )

    def split_match(self, match):
        """
        Extract and return values from match.

        We override this method to prefix the error message with the
        linter name.

        """

        path = match.group("path")
        if not path.startswith("b:/users/pedro/appdata/local/temp/"):
            return None, None, None, None, None, None, None

        match, line, col, error, warning, message, near = super().split_match(match)

        if match:
            message = message

        return match, line, None, error, warning, message, near
