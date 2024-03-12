#!/usr/bin/node
let x = 0;
process.argv.forEach((val, idx, arr) => {
  if (idx >= 2) {
    console.log(val);
  }
  x += 1;
});

if (x <= 2) {
  console.log('No argument');
}
