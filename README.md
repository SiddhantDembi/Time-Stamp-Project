# Date and Time Logger

This Python project is a simple Date and Time Logger application designed to assist users in tracking timestamps conveniently. 

## Features
- **Authentication:** Users authenticate via a password-protected login system.
- **Timestamp Management:** Users can save current timestamps, view, and delete past entries.
- **Export to CSV:** The application allows users to export data to CSV files for further analysis.
- **MySQL Integration:** Data is stored securely in a MySQL database for efficient management and retrieval.

## Setup
Clone the repository.
```bash
git clone https://github.com/SiddhantDembi/Time-Stamp-Project.git
```
Install the required dependencies using pip:
```bash
pip install -r requirements.txt
```
Set up the MySQL database and configure the environment variables in a .env file. Ensure the following variables are set:

```
DB_HOST=your_mysql_host
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
DB_DATABASE=your_mysql_database
LOGIN_PASSWORD=your_login_password
```

## Run
```bash
streamlit run app.py
```
or
```bash
python -m streamlit run app.py
```
