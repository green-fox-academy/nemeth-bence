'use strict';

var http = require('http');
var server = http.createServer(handleRequest);
function handleRequest(request, response){
  console.log(request);
  response.end('Jippykayjei, mothafuckas!');
}
server.listen(3000)
