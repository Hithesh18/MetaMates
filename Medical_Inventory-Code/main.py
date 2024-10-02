import psycopg2
import xml.etree.ElementTree as ET

# Function to parse the XML file
def parse_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    doctors = []
    
    for doctor in root.findall('Doctor'):
        name = doctor.find('Name').text
        speciality = doctor.find('Speciality').text
        address = doctor.find('Address').text
        clinic_office = doctor.find('ClinicOffice').text
        zip_code = doctor.find('ZIPCode').text
        city = doctor.find('City').text
        phone_number = doctor.find('PhoneNumber').text
        website = doctor.find('Website').text if doctor.find('Website').text else None
        rating = float(doctor.find('Rating').text)
        online_appointment = doctor.find('OnlineAppointment').text.lower() == 'yes'
        
        doctors.append((name, speciality, address, clinic_office, zip_code, city, phone_number, website, rating, online_appointment))
    
    return doctors

# Function to insert data into the PostgreSQL database
def insert_data_to_postgres(doctors):
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="root123",
            host="localhost"
        )
        cursor = conn.cursor()
        
        # Create the table if it doesn't exist
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS Doctors (
            ID SERIAL PRIMARY KEY,
            Name VARCHAR(255),
            Speciality VARCHAR(255),
            Address VARCHAR(255),
            ClinicOffice VARCHAR(255),
            ZIPCode VARCHAR(10),
            City VARCHAR(255),
            PhoneNumber VARCHAR(20),
            Website VARCHAR(255),
            Rating FLOAT,
            OnlineAppointment BOOLEAN,
            UNIQUE (Name, Speciality, Address, PhoneNumber)
        )
        '''
        cursor.execute(create_table_query)
        
        # Insert data into the table
        insert_query = '''
        INSERT INTO Doctors (Name, Speciality, Address, ClinicOffice, ZIPCode, City, PhoneNumber, Website, Rating, OnlineAppointment)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (Name, Speciality, Address, PhoneNumber) DO NOTHING
        '''
        cursor.executemany(insert_query, doctors)
        
        # Commit the transaction
        conn.commit()
        
        # Close the cursor and connection
        cursor.close()
        conn.close()
        
        print("Data inserted successfully")
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Path to the XML file
    xml_file_path = 'data.xml'
    
    # Parse the XML file
    doctors_data = parse_xml(xml_file_path)
    
    # Insert data into PostgreSQL
    insert_data_to_postgres(doctors_data)
