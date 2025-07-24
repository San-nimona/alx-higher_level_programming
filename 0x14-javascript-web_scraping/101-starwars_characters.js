#!/usr/bin/node

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
const request = require('request');

request(url, function (error, response, body) {
  if (error) {
    console.error(error.message);
    return;
  }
  const characters = JSON.parse(body).characters;
  const charName = (index) => {
    if (index >= characters.length) return;
    request(characters[index], function (error, response, body) {
      if (error) {
        console.error(error.message);
      }
      const allNames = JSON.parse(body).name;
      console.log(allNames);
      charName(index + 1);
    });
  };
  charName(0);
});
