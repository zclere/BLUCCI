var genre = document.querySelector(".genre");

function filterFunction() {

	if (genre.classList.contains('hidden')) {
		genre.classList.remove('hidden');
		window.scrollTo(0, 0);
	} else {
		genre.classList.add('hidden');
	}
}