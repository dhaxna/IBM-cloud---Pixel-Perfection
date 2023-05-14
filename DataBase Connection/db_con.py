import mysql.connector

# Connect to the MySQL database
cnx = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
)

# Create a cursor object to execute SQL queries
cursor = cnx.cursor()

# Insert a new user into the 'users' table
username = 'exampleuser'
password = 'password123'
query = "INSERT INTO users (username, password) VALUES (%s, %s)"
values = (username, password)
cursor.execute(query, values)
cnx.commit()
print("User inserted successfully")

# Retrieve all images uploaded by a specific user
user_id = 1
query = "SELECT * FROM images WHERE user_id = %s"
values = (user_id,)
cursor.execute(query, values)
result = cursor.fetchall()
for row in result:
    print(row)

# Update the filename 
image_id = 1
new_filename = 'new_filename.jpg'
query = "UPDATE images SET filename = %s WHERE id = %s"
values = (new_filename, image_id)
cursor.execute(query, values)
cnx.commit()
print("Image filename updated successfully")

# Delete an image from the 'images' table
image_id = 1
query = "DELETE FROM images WHERE id = %s"
values = (image_id,)
cursor.execute(query, values)
cnx.commit()
print("Image deleted successfully")

 
cursor.close()
cnx.close()
