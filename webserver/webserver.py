import asyncio
import logging
import time
import os
import sys
import argparse

import aiohttp
from aiohttp import web



def setup_routes(app, static_dir):

    # static path '/' will serve static files from the root path but will interfere with index
    #app.router.add_static('/static/', path=static_dir, name='static')
    app.router.add_static('/', path=static_dir, name='static')


def main(host_ip, port, static_dir):


    assert static_dir != None, "Static Dir must not be None"

    print(aiohttp.__version__)

    if not os.path.exists(static_dir):
        os.makedirs(static_dir)


    app = web.Application()


    setup_routes(app, static_dir)

    web.run_app(app, host=host_ip, port=port)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Webserver")

    parser.add_argument('--host',   '-i', action='store', dest="host_ip",  default="0.0.0.0", help="ip to listen to",   type=str)
    parser.add_argument('--port',   '-p', action='store', dest="port",     default=80,        help="port to listen on", type=int)
    parser.add_argument('--static', '-s', action='store', dest="static_dir", help="static directory full path", type=str)

    pargs = parser.parse_args()

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

    sys.exit(main(pargs.host_ip, pargs.port, pargs.static_dir))





