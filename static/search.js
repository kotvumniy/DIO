let searchTerm = document.getElementById("searchInput")

let searchButton = document.getElementById("searchButton")

searchButton.addEventListener("click", () => {

window.location.href = "/search/" + searchTerm.value

})


var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
  return new bootstrap.Popover(popoverTriggerEl)
})