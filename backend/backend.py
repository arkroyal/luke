#!/usr/bin/python3

import tornado.ioloop
import tornado.web
import json
import os

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        ret = {'message':'world'}
        self.write(json.dumps(ret))

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    env_dist = os.environ
    if 'BACKEND_PORT' in env_dist.keys():
        port = int(env_dist['BACKEND_PORT'])
    else:
        port = 8888
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()
