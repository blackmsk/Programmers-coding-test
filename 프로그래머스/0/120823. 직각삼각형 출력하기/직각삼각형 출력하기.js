const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

function printTriangle(n) {
    // Iterate through each row from 1 to n
    for (let i = 1; i <= n; i++) {
        // Create a string with i '*' characters
        let row = '*'.repeat(i);
        // Print the row
        console.log(row);
    }
}

rl.on('line', function (line) {
    input = line.split(' ');
}).on('close', function () {
    printTriangle(input[0]);
});