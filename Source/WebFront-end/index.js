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

// Serve the JavaScript file from the public/js directory
app.get('/js/dataFetcher.js', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'js', 'dataFetcher.js'));
});

// API endpoint to get data from Cassandra
app.get('/data', (req, res) => {
  const dataFilePath = path.join(__dirname, '..', '..', 'Source', 'Cassanndra', 'data.json');
  
  fs.readFile(dataFilePath, 'utf8', (err, data) => {
    if (err) {
      console.error('Error reading data file:', err);
      return res.status(500).send('Internal Server Error');
    }
    res.json(JSON.parse(data));
  });
});


const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
