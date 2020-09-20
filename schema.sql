CREATE TABLE users (id SERIAL PRIMARY KEY,
  username TEXT UNIQUE,
  password TEXT);
CREATE TABLE checkpoints (checkpoint_id SERIAL,
  name TEXT,
  category TEXT,
  description TEXT);
CREATE TABLE performances (performance_id SERIAL,
  data BYTEA,
  user_id SERIAL,
  checkpoint_id SERIAL,
  PRIMARY KEY(performance_id),
  CONSTRAINT fk_user FOREIGN KEY(user_id) REFERENCES users(user_id),
  CONSTRAINT fk_checkpoint FOREIGN KEY(checkpoint_id) REFERENCES checkpoints(checkpoint_id));
