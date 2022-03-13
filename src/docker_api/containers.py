from docker import DockerClient
from src.models.container import ContainerModel

class Container:
    def __init__(self,container:ContainerModel) -> None:
        self.name = container.Names[0]
        self.ip_address = container.NetworkSettings.Networks
        

def container_factory(api_address):
    api = DockerClient(base_url=api_address)
    return [Container(container) for container in api.containers()]
    