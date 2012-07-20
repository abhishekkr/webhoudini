#!/usr/bin/env python
##
# http://www.twitter.com/aBionic ~ABK~
#
# header_url ~ to see headers for resource
##

import cgi

from google.appengine.api import urlfetch

def show_headers(self):
  try:
    result = urlfetch.fetch(url=self.request.queryvars['url'])
  except:
    return """
    <html><head><title>WebHoudini is sleeping.....</title></head>
    <body>
      WebHoudini is sleeping as his servants have failed in fetching the resource from URL.....<br/>
      Please, check if the Domain &/or URL is correct and returning some response.<br/><br/>
      <b>$curl -L $URL</b><br/>
    </body></html>
    """
  result_headers = "<table>"
  if str(result.headers)==None:
    result_headers += "<tr><td>Weird ~ it received no headers</td></tr>"
  else:
    for key,value in result.headers.iteritems():
      result_headers += "<tr><td>" + cgi.escape(str(key)) + "</td><td>" + cgi.escape(str(value)) + "</td></tr>"
  result_headers += "</table>"
  response = """<html>
    <head>
      <title>Naked URL ~ all contents of resource served</title>
    </head>
    <body>
      <div class="main_pg" style="text-align:left;">
      """
  response = response + """
        <div>The HTTP Headers from requested URL <h5>""" + self.request.queryvars['url'] + """</h5> are<br/>
  <div>"""
  response = response + result_headers
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
