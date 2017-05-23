'use strict';

// Create a constructor for creating Animals.
// it should take one parameter: what the animal says
// Every animal should have a method called say() that prints what the animal says

function Animals() {
}

Animals.prototype.say = function(say) {
 console.log(say);
}

var dog = new Animals();
dog.say('wouf');

var lepke = new Animals();
lepke.say('lep-lep');
