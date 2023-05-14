-- Create a table to store user login information
CREATE TABLE users (
  id INT PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL
);

-- Create a table to store image metadata
CREATE TABLE images (
  id INT PRIMARY KEY AUTO_INCREMENT,
  user_id INT NOT NULL,
  filename VARCHAR(255) NOT NULL,
  filesize INT NOT NULL,
  uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users(id)
);
