/*<script>
    Write the image's url to the console.
    Replace the image with a picture of yourself.
    Make the link point to the Green Fox Academy website.
    Disable the second button.
    Replace its text with 'Don't click me!'.
  </script>*/

var bestEver = document.querySelector('img');
console.log('image URL:', bestEver.getAttribute('src'));
bestEver.setAttribute('src', 'file:///C:/Users/Bence/Desktop/Zodiac-10-1.jpg');

var bestEva = document.querySelector('a');
console.log('image URL:', bestEva.getAttribute('href'));
bestEva.setAttribute('href', 'https://www.greenfoxacademy.com/');

console.log(document.querySelector('.this-one'));
  document.querySelector('.this-one').disabled = true;

document.querySelector('.this-one').innerText = 'Don\'t click me!';
