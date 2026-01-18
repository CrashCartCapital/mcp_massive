#!/usr/bin/env python
"""
Backwards-compatible entrypoint script.
This script delegates to the main package CLI entry point.
"""

import os
import sys

# Add src directory to Python path so the package can be found
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from mcp_massive.server import poly_mcp as server
from mcp_massive import main

__all__ = ["server"]

if __name__ == "__main__":
    main()
