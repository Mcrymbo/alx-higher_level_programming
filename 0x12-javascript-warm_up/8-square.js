#!/usr/bin/node

const arg = process.argv[2];
const num = parseInt(arg);
let i;

if (!isNaN(num)){
	for (i = 0; i < num; i++){
		row = "";
		for (let j = 0; j < num; j++){
			row += "X";
		}
		console.log(row);
	}
}
else {
	console.log("Missing size");
}
