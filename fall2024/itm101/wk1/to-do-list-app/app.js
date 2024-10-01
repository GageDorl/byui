const express = require('express');
const bodyParser = require('body-parser');
const app = express();

app.use(bodyParser.urlencoded({ extended: true }));
app.set('view engine', 'ejs');

// Serve static files (CSS)
app.use(express.static("public"));

let tasks = [];

app.get('/', (req, res) => {
  res.render('index', { tasks: tasks });
});

app.post('/addtask', (req, res) => {
  let newTask = req.body.newtask;
  tasks.push(newTask);
  res.redirect('/');
});

app.post('/deletetask', (req, res) => {
  let index = req.body.taskIndex;
  tasks.splice(index, 1);
  res.redirect('/');
});

app.listen(3000, () => {
  console.log('Server is running on http://localhost:3000');
});
