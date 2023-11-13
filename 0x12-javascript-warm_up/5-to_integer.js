#!/usr/bin/node
 
const args = process.argv[2];
const number = parseInt(args);

if (!isNaN(number)){
	console.log(`My number: ${number}`);
}
else {
	console.log("Not a number");
}
