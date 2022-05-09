#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const todos = {};
    const tasks = JSON.parse(body);
    for (const task of tasks) {
      if (task.completed === true) {
        if (todos[task.userId]) {
          todos[task.userId] += 1;
        } else {
          todos[task.userId] = 1;
        }
      }
    }
    console.log(todos);
  } else {
    console.log('Error code: $(response.statusCode)');
  }
});
