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
	<script src="/flat_web/magic.js" type="text/javascript"> </script>
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
		<h5>Un-Shorten URL ~ know the final URL</h5>
		<form method="get" action="unshort_url" >
		  Short URL: <input type="text" name="unshort_url_value" id="unshort_url_value" />
		  <input type="button" value="Unshorten" onClick="fetch_me_result('/unshort_url?url='+document.getElementById('unshort_url_value').value);show_magic();" /><br/>
		</form><br/>
		<h5>HTTP Header View ~ know the HTTP Response Headers for provided URL</h5>
		<form method="get" action="header_url" >
		  Any URL: <input type="text" name="header_url_value" id="header_url_value" />
		  <input type="button" value="Headers" onClick="fetch_me_result('/header_url?url='+document.getElementById('header_url_value').value);show_magic();" /><br/>
		</form><br/>
		<h5>HTTP Response ~ know the resource content to be served</h5>
		<form method="get" action="resview_url" >
		  Any URL: <input type="text" name="resview_url_value" id="resview_url_value" />
		  <input type="button" value="ResView" onClick="fetch_me_result('/resview_url?url='+document.getElementById('resview_url_value').value);show_magic();" /><br/>
		</form><br/>
		</blockquote>
	<span>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~</span>
        </div>
      </td>
<!-- Internet Defense League ~begin -->
      <td>
      <a href="http://internetdefenseleague.org"><img src="http://internetdefenseleague.org/images/badges/final/shield_badge.png" style='height:230px; width:160px;' alt="Member of The Internet Defense League" /></a>
      </td>
<!-- Internet Defense League ~end -->
      </tr>
    </table>

<div id="magical_blanket" style="display:none;"></div>
<div id="magical_result" style="display:none;">
  <a href="#" onclick="show_magic()">[X]Close</a>
</div>

	<div>
	  online: 
	  <a href="https://github.com/abhishekkr">abhishekkr@github</a>,
	  <a href="http://www.twitter.com/aBionic">abionic@twitter</a>
	</div>

<!-- Internet Defense League ~begin -->
<script type="text/javascript">
window._idl = {};
_idl.variant = "banner";
_idl.campaign = "idl_launch";
(function() {
var idl = document.createElement('script');
idl.type = 'text/javascript';
idl.async = true;
idl.src = ('https:' == document.location.protocol ? 'https://' : 'http://') + 'members.internetdefenseleague.org/include/?url=' + (_idl.url || '') + '&campaign=' + (_idl.campaign || '') + '&variant=' + (_idl.variant || 'banner');
document.getElementsByTagName('body')[0].appendChild(idl);
})();
</script>
<!-- Internet Defense League ~end -->

  </body>
</html>"""
  return response
