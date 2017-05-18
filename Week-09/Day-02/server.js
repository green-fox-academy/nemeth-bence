'use strict'

var express = require('express');
var app = express();

app.get('/', function(req, res){
  res.send('Ez itt a főoldal.');
});

app.listen(3000);
