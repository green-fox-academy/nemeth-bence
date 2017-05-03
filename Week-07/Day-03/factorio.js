'use strict';
// - Create a function called `factorio`
//   that returns it's input's factorial

function factorio(num){
    if (num === 0){
        return 1; } else
      { return num * factorio( num ); }
}

console.log(factorio(4))


function factorio(num){
    var val = 1;
    for (var i = 2; i <= num; i++)
        val = val * i;
    return val;
}

console.log(factorio(4))
