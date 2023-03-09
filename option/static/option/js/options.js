function openTab(evt, cityName) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(cityName).style.display = "block";
  evt.currentTarget.className += " active";
}

document.getElementById("defaultOpen").click();



$(function() {
  $('.rightbase').hover(function() {
    $('.centerbase').css('transform', 'scaleX(0.5)');
  }, function() {
    // on mouseout, reset the background colour
    $('.centerbase').css('transform', 'scaleX(1)');
  });
});