import asyncio
import logging
import os
import ssl
import sys
import argparse

import aiohttp
from aiohttp import web


def setup_routes(app, static_dir):

    # static path '/' will serve static files from the root path but will interfere with index
    app.router.add_static('/', path=static_dir, name='static')


def main(host_ip, port, static_dir, cert_file, key_file):


    assert static_dir != None, "Static Dir must not be None"

    print(aiohttp.__version__)

    if not os.path.exists(cert_file):
        assert False, F"cert file does not exist"

    if not os.path.exists(key_file):
        assert False, F"key file does not exist"

    if not os.path.exists(static_dir):
        assert False, F"static dir {static_dir} does not exist"


    app = web.Application()

    setup_routes(app, static_dir)

    ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ssl_context.load_cert_chain(certfile=cert_file,keyfile=key_file)

    web.run_app(app, host=host_ip, port=port, ssl_context=ssl_context)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Webserver")

    parser.add_argument('--host',   '-i', action='store', dest="host_ip",  default="0.0.0.0", help="ip to listen to",   type=str)
    parser.add_argument('--port',   '-p', action='store', dest="port",     default=443,        help="port to listen on", type=int)
    parser.add_argument('--static', '-s', action='store', dest="static_dir", help="static directory full path", type=str)
    parser.add_argument('--cert',   '-c', action='store', dest="cert_file",  help="the cert and chain file",type=str)
    parser.add_argument('--key',    '-k', action='store', dest="key_file",   help="the private key file", type=str)

    pargs = parser.parse_args()

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

    sys.exit(main(pargs.host_ip, pargs.port, pargs.static_dir, pargs.cert_file, pargs.key_file))





