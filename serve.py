import BaseHTTPServer
import SimpleHTTPServer
import ssl
import os
import sys

DIR = sys.argv[1]
HOST = sys.argv[2]
PORT = int(sys.argv[3])

package_dir = os.getcwd()
os.chdir(DIR)
httpd = BaseHTTPServer.HTTPServer(
    (HOST, PORT),
    SimpleHTTPServer.SimpleHTTPRequestHandler
)
httpd.socket = ssl.wrap_socket(
    httpd.socket,
    certfile=os.path.join(package_dir, 'server.pem'),
    server_side=True,
)

address = 'https://{}:{}'.format(HOST, PORT)
os.system('open ' + address)

httpd.serve_forever()
