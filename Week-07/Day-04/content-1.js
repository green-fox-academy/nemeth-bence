/* <script>
    1. Alert the content of the heading.
    2. Write the content of the first paragraph to the console.
    3. Alert the content of the second paragraph.
    4. Replace the heading's content with 'New content'.
    5. Replace the last paragraph's content with the first paragraph's content.
  </script> */

var heading = document.querySelector('h1');
//alert(heading.textContent);

var para1 = document.querySelector('p');
console.log(para1.textContent);

var para2 = document.querySelector('.other');
//alert(para2.textContent);

heading.innerHTML = 'New content';

var lastPara = document.querySelector('.result');
lastPara.innerHTML = para1.innerHTML;
