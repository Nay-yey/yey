import os
print("1")
from http.server import HTTPServer, CGIHTTPRequestHandler# Make sure the server is created at current directory
print("2")
os.chdir('.')
print("3")
# Create server object listening the port 80
server_object = HTTPServer(server_address=('', 80), RequestHandlerClass=CGIHTTPRequestHandler)
print("4")
# Start the web server
server_object.serve_forever()

print("5")