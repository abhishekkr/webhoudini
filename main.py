"""[ main.py ]
it's just here to redirect '/' to '/index.htm'
the redirect-link could be changed by changing the link below
"""

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

import main_page
import unshort_url
import resview_url
import header_url

class HeadersURL(webapp.RequestHandler):
  def get(self):
    self.response.headers["Content-Type"] = "text/html"
    self.response.out.write(header_url.show_headers(self))
  def post(self):
    self.response.headers["Content-Type"] = "text/html"
    self.response.out.write(header_url.show_headers(self))

class ResViewURL(webapp.RequestHandler):
  def get(self):
    self.response.headers["Content-Type"] = "text/html"
    self.response.out.write(resview_url.show_body(self))
  def post(self):
    self.response.headers["Content-Type"] = "text/html"
    self.response.out.write(resview_url.show_body(self))

class UnShortenURL(webapp.RequestHandler):
  def get(self):
    self.response.headers["Content-Type"] = "text/html"
    self.response.out.write(unshort_url.url_trace(self))
  def post(self):
    self.response.headers["Content-Type"] = "text/html"
    self.response.out.write(unshort_url.url_trace(self))

class MainHandler(webapp.RequestHandler):
  def get(self):
    self.response.headers["Content-Type"] = "text/html"
    self.response.out.write(main_page.index(self))
  def post(self):
    self.response.headers["Content-Type"] = "text/html"
    self.response.out.write(main_page.index(self))

def main():
  application = webapp.WSGIApplication(
    [
          ('/', MainHandler),
          (r'/unshort_url(?:/\w+)*', UnShortenURL),
          (r'/resview_url(?:/\w+)*', ResViewURL),
          (r'/header_url(?:/\w+)*', HeadersURL)
        ], debug=True)
  util.run_wsgi_app(application)


if __name__ == '__main__':
  main()
