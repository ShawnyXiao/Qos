import json
import sys
import time

import requests


def main():
    urls = [
        "http://192.168.199.133:8888/",
        "http://192.168.199.246:8888/",
        "http://192.168.199.101:8888/",
        "http://192.168.199.236:8888/",
        "http://192.168.199.249:8888/",
        "http://192.168.199.163:8888/",
        "http://192.168.199.231:8888/",
        "http://192.168.199.142:8888/",
        "http://192.168.199.176:8888/",
        "http://192.168.199.207:8888/"
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