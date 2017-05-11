'use strict';

var mybutton = document.querySelector(".this-one");
var clicked = 0;
mybutton.addEventListener('click', function(){
  clicked += 1;
  if (clicked == 3){
    setTimeout(function(){
      var text = document.createElement("p");
      text.textContent = '5 seconds ellapsed and clicked 3 times'
      document.body.appendChild(text);
    }, 5000);
  }
})
