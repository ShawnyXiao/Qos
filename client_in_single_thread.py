import requests
import json
import time
import thread
import sys


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
        }
    ]

    headers = {'content-type': 'application/json'}

    client_id = sys.argv[1]
    file = open("qos_" + str(client_id) + ".csv", "w+")

    try:
        file.write("url,service_name,request_params,response,elapsed_time,current_time\n")

        while True:
            time.sleep(5)

            for url in urls:
                for payload in payloads:
                    start_time = time.time()
                    try:
                        response = requests.post(url, data=json.dumps(payload), headers=headers).json()
                    except Exception as e:
                        elapsed_time = sys.maxint
                    else:
                        elapsed_time = int(round((time.time() - start_time) * 1000))

                    if payload.get("params"):
                        request_params = "|".join(map(str, payload.get("params")))
                    else:
                        request_params = None
                    recode = "%s,%s,%s,%s,%d,%s\n" % (url, payload["method"], request_params, response["result"], elapsed_time, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                    file.write(recode)

                    print "%s,%s,%s,%s,%d,%s\n" % (url, payload["method"], request_params, response["result"], elapsed_time, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    finally:
        file.close()


if __name__ == "__main__":
    main()