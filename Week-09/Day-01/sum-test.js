'use strict';

var test = require('tape');
var sum = require('./sum.js');

test('empty', function (t){
    let list = [];
    let expected = 0;
    t.equal(sum(list), expected);
    t.end();
});

test('one', function (t){
    let list = [4];
    let expected = 4;
    t.equal(sum(list), expected);
    t.end();
});

test('multiple', function (t){
    let list = [1,3,5,7];
    let expected = 16;
    t.equal(sum(list), expected);
    t.end();
});

test('null', function (t){
    let list = [null, 7];
    let expected = 7;
    t.equal(sum(list), expected);
    t.end();
});

test('str', function (t){
    let list = [3, 'gatya', 7];
    let expected = 10;
    t.equal(sum(list), expected);
    t.end();
});
