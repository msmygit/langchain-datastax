#!/usr/bin/env python

import sys
import traceback
from importlib.machinery import SourceFileLoader

if __name__ == "__main__":
    files = sys.argv[1:]
    has_failure = False
    for file in files:
        try:
            SourceFileLoader("x", file).load_module()
        except (ImportError, FileNotFoundError):  # noqa: PERF203
            has_faillure = True
            print(file)
            traceback.print_exc()
            print()

    sys.exit(1 if has_failure else 0)
