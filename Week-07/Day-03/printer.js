'use strict';
// - Create a function called `printer`
//   which logs to the console the input parameters
//   (can have multiple number of arguments)

function inter(str){

  console.log(str);

}

inter('cumi')

function printer() {
    var str = '';
    for (var barmi in arguments) {
        str += arguments[barmi] + ',';
    }
    return str
}
console.log(printer(5,6,7,8,true,'string'));
