'use strict';

function sharpie (color, width){
  this.color = color;
  this.width = width;
  this.inkAmount = 100;
  this.use = function (){
    this.inkAmount -= this.width;
  }

}

var Sharpie1 = new sharpie ('blue', 25);
Sharpie1.use();
console.log('Blue sharpie has ' + Sharpie1.inkAmount + ' ink left.');

var Sharpie2 = new sharpie ('green', 90);
Sharpie2.use();
console.log('Green sharpie has ' + Sharpie2.inkAmount + ' ink left.');


var Sharpie3 = new sharpie ('Red', 33);
Sharpie3.use();
console.log('Red sharpie has ' + Sharpie3.inkAmount + ' ink left.');
