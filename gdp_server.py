import http.server
import socketserver
import json
import re

import pandas as pd

df = pd.read_csv('gdp_db.csv', sep=';')


class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        #if self.path == '/api/BRA':
        if None != re.search('/api/*', self.path):
            self.send_response(200)
            self.send_header("Content-type" , "text/html")
            self.end_headers()
            path = self.path
            cod_pais = path.split('/')[2]
            df_response = df[df['codigo_pais']==cod_pais]
            json_response =  df_response.to_json(orient='records', lines=True)
            content = json.dumps(json_response)
            self.wfile.write(bytes(content, "utf8 "))
            #self.wfil

# Create an object of the above class
handler_object = MyHttpRequestHandler
PORT = 8000
my_server = socketserver.TCPServer(("", PORT),handler_object)
# Star the server
my_server.serve_forever()


# curl http://192.168.41.153:8000/api
# nc 127.0.0.1 8001
# No browser:  http://192.168.41.153:8000/api