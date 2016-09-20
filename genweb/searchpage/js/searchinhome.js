$(document).ready(function() {
  var path = window.location.pathname;
  path = path.split("/");
  path = path[path.length-1];
  if (path.length <= 4 && (path == 'ca' || path == 'es' || path == 'en')) {
    history.pushState(null , null, window.location.origin + window.location.pathname + "/@@search?portal_type%3Alist=Document");
  }
})
