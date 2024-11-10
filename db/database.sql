CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NOT NULL
);

INSERT INTO items (name, description) VALUES ('Item1', 'Description 1');
INSERT INTO items (name, description) VALUES ('Item2', 'Description 2');
