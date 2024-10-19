from sqlalchemy import create_engine
import pandas as pd

# Set up the connection to MySQL
engine = create_engine('mysql+pymysql://root:Canada%4014@localhost:3306/employees')

connection = None

try:
    # Establish a connection
    connection = engine.connect()
    print("Connection to MySQL established successfully.")

#---- my sql Quererry ---- detabase is employees in my sql---

    # Define your query
    query1 = 'SELECT * FROM employees'

    # Execute the query and load the data into a pandas DataFrame
    df = pd.read_sql(query1, connection)

    # Display the resulting DataFrame
    print(df)

except Exception as e:
    print(f"Error occurred: {e}")

finally:
    # Ensure the connection is closed
    if connection:
        connection.close()
        print("Connection closed.")


