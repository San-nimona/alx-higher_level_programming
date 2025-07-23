#!/usr/bin/node

const request = require('request');
let films = 0;
const url = process.argv[2];
request (url, {json: true}, function (errror, response, body){
	let len = body.count;
	//let films = 0;
	for (let i = 1; i < len; i++){
		let url1 = url + `${i}/`;
		request (url1, {json: true}, function (error, response, body){
			const charArray = JSON.stringify(body.characters);
			const value = "https://swapi-api.alx-tools.com/api/people/18/";
			newArray = JSON.parse(charArray);
			newArray.forEach(function (character){
				if (character === value){
					films++;
				}
			})
			if (i === (len - 1)){
				console.log(films);
			}
		})
	}

})
