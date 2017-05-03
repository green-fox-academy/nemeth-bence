'use strict';
// - Create (dynamically*) a two dimensional list
//   with the following matrix**. Use a loop!
//
//   0 0 0 1
//   0 0 1 0
//   0 1 0 0
//   1 0 0 0
//
// - Print this two dimensional list to the console
//
// * size should depend on a variable
// ** Relax, a matrix is just like an array

function matrix(size){
    var column = [];
   for (var x = 0; x <= size; x++){
     for (var y = 0; y <= size; y++)
/*        column = [0] * size;
        column[i] = 1;*/
        console.log(column);
    }
    return
}

matrix(5)
matrix(7)
