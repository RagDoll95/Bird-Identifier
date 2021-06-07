DROP TABLE IF EXISTS bird;
DROP TABLE IF EXISTS post;

CREATE TABLE bird (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  imagepath TEXT UNIQUE NOT NULL,
  isbird INTEGER,
  species TEXT
);