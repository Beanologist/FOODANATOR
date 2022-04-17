let text = "Hungry but don't know what to eat?";
let text2 = document.getElementById("about");
let len = text.length;
let index = 0;
function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}
console.log("far");
window.addEventListener("load", thing);
function thing() {
  text2.innerText = text.slice(0, index);
  index++;
}
let interval = setInterval(thing, 200);
