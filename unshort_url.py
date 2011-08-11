#!/usr/bin/env python
##
# http://www.twitter.com/aBionic ~ABK~
#
# unshort_url ~ to trace url
##

from google.appengine.api import urlfetch

def url_trace(self):
  result = urlfetch.fetch(url=self.request.queryvars['url'])
  if str(result.final_url)=="None":
    result.final_url = self.request.queryvars['url']
  response = """<html>
    <head>
      <title>Unshorten-URL ~ URL Trace</title>
    </head>
    <body>
      <div class="main_pg" style="text-align:center;">
      """
  response = response + """
        <div>The requested URL <h5>""" + self.request.queryvars['url'] + """</h5> has 
  <h3><a href=\""""
  response = response + str(result.final_url)
  response = response + "\">"
  response = response + str(result.final_url)
  response = response + """</a></h3> as its final destination.
  """
  response = response + """
      <br/><br/>
      <h5>
        <a href="/">HOMEPAGE</a>
      </h5>
      </div>
    </body>
  </html>"""
  return response
