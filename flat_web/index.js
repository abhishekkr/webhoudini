

function loadXMLDoc(url,cfunc){
if (window.XMLHttpRequest)
  {// code for IE7+, Firefox, Chrome, Opera, Safari
  xmlhttp=new XMLHttpRequest();
  }
else
  {// code for IE6, IE5
  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }
xmlhttp.onreadystatechange=cfunc;
xmlhttp.open("GET",url,true);
xmlhttp.send();
}

function fetch_me_result(url){
   tag_id = "magical_result"
   document.getElementById(tag_id).innerHTML="<a href=\"#\" onclick=\"show_magic()\" style=\"float:right;\">[X]Close</a><br/> <h3>Loading...</h3>";
   loadXMLDoc(url,function(){
     if (xmlhttp.readyState==4 && xmlhttp.status==200){
       document.getElementById(tag_id).innerHTML="<a href=\"#\" onclick=\"show_magic()\" style=\"float:right;\">[X]Close</a><br/>" + xmlhttp.responseText;
    }
  });
}
