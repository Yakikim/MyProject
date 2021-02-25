import requests

base_path = 'http://127.0.0.1:'

def get(server):
    """
    Using for shutdown the servers
    """
    resp = requests.get(server)
    if resp.status_code != 200:
        raise Exception(f"stop_server {server} has failed")
    return(f"Server {server} has been stoped")


if __name__ == '__main__':
    print(get(f"{base_path}5000/stop_server"))
    print(get(f"{base_path}5001/stop_server"))