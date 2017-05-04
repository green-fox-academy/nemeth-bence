/*<script>
Does the third p have a cat class?
If so, alert 'YEAH CAT!'
If the fourth p has a 'dolphin' class, replace apple's content with 'pear'
If the first p has an 'apple' class, replace cat's content with 'dog'
Make apple red
Make balloon less balloon-like
</script>*/

var p = document.querySelectorAll('p');
if (p[2].classList.contains('cat')) {
   alert('YEAH CAT!');
    }

if (p[3].classList.contains('dolphin')) {
    p[0].textContent = 'pear';
    }
