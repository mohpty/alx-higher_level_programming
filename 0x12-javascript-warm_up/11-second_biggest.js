#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
  process.exit();
}
const numbers = [];
for (let i = 2; i < process.argv.length; i++) {
  numbers.push(Number(process.argv[i]));
}
numbers.sort();
console.log(numbers[numbers.length - 2]);
