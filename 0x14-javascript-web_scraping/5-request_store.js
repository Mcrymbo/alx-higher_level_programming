#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
request(url, (error, response, body) => {
  if (!error) {
    fs.writeFileSync(process.argv[3], body);
  }
});
