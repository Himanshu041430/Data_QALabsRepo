from sqlalchemy import create_engine
import pandas as pd

# Set up the connection to MySQL
engine = create_engine('mysql+pymysql://root:Canada%4014@localhost:3306/employees')

connection = None

try:
    # Establish a connection
    connection = engine.connect()
    print("Connection to MySQL established successfully.")

    # Define your query to read from the 'salaries' table
    query2 = 'SELECT * FROM salaries'

    # Execute the query and load the data into a pandas DataFrame
    df1 = pd.read_sql(query2, connection)

    # Display the resulting DataFrame
    print(df1)

except Exception as e:
    print(f"Error occurred: {e}")

finally:
    # Ensure the connection is closed
    if connection:
        connection.close()
        print("Connection closed.")
