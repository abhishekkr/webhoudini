#!/usr/bin/env python
##
# http://www.twitter.com/aBionic ~ABK~
#
# unshort_url ~ to trace url
##

import cgi

from google.appengine.api import urlfetch


def html_for_others(self):
  """
  Just sets your HTTP Headers so other WebOrigins can use content
  w/o XMLHttpRequest errors.
  """
  self.response.headers["Content-Type"] = "text/plain"
  self.response.headers["Access-Control-Allow-Headers"] = "*"
  self.response.headers["Access-Control-Allow-Origin"] = "*"
  self.response.headers["Access-Control-Allow-Methods"] = "*"


def show_body(self):
  """
  Responsible for fetching the 'url' body from Web and pass it on.
  """
  self.response.headers["Content-Type"] = "text/html"

  try:
    result = urlfetch.fetch(url=self.request.get('url'))
    if self.request.get('f') == 'vanilla':
      html_for_others(self)
      return result.content
    elif self.request.get('f') == 'safe':
      html_for_others(self)
      return cgi.escape(str(result.content))

  except Exception as err:
    return err
    """
    <html><head><title>WebHoudini is sleeping.....</title></head>
    <body>
      WebHoudini is sleeping as his servants have failed in fetching the resource from URL.....<br/>
      Please, check if the Domain &/or URL is correct and returning some response.<br/><br/>
      <b>$curl -L $URL</b><br/>
    </body></html>
    """

  if str(result.content)==None:
    result.content = "BLANK RESOURCE"
  response = """<html>
    <head>
      <title>Naked URL ~ all contents of resource served</title>
    </head>
    <body>
      <div class="main_pg" style="text-align:left;">
      """
  response = response + """
        <div>The resource served from requested URL <h5>""" + self.request.get['url'] + """</h5> is
  <div>"""
  response = response + cgi.escape(str(result.content))
  response = response + """</div>
  """
  response = response + """
      <br/><br/>
      <h5>
      <a href="#" onclick="show_magic()" style="float:right;">[X]Close</a><br/>
      </h5>
      </div>
    </body>
  </html>"""
  return response
