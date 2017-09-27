import requests
import json
import time


def main():
    url = "http://192.168.199.247:8888/"
    headers = {'content-type': 'application/json'}

    payload = {
        "method": "time",
        # "params": ["fuck!"],
        "jsonrpc": "2.0",
        "id": 0
    }
    start_time = time.time()
    response = requests.post(url, data=json.dumps(payload), headers=headers).json()
    elapsed_time = int(round((time.time() - start_time) * 1000))

    print elapsed_time # milliseconds

    print response["result"]

if __name__ == "__main__":
    main()