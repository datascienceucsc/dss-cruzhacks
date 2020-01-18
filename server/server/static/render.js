document.addEventListener("DOMContentLoaded", function() {
  document.querySelectorAll(".display-box").forEach(b => {
    b.style.display = "none";
  });
  let displayBox = document.querySelector("#home");
  displayBox.style.display = "block";
});

function hideAll(id_selector) {
  document.querySelectorAll(".display-box").forEach(b => {
    b.style.display = "none";
  });
  document.querySelectorAll(".nav-link").forEach(navItem => {
    navItem.classList.remove("active");
  });
  let displayBox = document.querySelector(id_selector);
  displayBox.style.display = "block";
}

document.querySelector("#nav-home").addEventListener("click", () => {
  hideAll("#home");
  document.querySelector("#nav-home").classList.add("active");
});

document.querySelector("#nav-singleCandidate").addEventListener("click", () => {
  hideAll("#singleCandidate");
  document.querySelector("#nav-singleCandidate").classList.add("active");
});

document.querySelector("#nav-duoCandidate").addEventListener("click", () => {
  hideAll("#duoCandidate");
  document.querySelector("#nav-duoCandidate").classList.add("active");
});
