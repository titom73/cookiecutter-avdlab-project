"""Local filters for cookiecutter project."""

import ipaddress
from cookiecutter.utils import simple_filter


@simple_filter
def demo(network, hostid):
    net = ipaddress.ip_network(network)
    return next(net.hosts(), hostid)
