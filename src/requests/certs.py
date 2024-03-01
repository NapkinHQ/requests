#!/usr/bin/env python

"""
requests.certs
~~~~~~~~~~~~~~

This module returns the preferred default CA certificate bundle. There is
only one — the one from the certifi package.

If you are packaging Requests, e.g., for a Linux distribution or a managed
environment, you can change the definition of where() to return a separately
packaged CA bundle.
"""

import pathlib
import os


def where():
    curr_dir = pathlib.Path(__file__).parent.resolve()
    return os.path.join(curr_dir, "cacert.pem")


if __name__ == "__main__":
    print(where())
