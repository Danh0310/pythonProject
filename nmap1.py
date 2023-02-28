var scanner = function(ip) {
  var xhr = new XMLHttpRequest();
  xhr.open('GET', 'http://localhost:8000/scanner.py?ip=' + ip, true);
  xhr.onreadystatechange = function() {
    if (xhr.readyState == 4) {
      var data = JSON.parse(xhr.responseText);
      console.log(data);
    }
  }
  xhr.send();
}