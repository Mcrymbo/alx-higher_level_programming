#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  if (!error) {
    const result = {};
    const data = JSON.parse(body);
    for (let i = 0; i < data.length; i++) {
      if (data[i].completed === true) {
        if (result[data[i].userId] === undefined) {
          result[data[i].userId] = 0;
        }
        result[data[i].userId]++;
      }
    }
    console.log(result);
  }
});
