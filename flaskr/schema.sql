DROP TABLE IF EXISTS image;
DROP TABLE IF EXISTS post;

CREATE TABLE Image (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  imagepath TEXT UNIQUE NOT NULL,
  isbird INTEGER
);

