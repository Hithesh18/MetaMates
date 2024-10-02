from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

def get_doctors():
    try:
        connection = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="root123",
            host="localhost"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT Name, Speciality, Address, ClinicOffice, ZIPCode, City, PhoneNumber, Website, Rating, OnlineAppointment FROM Doctors")
        doctors = cursor.fetchall()
        cursor.close()
        connection.close()
        return doctors
    except Exception as e:
        print(f"Error: {e}")
        return []

@app.route('/')
def index():
    doctors = get_doctors()
    return render_template('index.html', doctors=doctors)

if __name__ == '__main__':
    app.run(debug=True)
