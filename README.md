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

## Demo

Landing Page
![WhatsApp Image 2024-03-02 at 11 34 42_343cef18](https://github.com/SiddhantDembi/Time-Stamp-Project/assets/106478699/9a368808-d30c-441c-93f3-c3179fab1dcb)

After successfully logging in
![WhatsApp Image 2024-03-02 at 11 35 23_45ca8425](https://github.com/SiddhantDembi/Time-Stamp-Project/assets/106478699/23ccc975-44f8-4733-8406-ae1322fdc254)

Save the current date and time by clicking the `Save Date and Time ` button.
![WhatsApp Image 2024-03-02 at 11 36 40_bce2f089](https://github.com/SiddhantDembi/Time-Stamp-Project/assets/106478699/ce877d3f-eddd-44dd-aec3-846b8bb14d45)

View previous entries by clicking on `Previous Entries` button. 
![WhatsApp Image 2024-03-02 at 11 37 07_6759110f](https://github.com/SiddhantDembi/Time-Stamp-Project/assets/106478699/8d06fa36-883a-4f69-b0a1-e3b7a8e798de)

To delete the latest entry click on the `Delete Latest Entry`
![WhatsApp Image 2024-03-02 at 11 37 31_19c1652f](https://github.com/SiddhantDembi/Time-Stamp-Project/assets/106478699/d29f91a9-e010-42d9-af62-aec6d1b19780)
