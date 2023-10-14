import random
from bottle import Bottle, request

class WebServer(Bottle):

    def __init__(self):
        super().__init__()

        self.route("/", ["GET"], self.start)

    def start(self):
        return "Hello World!"

if __name__ == "__main__":
    host_name = "localhost"
    server_port = 8080
    app = WebServer()
    app.run(host=host_name, port=server_port)
    print("Server stopped.")