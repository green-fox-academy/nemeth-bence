'use strict';

var mybutton = document.querySelector(".this-one");
mybutton.onclick = text

function press (){
  var newDiv = document.createElement("p");
  newDiv.textContent = '2 seconds ellapsed'
  document.body.appendChild(newDiv);
};

function text(){
  setTimeout(press, 2000)
}
