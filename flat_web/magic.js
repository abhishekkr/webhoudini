function toggle_display(div_id) {
  var div_by_id = document.getElementById(div_id);
  if(div_by_id.style.display=='none'){
    div_by_id.style.display = 'block';
  }
  else{
    div_by_id.style.display = 'none';
  }
}

function get_view_width(){
  if(typeof window.innerWidth != 'undefined'){
    view_width = window.innerWidth;
  }else{
    view_width = document.documentElement.clientWidth;
  }

  if( (view_width > document.body.parentNode.scrollWidth) && (view_width > document.body.parentNode.clientWidth) ){
    window_width = view_width;
  }else{
    if(document.body.parentNode.clientWidth > document.body.parentNode.scrollWidth){
      window_width = document.body.parentNode.clientWidth;
    }else{
      window_width = document.body.parentNode.scrollWidth;
    }
  }

  return window_width;
}

function get_view_height(){
  if(typeof window.innerHeight != 'undefined'){
    view_height = window.innerHeight;
  }else{
    view_height = document.documentElement.clientHeight;
  }

  if( (view_height > document.body.parentNode.scrollHeight) && (view_height > document.body.parentNode.clientHeight) ){
    window_height = view_height;
  }else{
    if (document.body.parentNode.clientHeight > document.body.parentNode.scrollHeight) {
      window_height = document.body.parentNode.clientHeight;
    }else{
      window_height = document.body.parentNode.scrollHeight;
    }
  }

  return window_height;
}

function locate_result(magical_result) {
  var window_height = get_view_height();
  var window_width = get_view_width();
  view_left = (window_width - ((window_width/100)*90))/2 ; //width is 90% of window
  view_top = (window_height - ((window_height/100)*75))/2 ;//height is 75% of window

  var result = document.getElementById(magical_result);
  result.style.left = view_left + 'px';
  result.style.top = view_top + 'px';
}

function show_magic() {
  locate_result('magical_result');
  toggle_display('magical_blanket');
  toggle_display('magical_result');		
}
