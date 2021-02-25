import requests

base_path = 'http://127.0.0.1:'

def get():
    """
    Using for shutdown the servers
    """
    resp = requests.get(f"{base_path}5000/stop_server")
    if resp.status_code != 200:
        raise Exception("stop_server has failed")
    resp = requests.get(f"{base_path}5001/stop_server")
    if resp.status_code != 200:
        raise Exception("stop_server has failed")
    return(resp.json().get("Servers has been stoped"))


if __name__ == '__main__':
    get