const express = require('express');
const app = express();
const path = require('path');
const fs = require('fs');

// Serve static files from the 'public' directory
app.use(express.static(path.join(__dirname, 'public')));

// Redirect from root to /Home
app.get('/', (req, res) => {
  res.redirect('/Home');
});

// Serve test.html at /Home
app.get('/Home', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});


const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
