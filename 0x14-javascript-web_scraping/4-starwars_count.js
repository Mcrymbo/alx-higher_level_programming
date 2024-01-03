#!/usr/bin/node
const request = require('request');
let number = 0;

const url = process.argv[2];
request(url, (error, response, body) => {
  if (!error) {
    const data = JSON.parse(body);
    const result = data.results;
    for (let i = 0; i < result.length; i++) {
      const chars = result[i].characters;
      for (let j = 0; j < chars.length; j++) {
        if (chars[j].search('18') > 0) {
          number++;
        }
      }
    }
  }
  console.log(number);
});
