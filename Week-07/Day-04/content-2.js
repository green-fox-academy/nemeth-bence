/*You can work in the html or in a separate js file. Like:
  <script>
    fill every paragraph with the last one's content.
  </script>*/

var paragraphs = document.querySelectorAll('p');
  paragraphs.forEach(function(i) {
       i.innerHTML = paragraphs[3].innerHTML
     })

console.log(paragraphs);
