from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import time
import shutil
import json
from word_def import Enlightenmint

port = 8080
VBOX_GATEWAY_IP = "10.0.2.2"  # default gateway IP of VirtualBox
LOCALHOST_IP = "127.0.0.1"  # default localhost IP

mint = Enlightenmint()
usr = 'eda'

class HTTPServerRequestHandler(BaseHTTPRequestHandler):

    def set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', self.get_mimetype())
        self.end_headers()

    def get_mimetype(self):
        if self.path.endswith('.html'):
            return 'text/html'
        elif self.path.endswith('.css'):
            return 'text/css'
        elif self.path.endswith('.txt'):
            return 'text/plain'
        elif self.path.endswith('.js'):
            return 'application/javascript'
        elif self.path.endswith('.json'):
            return 'application/json'

    def process_query(self):
        query_splice = self.path.split('?')
        if len(query_splice) == 2:
            self.path = query_splice[0]
            print(self.path)
            query = query_splice[1].lower()
            definitions = mint.define(query)
            print(query)
            print(definitions)
            with open(query+'.json', 'w') as outfile:
                json.dump(definitions, outfile)
            with open('current_word', 'w') as outfile:
                outfile.write(query)

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        try:
            self.process_query()
            requestedFile = open(os.curdir + os.sep + self.path, 'rb')
            self.set_headers()
            self.wfile.write(requestedFile.read())
            requestedFile.close()
        except IOError:
            self.send_error(404, 'File not found: %s' % self.path)
            self.end_headers()

    def do_HEAD(self):
        if self.path == '/':
            self.path = '/index.html'
        try:
            if not os.path.exists(os.curdir + os.sep + self.path):
                raise IOError()
            self.set_headers()
        except IOError:
            self.send_error(404, 'File not found: %s' % self.path)
            self.end_headers()

def run():
    try:
        print('Starting server on port %d...' % port)
        # mint.load_user(usr)
        server_address = (LOCALHOST_IP, port)
        httpd = HTTPServer(server_address, HTTPServerRequestHandler)
        print('Running server...')
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\nKeyboardInterrupt detected, shutting down server...')
        # mint.save_user(usr)
        httpd.socket.close()
run()
