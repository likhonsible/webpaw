<?php
// SQLite database file
$db_file = __DIR__ . '/pizza_game.db';

// Create (connect to) SQLite database in file
$conn = new SQLite3($db_file);

// Create the 'users' table if it doesn't exist
$conn->exec("CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id TEXT NOT NULL,
    username TEXT,
    earnings INTEGER DEFAULT 0
)");

if (!$conn) {
    die("Connection failed: " . $conn->lastErrorMsg());
}
?>
