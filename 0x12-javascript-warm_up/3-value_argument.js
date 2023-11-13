#!/usr/bin/node

const [, , args] = process.argv;

if (typeof args === 'undefined') {
  console.log('No argument');
} else {
  console.log(args);
}
