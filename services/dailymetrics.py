import psycopg2
from dto.dailymetric import DailyMetrics

def insertDailyMetric(dailymetric: DailyMetrics):

    # Connect to your postgres DB
    conn = psycopg2.connect("dbname=lifeflow user=postgres")

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute a query
    cur.execute("INSERT INTO dailymetrics VALUES (default, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
        dailymetric.user_id, dailymetric.date, dailymetric.mood, dailymetric.energy, dailymetric.appetite, dailymetric.cravings, dailymetric.sleep_quality, dailymetric.sleep_time, dailymetric.workout_time, dailymetric.workout_type 
    ))

    # Make the changes to the database persistent
    conn.commit()

    # Close communication with the database
    cur.close()
    conn.close()