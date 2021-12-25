document.addEventListener("DOMContentLoaded", function(event) {

  document.getElementById("loading").remove();

  var btnScrollTop = document.getElementById("btn-scroll-top");

  window.onscroll = function() {
    if (document.body.scrollTop > 100
        || document.documentElement.scrollTop > 100) {
      btnScrollTop.style.display = "block";
    } else {
      btnScrollTop.style.display = "none";
    }
  };

  btnScrollTop.onclick = function() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
  }

});
