function calculate() {
    const command = document.getElementById('command').value;
    const num1 = parseFloat(document.getElementById('num1').value);
    const num2 = parseFloat(document.getElementById('num2').value);
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
            result = 'Invalid operation';
    }

    document.getElementById('result').innerText = `The result of ${command}ing ${num1} and ${num2} is ${result}.`;
}