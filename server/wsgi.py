"""
WSGI config for server project.
It exposes the WSGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""
from django.core.wsgi import get_wsgi_application

from settings import BASE_DIR, STATIC_ROOT, MEDIA_ROOT

import os
import tornado.httpserver
import tornado.ioloop
import tornado.wsgi
import sys
import django.core.handlers.wsgi

sys.path.append(BASE_DIR)


def main():
        os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
        application = get_wsgi_application()
        container = tornado.wsgi.WSGIContainer(application)
	tornado_app = tornado.web.Application(
   	 [
          (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': STATIC_ROOT}),
	  (r'/media/(.*)', tornado.web.StaticFileHandler, {'path': MEDIA_ROOT}),
	  ('.*', tornado.web.FallbackHandler, dict(fallback=container)),
         ]
        )
        http_server = tornado.httpserver.HTTPServer(tornado_app)
        http_server.listen(80)
        tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
        main()
