from docker import APIClient

client = APIClient("http://localhost:2375")
print(client.containers())
