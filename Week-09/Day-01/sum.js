'use strict';

var object = {
    sum: function (list) {
        let sum = 0;
        list.forEach(function (num) {
            if (typeof num === 'number'){
                sum += num;
            }
        });
        return sum;
    }
};

console.log(object.sum([9,8,7]));

module.exports = object.sum;
