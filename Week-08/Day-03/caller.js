'use strict';

// Implement the selectLastEvenNumber function that takes an array and callback,
// it should call the callback immediately with the last even number on the array


function printNumber(num) {
  console.log(num);
}

function selectLastEvenNumber(x, callback){
  let lastEven = 0;
  x.forEach(function(n){
  if (n % 2 == 0){
    lastEven = n;
  }
 });
  callback(lastEven);
}

 selectLastEvenNumber([2, 5, 7, 8, 9, 11], printNumber); // should print 8
