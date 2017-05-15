'use-strict';
var candies = 10000;
var lollypops = 0;
var speed = 0;
const candiesContainer = document.querySelector('.candies');
const lollypopsContainer = document.querySelector('.lollypops');
const candiesTimeContainer = document.querySelector('.speed');
const createCandiesButton = document.querySelector('.create-candies');
const buyLollypopsButton = document.querySelector('.buy-lollypops');
const makeCandyRainButton = document.querySelector('.candy-machine');

function updateCandies() {
  candiesContainer.textContent = candies;
}

function makeCandy() {
  candies += 1;
  updateCandies();
  updateCandiesTime();
  setTimeout(makeCandy, speed);
}

function updateLollypops() {
  lollypopsContainer.textContent = '';
  for (let i = 0; i < lollypops; i++) {
    lollypopsContainer.textContent += "🍭";
  }

  if (lollypops === 10) {
    speed = 1000;
    setTimeout(makeCandy, speed);
  }
}

function updateCandiesTime() {
  candiesTimeContainer.textContent = (speed*0.1);
}

function createCandy() {
  candies += 1;
  updateCandies();
}

function buyLollypop() {
  if (candies > 100) {
    candies -= 100;
    lollypops += 1;
  } else {
    alert(':(');
  }

  updateCandies();
  updateLollypops();
}

function makeCandyRain() {
  speed = 1000/speed;
}

createCandiesButton.addEventListener('click', createCandy);
buyLollypopsButton.addEventListener('click', buyLollypop);
makeCandyRainButton.addEventListener('click', makeCandyRain);

updateCandies();
updateLollypops();
updateCandiesTime();
