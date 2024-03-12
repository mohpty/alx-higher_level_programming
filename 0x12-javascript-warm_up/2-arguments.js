#!/usr/bin/node
const size = process.argv.length;
if (size > 3) { console.log('Arguments found'); } else if (size > 2) { console.log('Argument found'); } else { console.log('No argument'); }
