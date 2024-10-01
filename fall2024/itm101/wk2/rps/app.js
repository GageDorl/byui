const express = require('express');
const path = require('path');
const app = express();
const port = 3000;

// Serve static files (for the frontend)
app.use(express.static('public'));

// Helper function to determine winner
const getWinner = (playerChoice, computerChoice) => {
    if (playerChoice === computerChoice) return 'It\'s a tie!';
    if (
        (playerChoice === '🪨' && computerChoice === '✂️') ||
        (playerChoice === '📄' && computerChoice === '🪨') ||
        (playerChoice === '✂️' && computerChoice === '📄')
    ) {
        return 'You did fine, I guess (you won)';
    }
    return 'Why\'d you even pick that?! (you lose)';
};

// Route for playing the game
app.get('/play', (req, res) => {
    const choices = ['🪨', '📄', '✂️'];
    const playerChoice = req.query.choice;
    const computerChoice = choices[Math.floor(Math.random() * choices.length)];
    const result = getWinner(playerChoice, computerChoice);

    res.json({
        playerChoice,
        computerChoice,
        result
    });
});

// Start the server
app.listen(port, () => {
    console.log(`Rock Paper Scissors app listening at http://localhost:${port}`);
});
