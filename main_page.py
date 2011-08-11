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
	<link rel="stylesheet" href="/flat_web/index.css" type="text/css" />
	<script src="/flat_web/index.js" type="text/javascript"> </script>
  </head>
  <body>
    <table> 
      <tr>
      <td>
        <img src="/flat_web/logoY480px.jpg" alt="logo" /> 
	<div class="outline txtcenter" style="width:235px;">
  	  <div id="title">Web Houdini</div>
	  <div id="title_tag">The Web Magician...<br/>showing Online Tricks</div>
	  <div id="title_repo"><a href="https://github.com/abhishekkr/webhoudini">WebHoudini <i>Github</i> Repo</a></div>
	  <i>would keep adding more tricks...</i>
	</div>
      </td>
      <td>
        <div id="axnarea" style="text-align:center;">
	<span>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~</span>
	        <blockquote>
		<h3>Un-Shorten URL ~ know the final URL</h3>
		<form method="get" action="unshort_url" >
		  Short URL: <input type="text" name="url" id="url" />
		  <input type="button" value="Unshorten" onClick="fetch_me_result('unshort_url','/unshort_url?url='+document.getElementById('url').value);" /><br/>
		  <b id="unshort_url"></b>
		</form>
		</blockquote>
	<span>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~</span>
        </div>
      </td>
      </tr>
    </table>

	<div>
	  online: 
	  <a href="https://github.com/abhishekkr">abhishekkr@github</a>,
	  <a href="http://www.twitter.com/aBionic">abionic@twitter</a>
	</div>

  </body>
</html>"""
  return response
