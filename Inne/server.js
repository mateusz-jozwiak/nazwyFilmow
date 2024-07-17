const express = require('express');
const Redis = require('ioredis');
const cors = require('cors');

const app = express();
const port = 3000;

// Połączenie z Redis
const redis = new Redis({
  port: 2345,
  host: '65.109.228.144',
  password: 'GIQkLFR0tRvnoT3wrJVKs97DffsKq92gSJwt1qwPx9YPh6FBzsT8Y7R2yv1ilo4y',
  db: 1,
});

app.use(cors());

app.get('/data', async (req, res) => {
  try {
    const keys = await redis.keys('*');
    const data = [];

    for (const key of keys) {
      const item = await redis.hgetall(key);
      data.push(item);
    }

    res.json(data);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
