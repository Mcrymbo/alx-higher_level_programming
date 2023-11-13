#!/usr/bin/node

const [, ,args] = process.argv

if (typeof args === 'undefined'){
	console.log("No arguments");
}
else {
	console.log(args);
}
