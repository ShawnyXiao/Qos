import requests
import json
import time
import thread


def request_in_thread(url, payload, thread_name, delay):
    headers = {'content-type': 'application/json'}
    while True:
        time.sleep(delay)

        start_time = time.time()
        response = requests.post(url, data=json.dumps(payload), headers=headers).json()
        elapsed_time = int(round((time.time() - start_time) * 1000))

        print "%s: (url, method, elapsed, response, time) (%s, %s, %d, %s, %s)" % (thread_name, url, payload["method"], elapsed_time, response["result"], time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


def main():
    urls = [
        "http://172.18.196.25:8888/",
        "http://172.18.196.28:8888/",
        "http://172.18.196.35:8888/",
        "http://172.18.196.36:8888/",
        "http://172.18.196.37:8888/",
        "http://172.18.196.38:8888/",
        "http://172.18.196.39:8888/",
        "http://172.18.196.40:8888/",
        "http://172.18.196.41:8888/",
        "http://172.18.196.42:8888/",
        "http://172.18.196.43:8888/",
        "http://172.18.196.45:8888/",
        "http://172.18.196.46:8888/",
        "http://172.18.196.47:8888/",
        "http://172.18.196.48:8888/",

        "http://172.18.196.34:8888/",
        "http://172.18.196.53:8888/",
        "http://172.18.196.55:8888/",
        "http://172.18.196.51:8888/",
        "http://172.18.196.52:8888/",
        "http://172.18.196.54:8888/",
        "http://172.18.196.56:8888/",
        "http://172.18.196.57:8888/",
        "http://172.18.196.58:8888/",
        "http://172.18.196.59:8888/",
        "http://172.18.196.60:8888/",
        "http://172.18.196.61:8888/",
        "http://172.18.196.62:8888/",
        "http://172.18.196.63:8888/",
        "http://172.18.196.69:8888/",
        "http://172.18.196.64:8888/",
        "http://172.18.196.68:8888/",
        "http://172.18.196.65:8888/",
        "http://172.18.196.66:8888/",
        "http://172.18.196.67:8888/",
    ]
    payloads = [{
            "method": "time",
            "jsonrpc": "2.0",
            "id": 0
        }, {
            "method": "echo",
            "params": ["Echo me!"],
            "jsonrpc": "2.0",
            "id": 0
        }, {
            "method": "add",
            "params": [520, 1314],
            "jsonrpc": "2.0",
            "id": 0
        }, {
            "method": "heavy",
            "jsonrpc": "2.0",
            "id": 0
        }
    ]

    for i in range(len(urls)):
        for j in range(len(payloads)):
            try:
                thread.start_new_thread(request_in_thread, (urls[i], payloads[j], "Thread-" + str(i) + "-" + str(j), 2))
            except:
                print "Error: unable to start thread"

    while True:
        pass;


if __name__ == "__main__":
    main()