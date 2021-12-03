/*
 * Called to set up select options on the main page
 * for the the required languages .
 */
window.onload = function () {
	v = document.getElementById('langs')
	langs = JSON.parse(v.getAttribute('content'))
	console.log(langs)
	x = document.getElementsByName('lang')[0]
	for (var u in langs) {
		opt = document.createElement('option')
		opt.value = u
		opt.innerHTML = langs[u]['display']
		x.appendChild(opt)
	}
}