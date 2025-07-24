#!/usr/bin/node

const request = require('request');
let films = 0;
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  body = JSON.parse(body);
  const len = body.count;
  for (let i = 1; i < len; i++) {
    const url1 = url + `${i}/`;
    request(url1, function (error, response, body) {
      if (error) {
        console.error(error);
        return;
      }
      const charArray = JSON.parse(body).characters;
      const value = 'https://swapi-api.alx-tools.com/api/people/18/';
      charArray.forEach(function (character) {
        if (character === value) {
          films++;
        }
      });
      if (i === (len - 1)) {
        console.log(films);
      }
    });
  }
});
