#!/usr/bin/node
const number = Number(process.argv[2]);
let line;
if (isNaN(number)) {
  console.log('Missing size');
}
for (let i = 0; i < number; i++) {
  line = '';
  for (let j = 0; j < number; j++) {
    line += 'x';
  }
  console.log(line);
}
