/*<script>
  fill output1 with the first paragraph's content, text only.
  fill output2 with the first paragraph's content keeping the cat strong.
</script>*/

var output1 = document.querySelector('.output1');
var p1 = document.querySelector('body > p');
    output1.textContent = p1.textContent;

var output2 = document.querySelector('.output2');
output2.innerHTML = p1.innerHTML;
