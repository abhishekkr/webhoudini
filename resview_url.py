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
  _url = self.request.get('url')
  _format = self.request.get('f')
  try:
    result = urlfetch.fetch(url=_url)
    result_content = result.content.decode('utf-8').encode('ASCII', 'ignore')
    if _format == 'vanilla':
      html_for_others(self)
      return result_content
    elif _format == 'safe':
      html_for_others(self)
      return cgi.escape(str(result_content))

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

  if str(result_content)==None:
    result_content = "BLANK RESOURCE"

  response = """<html>
    <head>
      <title>Naked URL ~ all contents of resource served</title>
    </head>
    <body>
      <div class="main_pg" style="text-align:left;">
        <div>The resource served from requested URL <h5>""" + _url + """</h5> is
          <div>
          """ + cgi.escape(result_content) + """
          </div>
          <br/><br/>
          <h5>
            <a href="#" onclick="show_magic()" style="float:right;">[X]Close</a><br/>
          </h5>
        </div>
      </div>
    </body>
  </html>"""
  return response
