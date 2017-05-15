'use strict';

var test = require('tape');
var anagram = require('./anagram.js');

test('Anagram', function (t){
    var word1 = 'Dictionary';
    var word2 = 'Indicatory';
    t.equal(anagram(word1, word2), true);
    t.end();
});

test('NotAnagram', function (t){
    var word1 = 'example';
    var word2 = 'fail';
    t.equal(anagram(word1, word2), false);
    t.end();
});
