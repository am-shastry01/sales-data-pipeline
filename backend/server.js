const express = require("express");
const { Pool } = require("pg");
const cors = require("cors");

const app = express();
app.use(cors());

const pool = new Pool({
  user: "postgres",
  host: "localhost",
  database: "sales_pipeline",
  password: "Aryan930054",
  port: 5432,
});

app.get("/revenue", async (req, res) => {
  try {
    const result = await pool.query("SELECT * FROM product_revenue");
    res.json(result.rows);
  } catch (err) {
    console.error(err);
    res.status(500).send("Server Error");
  }
});

app.listen(5000, () => {
  console.log("Server running on port 5000");
});