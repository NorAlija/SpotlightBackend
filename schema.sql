CREATE TABLE Image (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT (datetime('now','utc')),
    filename VARCHAR(255) NOT NULL UNIQUE
);