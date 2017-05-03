'use strict';
// - Write a function called `sum` that sum all the numbers until the given parameter
// - The function should return the result


function sum(num){
  var out = 0;
  for (var i = 0; i <= num; i++)
      out += i;
      return out
}

console.log(sum(4))
