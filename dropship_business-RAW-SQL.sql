"""
This is an initial database implementation based off of my initial Dropship Business ER Diagram.

"""



--created customer entity

CREATE TABLE customers (
	customer_id SERIAL PRIMARY KEY,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	email VARCHAR(50) NOT NULL UNIQUE,
	address_line1 VARCHAR(75) NOT NULL,
	address_line2 VARCHAR(75),
	city VARCHAR(90) NOT NULL,
	country VARCHAR(60) NOT NULL,
	zipcode VARCHAR(20) NOT NULL
);

--created an account entity

CREATE TABLE accounts (
	account_id SERIAL PRIMARY KEY,
	password VARCHAR(25) NOT NULL,
	user_name VARCHAR(25) UNIQUE NOT NULL,
	account_purpose VARCHAR(25),
	customer_id INT NOT NULL UNIQUE
);

--created order entity

CREATE TABLE orders (
	order_id SERIAL PRIMARY KEY,
	processing_date DATE NOT NULL,
	product_quantity INT NOT NULL,
	account_id INT NOT NULL,
	brand_id INT NOT NULL
);
	
--created product entity

CREATE TABLE products (
	product_id SERIAL PRIMARY KEY,
	description VARCHAR(50) UNIQUE NOT NULL,
	price DECIMAL(10,2) NOT NULL
);

--created brands entity

CREATE TABLE brands (
	brand_id SERIAL PRIMARY KEY,
	name TEXT NOT NULL UNIQUE,
	email VARCHAR(50) NOT NULL UNIQUE,
	address_line1 VARCHAR(75) NOT NULL,
	address_line2 VARCHAR(75),
	city VARCHAR(85) NOT NULL,
	country VARCHAR(56) NOT NULL,
	zipcode VARCHAR(20) NOT NULL
);

--created co-packer entity

CREATE TABLE distributors (
	distributor_id SERIAL PRIMARY KEY,
	name TEXT NOT NULL UNIQUE,
	email VARCHAR(50) NOT NULL UNIQUE
);

--created package entity
	
CREATE TABLE parcels (
	parcel_id SERIAL PRIMARY KEY,
	usps_tracking_number CHAR(22) NOT NULL,
	date_shipped DATE NOT NULL,
	estimated_delivery_date DATE NOT NULL,
	customer_id INT NOT NULL,
	distributor_id INT NOT NULL 
);

--initial design for one to one relationship

ALTER TABLE accounts
ADD CONSTRAINT fk_accounts_customers
FOREIGN KEY (customer_id) REFERENCES customers (customer_id);


--initial design alter statements for one to many relationships

ALTER TABLE parcels
ADD CONSTRAINT fk_parcels_customers
FOREIGN KEY (customer_id) REFERENCES customers (customer_id);

ALTER TABLE parcels
ADD CONSTRAINT fk_parcles_distributors
FOREIGN KEY (distributor_id) REFERENCES distributors (distributor_id);

ALTER TABLE orders
ADD CONSTRAINT fk_orders_accounts 
FOREIGN KEY (account_id) REFERENCES accounts (account_id);

ALTER TABLE orders 
ADD CONSTRAINT fk_orders_brands
FOREIGN KEY (brand_id) REFERENCES brands (brand_id);

--initial design table and alter statements for many to many relationships


CREATE TABLE product_brands(
	product_id INT NOT NULL,
	brand_id INT,
	PRIMARY KEY (product_id, brand_id)
);

ALTER TABLE product_brands
ADD CONSTRAINT fk_product_brand_products
FOREIGN KEY (product_id) REFERENCES products (product_id);

ALTER TABLE product_brands
ADD CONSTRAINT fk_product_brand_brands
FOREIGN KEY (brand_id) REFERENCES brands (brand_id);



CREATE TABLE brand_distribution (
	brand_id INT NOT NULL,
	distributor_id INT,
	PRIMARY KEY (brand_id, distributor_id)
);

ALTER TABLE brand_distribution
ADD CONSTRAINT fk_brand_distribution_brands
FOREIGN KEY (brand_id) REFERENCES brands (brand_id);

ALTER TABLE brand_distribution
ADD CONSTRAINT fk_brand_distribution_distributors
FOREIGN KEY (distributor_id) REFERENCES distributors (distributor_id);