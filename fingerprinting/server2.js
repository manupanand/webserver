const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = 8080;

// Middleware to parse JSON data
app.use(bodyParser.json());

// Serve the tracking HTML page
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

// Endpoint to receive tracking data
app.post('/track', (req, res) => {
    const data = req.body;
    const ip = req.headers['x-forwarded-for'] || req.socket.remoteAddress;
    data.ip = ip;
    console.log('Received tracking data:', data);
    fs.appendFile('tracking_data.log', JSON.stringify(data) + '\n', (err) => {
        if (err) {
            console.error('Error writing to log file', err);
        }
    });
    res.sendStatus(200);
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});