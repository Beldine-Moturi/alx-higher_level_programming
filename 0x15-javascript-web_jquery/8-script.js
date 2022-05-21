$(function() {
    $.get("https://swapi-api.hbtn.io/api/films/?format=json", function(data) {
	var movies = data.results;
	movies.forEach(movie => $('UL#list_movies').append(`<li>${movie.title}</li>`));
    });
});
