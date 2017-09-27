from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

from jsonrpc import JSONRPCResponseManager, dispatcher

import time
import socket


@Request.application
def application(request):
    # Dispatcher is dictionary {<method_name>: callable}
    dispatcher["time"] = lambda : time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    dispatcher["echo"] = lambda s: s
    dispatcher["add"] = lambda a, b: a + b

    response = JSONRPCResponseManager.handle(request.data, dispatcher)
    return Response(response.json, mimetype='application/json')


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()

    run_simple(ip, 8888, application)
