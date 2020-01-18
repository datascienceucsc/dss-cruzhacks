function hideAll(id_selector) {
  document.querySelectorAll(".display-box").forEach(b => {
    b.style.display = "none";
  });
  let displayBox = document.querySelector(id_selector);
  displayBox.style.display = "block";
}

document.querySelector("#nav-dashboard").addEventListener("click", () => {
    hideAll("#dashboard");
});

document.querySelector("#nav-shortcuts").addEventListener("click", () => {
    hideAll("#shortcuts");
});

document.querySelector("#nav-overview").addEventListener("click", () => {
  hideAll("#overview");
});
