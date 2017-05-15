'use strict';

function anagram(str1, str2){
  let word1 = str1.toString().toLowerCase().split('').sort().join();
  let word2 = str2.toString().toLowerCase().split('').sort().join();
  return word1 === word2;
}

module.exports = anagram;

console.log(anagram('Elvis', 'Lives'))
