import tkinter.messagebox as messagebox
import mysql.connector
import numpy as np

def save_data_to_mysql(Registration_Number, name, date, dob, age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, result):
    try:
        # Connect to the MySQL server
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="anass"
        )

        # Create a cursor object
        mycursor = mydb.cursor()

        # Create the database if it does not exist
        mycursor.execute("CREATE DATABASE IF NOT EXISTS Heart_Data")

        # Connect to the specific database
        mydb.database = "Heart_Data"

        # Check if the table already exists, and if not, create it
        mycursor.execute("""CREATE TABLE IF NOT EXISTS data_patient (
                            Registration_Number INT PRIMARY KEY,
                            name VARCHAR(50),
                            date VARCHAR(10),
                            dob VARCHAR(10),
                            age VARCHAR(3),
                            sex VARCHAR(10),
                            cp VARCHAR(10),
                            trestbps VARCHAR(5),
                            chol VARCHAR(5),
                            fbs VARCHAR(10),
                            restecg VARCHAR(10),
                            thalach VARCHAR(5),
                            exang VARCHAR(10),
                            oldpeak VARCHAR(5),
                            slope VARCHAR(10),
                            ca VARCHAR(5),
                            thal VARCHAR(10),
                            result VARCHAR(10))""")

        # Insert the data into the table
        mycursor.execute("""INSERT INTO data_patient (Registration_Number, name, date, dob, age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, result) 
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                         (Registration_Number, name, str(date), str(dob), str(age), sex, str(cp), str(trestbps), str(chol), str(fbs),
                          str(restecg), str(thalach), str(exang), str(oldpeak), str(slope), str(ca), str(thal), str(result)))

        # Commit the changes and close the connection
        mydb.commit()
        mycursor.close()
        mydb.close()

        # Show a success message
        messagebox.showinfo("Success", "Data saved to MySQL database")

    except mysql.connector.Error as error:
        print(f"MySQL error: {error}")
        messagebox.showerror("Error", "Failed to save data to MySQL database")
