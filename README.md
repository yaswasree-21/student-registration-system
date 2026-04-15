# Flask User Registration App

This is a simple Flask web application that allows users to register by filling out a form. The data is stored in a MySQL database.

## Features
- User registration form with fields: First Name, Last Name, Roll Number, Email, Phone Number, College Name, Department, Skills (multi-select), and Comments.
- Data insertion into a MySQL database table named `registration`.
- Renders templates for the form and a success page.

## Prerequisites
- Python 3.x
- MySQL Server
- Flask
- mysql-connector-python

## Installation
1. Clone or download the project files.
2. Install dependencies:
3. Set up MySQL database:
- Create a database named `registrationdb`.
- Create a table `registration` with the following schema:
  ```sql
  CREATE TABLE registration (
      id INT AUTO_INCREMENT PRIMARY KEY,
      fname VARCHAR(255),
      lname VARCHAR(255),
      roll_no VARCHAR(255),
      email VARCHAR(255),
      phone_no VARCHAR(255),
      college VARCHAR(255),
      dept VARCHAR(255),
      skills TEXT,
      comments TEXT
  );
  ```
- Update the database connection details in [app.py](http://_vscodecontentref_/0) (host, user, password).

## Usage
1. Run the application:
2. Open a web browser and go to `http://localhost:5000`.
3. Fill out the registration form and submit.

## Templates
- [form.html](http://_vscodecontentref_/1): The registration form.
- `stored.html`: Confirmation page after successful submission.

## Notes
- Ensure MySQL server is running.
- The app runs in debug mode by default.
- Skills are stored as a comma-separated string.
- If no skills are selected, it defaults to "None".