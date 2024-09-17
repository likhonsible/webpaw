<?php
header('Content-Type: application/json');

// Enable error reporting
ini_set('display_errors', 0); // Don't display errors in the browser
ini_set('log_errors', 1); // Enable error logging
ini_set('error_log', 'backend/logs/error.log'); // Specify the log file

try {
    $db = new SQLite3('pizza_game.db');

    // Fetch leaderboard
    $result = $db->query('SELECT username, earnings FROM users ORDER BY earnings DESC LIMIT 10');

    $leaderboard = [];
    while ($row = $result->fetchArray(SQLITE3_ASSOC)) {
        $leaderboard[] = $row;
    }

    echo json_encode($leaderboard);
} catch (Exception $e) {
    error_log('Database error: ' . $e->getMessage());
    echo json_encode(['error' => 'Database error occurred']);
}
?>
