const path = require('path');
const express = require('express');
const cors = require('cors');
const app = express();

app.use(express.static(path.join(__dirname, '../dist')));
app.use(cors());

const PORT = 8080;

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, '../dist', 'index.html'));
});

app.listen(PORT, () => {
    console.log(`App listening to ${PORT}...`);
});

