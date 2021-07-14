"""
This script runs the blankFlaskApp application using a development server.
"""

from os import environ
from blankFlaskApp import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
#    HOST = environ.get('SERVER_HOST', 'localhost')
#    try:
#        PORT = int(environ.get('SERVER_PORT', '80'))
#    except ValueError:
#       PORT = 80
    app.run(HOST, PORT)
