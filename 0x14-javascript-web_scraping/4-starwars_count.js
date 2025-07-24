#!/usr/bin/node

const request = require('request');
let films = 0;
let url;
try {
  url = process.argv[2];
  if (!url) throw new Error('No URL or episode ID provided.');
} catch (err) {
  console.error(err.message);
  process.exit(1);
}

request(url, function (error, response, body) {
  if (error) {
    console.error(error.message);
    return;
  }
  body = JSON.parse(body);
  const len = body.count;
  for (let i = 1; i < len; i++) {
    const url1 = url + `/${i}/`;
    request(url1, function (error, response, body) {
      if (error) {
        console.error(error.message);
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
