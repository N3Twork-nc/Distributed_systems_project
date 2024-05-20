const express = require('express');
const app = express();
const path = require('path');

// Import fake data
const books = require('./fakeData');

// Serve static files from the 'public' directory
app.use(express.static(path.join(__dirname, 'public')));

// Redirect from root to /Home
app.get('/', (req, res) => {
  res.redirect('/Home');
});

// Serve index.html at /Home
app.get('/Home', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Serve the JavaScript file from the public/js/main directory
app.get('/js/main/main.js', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'js', 'main', 'main.js'));
});

// API endpoint to get books
app.get('/fakeData', (req, res) => {
  console.log("Books data:", books);
  res.json(books);
});

const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
