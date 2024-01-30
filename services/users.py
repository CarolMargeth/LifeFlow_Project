import psycopg2
from dto.user import User

def insertUser(user:User):

    # Connect to your postgres DB
    conn = psycopg2.connect("dbname=lifeflow user=postgres")

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute a query
    cur.execute("INSERT INTO Users VALUES (default, %s, %s, %s, %s, %s, %s)", (
        user.first_name, user.middle_name, user.last_name, user.age, user.height, user.email
    ))

    # Make the changes to the database persistent
    conn.commit()

    # Close communication with the database
    cur.close()
    conn.close()