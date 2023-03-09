window.onscroll = function() {
	myFunction();
	mobileNav(x);
};

var navbar = document.getElementById("navbar");
var sticky = navbar.offsetTop;

function myFunction() {
  if (window.scrollY >= sticky) {
    navbar.classList.add("sticky");
  } else {
    navbar.classList.remove("sticky");
  }
}


function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
}


var x = window.matchMedia("(max-width: 1026px)")
var mobilenavbar = document.getElementById("m_navbar");
var pinned = mobilenavbar.offsetTop;

function mobileNav(x) {
  if (x.matches) {

  	if (window.scrollY >= pinned) {
  		mobilenavbar.classList.add("pinned");
  	} else {
  		mobilenavbar.classList.remove("pinned");
  	}

  } else {
  	mobilenavbar.classList.remove("pinned");
  }

}

