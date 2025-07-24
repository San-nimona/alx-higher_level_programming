#!/usr/bin/node

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
const request = require('request');

request(url, function (error, response, body){
	if (error){
		console.error(error);
		return;
	}
	const characters = JSON.parse(body).characters;
	console.log(characters[0]);
	//console.log(body.length);
	//console.log(JSON.parse(body).characters);
	//for (let i = 0; i < body.length; i++){
	//characters.forEach(function (character){
	async function inOrder(){
		for (const character of characters){
	//for (let character in characters){
		//const url1 = characters[i];
			await request(character, function (error, response, body){
				const charName = JSON.parse(body).name;
				console.log(charName);
			});
		}
	}
	inOrder();
})
