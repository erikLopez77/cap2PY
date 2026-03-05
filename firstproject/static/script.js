function myfunction(id) {
  var x = document.getElementById("detalle-" + id);
  if (x.style.display === "none")
    x.style.display = "block";
  else
    x.style.display = "none";
}