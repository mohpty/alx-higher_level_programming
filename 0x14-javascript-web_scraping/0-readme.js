#!/usr/bin/node
// A script that reads the content of a file and prints it

const file = process.argv[2];
const fs = require('fs');
fs.readFile(file, 'utf8', (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
