includeDiv = document.getElementById("includeDiv");
images = document.getElementsByClassName("images");
let includeP = document.getElementById("includeP");
let excludeP = document.getElementById("excludeP");
let excludeText = "";
let includeButton = "";
let excludeArray = [];
let index = 0;
let container = document.getElementById("container");
let textContainer = document.getElementById("textContainer");
let recipie = document.getElementById("recipieContainer");

for (let i = 0; i < images.length; i++) {
  document.getElementById(String(i)).addEventListener("click", showInfo);
}

function showInfo(el) {
  console.log(this);
  textContainer.innerText = this.alt;
  if (this.getAttribute("name") == " "){
    recipie.innerText = "Sorry there is no recipie available at this time"
 }
  else{
    recipie.innerText = this.getAttribute("name");
  }
}
function include(el) {
  for (let i = 0; i < 26; i++) {
    if (includeDiv.children[i] != el) {
      includeDiv.children[i].classList.remove("include");
    }
  }
  includeButton = el.innerText;
  console.log(includeButton);
  el.classList.toggle("include");
}

function submitMeal() {
  passToFlask();
  document.getElementById("theForm").submit();
}
function exclude(el) {
  let notPopped = true;
  for (let i = 0; i < excludeArray.length; i++) {
    if (excludeArray[i] == el.innerText) {
      index = i;
      notPopped = false;
    }
  }
  if (notPopped) {
    excludeArray.push(el.innerText);
  } else {
    excludeArray.splice(index, 1);
  }
  el.classList.toggle("exclude");
  console.log(excludeArray);
}
function passToFlask() {
  includeP.value = includeButton;

  for (let i = 0; i < excludeArray.length - 1; i++) {
    excludeText += excludeArray[i] + ",";
  }
  excludeText += excludeArray[excludeArray.length - 1];
  excludeP.value = excludeText;
}
