Overview
Finding reliable doctors in a busy city like Stuttgart can be daunting. Our project aims to streamline this process by offering a robust platform where users can filter and discover the best doctors in Stuttgart. By leveraging metadata and advanced search functionalities, users can refine their search based on criteria like medical specialty, clinic location, patient reviews, and appointment availability. This not only saves time but also ensures that users find doctors who meet their specific needs and preferences.
Project Objectives
The primary goal is to streamline the collection, preparation, and access of doctor information metadata from XML files, inserting it into a PostgreSQL database using Python.
Main Objectives:
•
Efficient data collection from external XML sources
•
Proper preparation and validation of collected data
•
Reliable access and insertion of data into a PostgreSQL database
Data Collection
•
Collect data from an external XML file, which includes information like the doctor’s name, specialty, address, contact details, and appointment availability.
•
Use tools and libraries such as xml.etree.ElementTree for parsing XML files.
Data Preparation
•
Parse and prepare the data for insertion into the database.
•
Transform XML data into a structured format suitable for database insertion.
Data Access
•
Connect to the PostgreSQL database and insert the prepared data.
•
The database schema includes fields such as Name, Speciality, Address, and more.
Technologies Used
•
XML, PostgreSQL, Python, HTML, CSS, JavaScript


To run the project
1.Our project as 4 files (2 python, 1 XML and 1 HTML (Inside Templates) )
2.Run $ python main.py (It will create tables and insert the XML data into Postgres)
3.Run $ python app.py (It will open Frontend HTML page for view the tables)

For testing purpose we have added 4 data and also attached collected XML Raw data.
