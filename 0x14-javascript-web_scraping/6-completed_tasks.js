#!/usr/bin/node

const request = require('request');

const url = 'https://jsonplaceholder.typicode.com/todos';

request(url, function (error, response, body) {
  const completed = {};
  if (error) {
    console.error(error);
    return;
  }
  JSON.parse(body).forEach(function (task) {
    if (task.completed) {
      if (completed[task.userId]) {
        completed[task.userId]++;
      } else {
        completed[task.userId] = 1;
      }
    }
  });
  console.log(completed);
});
