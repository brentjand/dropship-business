from faker import Faker
from datetime import datetime
import random
import csv


"""
Faker command library for CSV data creation
https://zetcode.com/php/faker/

https://faker.readthedocs.io/en/master/providers/faker.providers.profile.html

https://towardsdatascience.com/generation-of-large-csv-data-using-python-faker-8cfcbedca7a7

SQL Statements


--8,9,10

UPDATE parcels
SET brand_id = 8
WHERE id = 5
;



INSERT INTO accounts (
	username, password, purpose, customer_id
	)
	VALUES 
	('Emily.K', 'QWsdfdf123','business', 1),
	('Charles.S', 'sdfrte#reE', 'busniess', 2),
	('Anthony.F', 'hdhdsfR5s', 'business', 3),
	('Aaron.M', 'pasword1234$@', 'personal', 4),
	('Rachel.D', 'hdhdhdh438&', 'busniess', 5),
	('Oliver.G', 'korsgirl123$', 'busniess', 6),
	('Chad.D', 'chadspass1', 'hobby', 7),
	('Michael.H', 'mh1_1966', 'business', 8)
	;


--INSERT INTO brands (name, email, address)
--VALUES ('Japanese Kaolin Expressions', 'kaolin-sales@gmail.com', '11541 Castaneda Radial, Valerieburgh, GA 08622');

--INSERT INTO products (description, price)
--VALUES ('BROWN Classic Dinner 10ct', 19.99);

--INSERT INTO distributors (name, email, address)
--VALUES ('Pottery Warehouse', 'contact@potterywarehouse.com', '62174 Wang Streets, Riveraview, KY 68065');

--INSERT INTO orders (product_quantity, processing_date, product_id, account_id, brand_id)
--VALUES (1, '10-23-2021', 15, 9, 3);

--INSERT INTO parcels (usps_tracking_number, shipment_date, estimated_delivery_date, customer_id, distributor_id)
--VALUES ('57848385685684848', '10-29-2021', '11-05-2021', 4, 2);


"""

faker = Faker()


for i in range(10):
    print(faker.date())


"""
import csv
from faker import Faker
import datetime

def datagenerate(records, headers):
    fake = Faker('en_US')
    fake1 = Faker('en_GB')   # To generate phone numbers
    with open("People_data.csv", 'wt') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        writer.writeheader()
        for i in range(records):
            full_name = fake.name()
            FLname = full_name.split(" ")
            Fname = FLname[0]
            Lname = FLname[1]
            domain_name = "@testDomain.com"
            userId = Fname +"."+ Lname + domain_name
            
            writer.writerow({
                    "Email Id" : userId,
                    "Prefix" : fake.prefix(),
                    "Name": fake.name(),
                    "Birth Date" : fake.date(pattern="%d-%m-%Y", end_datetime=datetime.date(2000, 1,1)),
                    "Phone Number" : fake1.phone_number(),
                    "Additional Email Id": fake.email(),
                    "Address" : fake.address(),
                    "Zip Code" : fake.zipcode(),
                    "City" : fake.city(),
                    "State" : fake.state(),
                    "Country" : fake.country(),
                    "Year":fake.year(),
                    "Time": fake.time(),
                    "Link": fake.url(),
                    "Text": fake.word(),
                    })
    
if __name__ == '__main__':
    records = 100
    headers = ["Email Id", "Prefix", "Name", "Birth Date", "Phone Number", "Additional Email Id",
               "Address", "Zip Code", "City","State", "Country", "Year", "Time", "Link", "Text"]
    datagenerate(records, headers)
    print("CSV generation complete!")
"""
