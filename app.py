from flask import Flask
from redis import Redis, RedisError
import os
import socket


app = Flask(__name__)

@app.route("/")
def hello():
    try:
        redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)
        visits = redis.incr("counter")
    except RedisError:
        visits = "cannot connect to Redis, counter disabled"

    html = "<pre>\nHello {name}!\n" \
           "Hostname: {hostname}\n" \
           "Visits: {visits}\n</pre>"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)