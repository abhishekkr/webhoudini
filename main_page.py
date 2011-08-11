#!/usr/bin/env python
##
# http://www.twitter.com/aBionic ~ABK~
#
# unshort_url ~ to trace url
##

def index(self):
  response = """<html>
  <head>
  	<title>Web Houdini</title>
  </head>
  <body>
  	<h1>Web Houdini</h1>
	<a href="https://github.com/abhishekkr/webhoudini">@github</a>
	<h3>The Web Magician showing Online Tricks</h3>
	<h5 stylw="float:bottom; margin-bottom:5px;">
		<i>will be adding more...</i><br/><br/>

             <div class="main_pg" style="text-align:center;">
		<form method="get" action="unshort_url" >
		  URL: <input type="text" name="url" id="url" />
		  <input type="submit" value="Unshorten" />
		</form>
             </div>
	</h5>
	<a href="https://github.com/abhishekkr">@github</a>
	<a href="http://www.twitter.com/aBionic">@twitter</a>
  </body>
</html>"""
  return response
