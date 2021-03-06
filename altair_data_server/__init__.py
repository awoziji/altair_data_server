"""Altair data server"""
__version__ = "0.5.0.dev0"
__all__ = [
    "AltairDataServer",
    "data_server",
    "data_server_proxied",
    "Provider",
    "Resource",
]

from ._altair_server import AltairDataServer, data_server, data_server_proxied
from ._provide import Provider, Resource
