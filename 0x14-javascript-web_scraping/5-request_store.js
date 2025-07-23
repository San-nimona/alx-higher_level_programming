#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const path = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  fs.writeFileSync(path, body, 'utf-8');
});
