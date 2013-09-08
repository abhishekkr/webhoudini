#!/usr/bin/env python
##
# http://www.twitter.com/aBionic ~ABK~
#
# unshort_url ~ to trace url
##

from google.appengine.api import urlfetch

def url_trace(self):
  try:
    result = urlfetch.fetch(url=self.request.get['url'])
  except:
    return """
    <html><head><title>WebHoudini is sleeping.....</title></head>
    <body>
      WebHoudini is sleeping as his servants have failed in fetching the resource from URL.....<br/>
      Please, check if the Domain &/or URL is correct and returning some response.<br/><br/>
      <b>$curl -L $URL</b><br/>
    </body></html>
    """
  if str(result.final_url)=="None":
    result.final_url = self.request.get['url']
  response = """<html>
    <head>
      <title>Unshorten-URL ~ URL Trace</title>
    </head>
    <body>
      <div class="main_pg" style="text-align:center;">
      """
  response = response + """
        <div>The requested URL <h5>""" + self.request.get['url'] + """</h5> has
  <h3><a href=\""""
  response = response + str(result.final_url)
  response = response + "\">"
  response = response + str(result.final_url)
  response = response + """</a></h3> as its final destination.
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
