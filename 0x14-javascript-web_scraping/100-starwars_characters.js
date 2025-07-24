#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';

request((url + id), function (error, response, body){
	if (error){
		console.error(error);
		return;
	}
	JSON.parse(body).characters.forEach(function (character){
		request(character, function (error, response, body){
			if (error){
				console.error(error);
			};
			console.log(JSON.parse(body).name);
		});
	});
});
