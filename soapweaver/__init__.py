"""
SOAPWeaver - Convert any SOAP API into an MCP server.

This package provides a framework for dynamically creating MCP (Model Context Protocol)
servers from web API configurations, making it easy to integrate SOAP APIs with AI assistants.
"""

__version__ = "0.1.0"
__author__ = "SOAPWeaver Contributors"

from .server import SOAPWeaver
from .models import APIConfig, APIEndpoint, APIConfig, RequestParam

__all__ = [
    "SOAPWeaver",
    "APIConfig", 
    "APIEndpoint",
    "AuthConfig",
    "RequestParam"
]
