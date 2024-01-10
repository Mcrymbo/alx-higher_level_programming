const url = 'https://swapi-api.alx-tools.com/api/films/?format=json'
$.get(url, function (data) {
	const res = data.results;
	for (let i = 0; i < res.length; i++) {
		$('UL#list_movies').append('<li>' + res[i].title + '</li>');
	}
});
