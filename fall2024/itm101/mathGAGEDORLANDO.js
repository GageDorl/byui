const command = process.argv[2];
const num1 = parseFloat(process.argv[3]);
const num2 = parseFloat(process.argv[4]);

let result;

switch (command) {
  case 'add':
    result = num1 + num2;
    break;
  case 'subtract':
    result = num1 - num2;
    break;
  case 'multiply':
    result = num1 * num2;
    break;
  case 'divide':
    result = num1 / num2;
    break;
  case 'exponent':
    result = num1 ** num2;
    break;
  default:
    console.log('Invalid command. Please use add, subtract, multiply, divide, or exponent.');
    process.exit(1);
}

console.log(`The result of ${command}ing ${num1} and ${num2} is ${result}.`);