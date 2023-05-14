import mysql.connector
from getpass import getpass

# Get the database credentials from the environment or securely prompt the user
db_host = getpass("Enter the database host:")
db_username = getpass("Enter the database username:")
db_password = getpass("Enter the database password:")

# Connect to the MySQL database
cnx = mysql.connector.connect(
    host=db_host,
    user=db_username,
    password=db_password,
    database="your_database"
)

# ...
# Perform database operations (insert, select, update, delete)
# ...

# Close the database connection
cnx.close()

