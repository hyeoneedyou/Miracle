const showListBtn = document.querySelector(".nav_showListBtn"),
  sublist = document.querySelector(".sublist"),
  plusBtn = document.querySelector(".nav_plusBtn"),
  plusList = document.querySelector(".plusList");

showListBtn.addEventListener("click", () => {
  showListBtn.classList.toggle("clicked");
  sublist.classList.toggle("clicked");
});

plusBtn.addEventListener("click", () => {
  plusBtn.classList.toggle("clicked");
  plusList.classList.toggle("clicked");
});
