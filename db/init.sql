-- db/init.sql : runs ONLY when the database volume is empty (the first start)
CREATE TABLE IF NOT EXISTS notes (
  id         serial PRIMARY KEY,
  body       text NOT NULL,
  created_at timestamptz NOT NULL DEFAULT now()
);
INSERT INTO notes (body) VALUES ('first note, created by init.sql');
