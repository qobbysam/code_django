var Chat = (function() {
  var _socket;

  function init(socket) {
    _socket = socket;

    $('form#message').submit(function() {
      var username = $.trim($('#uName').val());
      var message = $.trim($('#topleftcol').val());
      var codePython ='';
      var codeJava ='';
      
      if (!username.length) {
          alert("No name :(");}
       if (!message.length) {
        $('#topleftcol').focus();
      } else {
        _socket.send_json({username: username, message: message, codeJava:codeJava, codePython:codePython});
        $('#topleftcol').val('');
        $('#topleftcol').focus();
      }
      return false;
    });
 
  }

  return {
     init: init
  };

})();

SockJS.prototype.send_json = function(data) {
  this.send(JSON.stringify(data));
};

var initsock = function(callback) {
  sock = new SockJS('http://' + SOCK.host + ':' + SOCK.port + '/' + SOCK.channel )

  sock.onmessage = function(e) {
    console.log('message', e.data);
    var data = e.data;
    if (data.message && data.username) {
      var out = $('#out');
      
      $('<span>')
        .addClass('date')
        .text(data.onSending)
        .appendTo(out);
      $('<li>')
        .append($('<strong>').text( data.username + " :   "))
        .append($('<span>').text(data.message + "  ") )
        .appendTo(out);
      out.scrollTop(out.scrollTop() + 1000);
      // console.log (e.username);
    }

      if (e.codePython !== 'ap'){
        $('#mypy').val($('#mypy').val()+data.codePython);
      }
      if (e.codeJava !== 'bc'){
       
      $('#myjav').val(data.codeJava); 
      }
  };

  sock.onclose = function() {
    console.log('closed :(');
  };

  sock.onopen = function() {
    console.log('open');
    // sock.send(auth_json);

    if (sock.readyState !== SockJS.OPEN) {
      throw "Connection NOT open";
    }
    callback(sock);
  };

  sock.oncode =function(c){
    console.log('in comming code')
    var data = c.data;

    if (data.code){
      var out = $('out');
      $('<p>')
      .append($('<span>').text(data.code))
      .appendTo(out);
    }

  }

};


$(function() {
  initsock(function(socket) {
    Chat.init(socket);
  });
});
