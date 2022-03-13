from typing import Any, Dict, List, Optional
from pydantic import BaseModel
from enum import Enum


class State(Enum):
    Running = "running"
    Stopped = "stopped"


class NetworkTypeModel(BaseModel):
    IPAMConfig: Any
    Links: Any
    Aliases: Any
    NetworkID: str
    EndpointID: str
    Gateway: str
    IPAddress: str
    IPPrefixLen: str
    IPv6Gateway: str
    GlobalIPv6Address: str
    GlobalIPv6PrefixLen: int
    MacAddress: str
    DriverOpts: Any


class ContainerNetworkModel(BaseModel):
    bridge: NetworkTypeModel


class ContainerLabelModel(BaseModel):
    pass


class MappedPorts(BaseModel):
    PrivatePort: int
    Type: str


class ContainerNetworkSettinsgModel(BaseModel):
    Networks: ContainerNetworkModel


class ContainerModel(BaseModel):
    Id: str
    Names: List[str]
    Image: str
    ImageID: str
    Ports: List[Dict[Any, Any]]
    Labels: Dict[str, str]
    State: State
    Ports = List[MappedPorts]
    Status: str
    NetworkSettings: ContainerNetworkSettinsgModel
    Mounts: List[Any]


test_container = {'Id': '5241a3f41efce48a0f9c4b8394f57b480403f37e7306246c67e6549bd4a1350c',
                  'Names': ['/zen_mcnulty'],
                  'Image': 'docker/getting-started',
                  'ImageID': 'sha256:bd9a9f73389835f470cc69edf12f472c1dca7f213e05f00a1e8211007c95028f',
                  'Command': "/docker-entrypoint.sh nginx -g 'daemon off;'",
                  'Created': 1647109382,
                  'Ports': [{'PrivatePort': 80, 'Type': 'tcp'}],
                  'Labels': {'desktop.docker.io/wsl-distro': 'Ubuntu-20.04', 'maintainer': 'NGINX Docker Maintainers <docker-maint@nginx.com>'},
                  'State': 'running',
                  'Status': 'Up 6 seconds',
                  'HostConfig': {'NetworkMode': 'default'},
                  'NetworkSettings': {'Networks': {'bridge': {'IPAMConfig': None, 'Links': None, 'Aliases': None, 'NetworkID': 'f30f49823b16ca96268ef45f17ffff8c73d675968eb18a5fda10456089b814f8', 'EndpointID': '52675a615cca84622ef70a1647aa6444c64b3b385411130ef96d006fb065d7d5', 'Gateway': '172.17.0.1', 'IPAddress': '172.17.0.2', 'IPPrefixLen': 16, 'IPv6Gateway': '', 'GlobalIPv6Address': '', 'GlobalIPv6PrefixLen': 0, 'MacAddress': '02:42:ac:11:00:02', 'DriverOpts': None}}},
                  'Mounts': []}

container = ContainerModel(**test_container)
print(container.NetworkSettings.Networks)
