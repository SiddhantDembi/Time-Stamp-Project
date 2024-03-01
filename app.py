import streamlit as st
from datetime import datetime
import mysql.connector
import pytz
import os
from dotenv import load_dotenv
import csv

# Load environment variables from .env file
load_dotenv()

# Database connection details
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_DATABASE = os.getenv("DB_DATABASE")

# Login password
LOGIN_PASSWORD = os.getenv("LOGIN_PASSWORD")

# Create a MySQL connection
db_connection = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_DATABASE
)

# Create a cursor to interact with the database
db_cursor = db_connection.cursor()

def login_page():
    st.title("Login Page")
    password = st.text_input("Enter Password", type="password")
    if password == LOGIN_PASSWORD:
        st.success("Login Successful!")
        return True
    elif password != "":
        st.error("Wrong Password")
    return False

def save_current_datetime():
    # Get the current time in the Indian Standard Time (IST) timezone
    ist_timezone = pytz.timezone("Asia/Kolkata")
    current_datetime_ist = datetime.now(ist_timezone)
    
    formatted_date = current_datetime_ist.strftime("%d %B %Y")
    next_id_data_id = get_next_id("data_id")
    next_id_raw_data_id = get_next_id("raw_data_id")
    
    # Insert the date entry into the MySQL database for data_id table
    query_data_id = "INSERT INTO data_id (ID, Date, Time) VALUES (%s, %s, %s)"
    values_data_id = (next_id_data_id, formatted_date, current_datetime_ist.strftime("%I:%M %p"))
    db_cursor.execute(query_data_id, values_data_id)
    db_connection.commit()
    
    # Insert the date entry into the MySQL database for raw_data_id table
    query_raw_data_id = "INSERT INTO raw_data_id (ID, Date, Time) VALUES (%s, %s, %s)"
    values_raw_data_id = (next_id_raw_data_id, formatted_date, current_datetime_ist.strftime("%I:%M %p"))
    db_cursor.execute(query_raw_data_id, values_raw_data_id)
    db_connection.commit()
    
    st.success(f"Saved: {formatted_date} {current_datetime_ist.strftime('%I:%M %p')} (IST)")

def get_next_id(table_name):
    # Retrieve the next ID from the database based on the table name
    query = f"SELECT MAX(ID) FROM {table_name}"
    db_cursor.execute(query)
    result = db_cursor.fetchone()
    if result[0] is not None:
        return result[0] + 1
    else:
        return 1

def view_previous_entries(table_name):
    st.subheader("Previous Entries")
    
    # Retrieve previous entries from the specified table in the database in descending order by ID
    query = f"SELECT * FROM {table_name} ORDER BY ID DESC"
    db_cursor.execute(query)
    entries = db_cursor.fetchall()
    
    for entry in entries:
        data_id, formatted_date, formatted_time = entry
        st.write(f"ID: {data_id}")
        st.write(f"Date: {formatted_date}")
        st.write(f"Time: {formatted_time}")
        st.write("-" * 30)

def delete_latest_entry(table_name):
    # First, retrieve the ID of the latest entry from the specified table
    query_select = f"SELECT MAX(ID) FROM {table_name}"
    db_cursor.execute(query_select)
    latest_id = db_cursor.fetchone()[0]
    
    if latest_id is not None:
        # Then, delete the entry with the latest ID from the specified table
        query_delete = f"DELETE FROM {table_name} WHERE ID = %s"
        db_cursor.execute(query_delete, (latest_id,))
        db_connection.commit()
        st.success("Latest entry deleted successfully.")
    else:
        st.warning("No entries found to delete.")

def refresh():
   st.rerun()
   
def export_table_as_csv():
    st.info("Exporting data to CSV file...")
    query = "SELECT * FROM data_id"
    db_cursor.execute(query)
    data = db_cursor.fetchall()
    with open("data_id.csv", "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([i[0] for i in db_cursor.description])
        csv_writer.writerows(data)
    st.success("Data exported successfully!")
    
def export_raw_table_as_csv():
    st.info("Exporting raw data to CSV file...")
    query = "SELECT * FROM raw_data_id"
    db_cursor.execute(query)
    data = db_cursor.fetchall()
    with open("raw_data_id.csv", "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([i[0] for i in db_cursor.description])
        csv_writer.writerows(data)
    st.success("Raw data exported successfully!")

if login_page():
    st.title("Date and Time Logger")
    
    st.write("-" * 30)

    
    if st.button("Refresh"):
        refresh()
        
    if st.button("Save Date and Time"):
        save_current_datetime()
    
    st.write("-" * 30)

    
    if st.button("Previous Entries"):
        view_previous_entries("data_id")
    
    
    if st.button("Delete Latest Entry"):
        delete_latest_entry("data_id")
    
    st.write("-" * 30)

    
    if st.button("Previous Raw Entries"):
        view_previous_entries("raw_data_id")
    
    if st.button("Delete Latest Raw Entry"):
        delete_latest_entry("raw_data_id")
    
    
    st.write("-" * 30)

    
    if st.button("Export Data"):
        export_table_as_csv()
        
    if st.button("Export Raw Data"):
        export_raw_table_as_csv()
        
# Close the database connection when done
db_cursor.close()
db_connection.close()
