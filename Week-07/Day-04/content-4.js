/*<script>
    replace the list items' content with items from this list:
    ['apple', 'banana', 'cat', 'dog']
</script>*/

var listelements = document.querySelectorAll('li')
var list = ['apple', 'banana', 'cat', 'dog']

list.forEach(function(valami,akarmi) {
listelements[akarmi].textContent = valami;
});
