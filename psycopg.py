import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect("dbname=lifeflow user=postgres")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
cur.execute("SELECT * FROM Users")

# Retrieve query results
records = cur.fetchall()

print(records)

# Close communication with the database
cur.close()
conn.close()
