import psycopg2

def connect_db():

    conn = psycopg2.connect(
        host="localhost",
        database="student_database",  # or postgres
        user="postgres",
        password="Amit@123",
        port="5432"
    )

    return conn