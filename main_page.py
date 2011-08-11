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
	<a href="https://github.com/abhishekkr/webhoudini">WebHoudini Project Repo @Github</a>
	<h3>The Web Magician showing Online Tricks</h3>
	<h5 stylw="float:bottom; margin-bottom:5px;">
		<i>will be adding more...</i><br/><br/>

             <div class="main_pg" style="text-align:center;">
	        <blockquote>
		<h3>Un-Shorten URL ~ know the final URL</h3>
		<form method="get" action="unshort_url" >
		  URL: <input type="text" name="url" id="url" />
		  <input type="submit" value="Unshorten" />
		</form>
		</blockquote>
             </div>
	</h5>
	online: 
	<a href="https://github.com/abhishekkr">abhishekkr@github</a>,
	<a href="http://www.twitter.com/aBionic">abionic@twitter</a>
  </body>
</html>"""
  return response
