#!/usr/bin/env python
##
# http://www.twitter.com/aBionic ~ABK~
#
# unshort_url ~ to trace url
##

import cgi

from google.appengine.api import urlfetch

def show_body(self):
  result = urlfetch.fetch(url=self.request.queryvars['url'])
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
        <div>The resource served from requested URL <h5>""" + self.request.queryvars['url'] + """</h5> is
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
