# Dropship Business App Database
# Implemented with Python, Flask ORM, PostgreSQL

A Dropship Business database design that utilizes ORM via SQLAlchemy with Flask to manage backend app development in Python.  
API was tested through a client (e.g Insomnia), and relational database management was implemented via PostgreSQL.

Project files associated with the app are located in the ZIP file titled dropship_business_ORM.

The package includes: 

* Entity-relationship Diagram for a Dropship Business Model (draw.io) 

* Postgres SQL schema v1.0_2021-11-08 (.sql) - Initial design concepts, not used in final version. Includes examples of one-to-one, many-to-one, and many-to-many 
Foreign Key references. 

* pg_dump_11-23-2021 (.sql) - a database dump created using pg_dump. Features examples where database queries are optimized through the use of index. 

* Flask directory containing REST API that features subfolders for database migrations (Flask-Migrate), a Rest API built on Python backend using the Flask framework.
 
* Insomnia_Request_Collection_2021-11-21 (.json) - an Insomnia Request Collection featuring endpoints for various GET, POST, PUT/PATCH, and DELETE HTTP methods. 

* README.md documentation with a retrospective analysis regarding the project. 


## Technologies Utilized in the App Development Process

* Docker\
Instructions on Docker installation can be found here:\
https://docs.docker.com/get-docker/

* PostgreSQL\
Instructions on PostgreSQL installation can be referenced here: \
https://www.postgresql.org/

* pgadmin 4\
A well written tutorial on How to Install and run psql using docker can be found here:\
https://dev.to/shree_j/how-to-install-and-run-psql-using-docker-41j2

* Insomnia\
Instructions on Insomnia installation can be referenced here: \
https://insomnia.rest/

* Flask SQAlchemy\
Instructions on Flask-SQLAlchemy installation can be referenced here:\
https://pythonbasics.org/flask-sqlalchemy/

* venv\
Instructions regarding the Python virtual environment (venv) from which the app directory operates can be found here:\
https://docs.python.org/3/library/venv.html


## API Reference Tables


Accounts API
|      Name     |      HTTP Method     |     Parameter       |       Path                              |  Description  |
| ------------  |-------------         |    ------------     | --------------                          |---------------|
| index | GET | /accounts | http://localhost:5000/accounts  | Retrieves an index of every record stored in the accounts table. |
| update | PATCH  | /accounts/:id | http://localhost:5000/accounts/:id | Grants an ability to update a record in the accounts table. |
| delete account  | DELETE| /accounts/:id | http://localhost:5000/accounts/:id | Grants an ability to delete a selected user account. |\


Account Query Parameters
| Name | Data Type | Required/Optional | Description |
|------|--------|-------|------|
| name | string | optional | Lists the name associated with an account record. Can be updated with PATCH request. |
| purpose | string | optional | Lists the purpose associated with an account record. Can be updated with PATCH request. |\


Brands API
|      Name     |      HTTP Method     |     Parameter       |       Path                              |  Description  |
| ------------  |-------------         |    ------------     | --------------                          |---------------|
| index | GET | /brands | http://localhost:5000/brands | Retrieves an index of every record stored in the brands table. |
| new brand | POST | /brands | http://localhost:5000/brands | Instantiates a new record in the brands table. |
| update | PATCH | /brands/:id | http://localhost:5000/brands/:id | Grants an ability to update a record in the brands table. |\


Brand Query Parameters
| Name | Data Type | Required/Optional | Description |
| ------------  |-------------         |    ------------     | --------------  |
| address | string | optional | Lists the address associated with a given record. Can be updated with patch request. |
| email | string | optional | Lists the email associated with a given record. Can be updated with patch request. |
| name | string | optional | Lists the name associated with a given record. Can be updated with patch request. |\


Poducts API
|      Name     |      HTTP Method     |     Parameter       |       Path                              |  Description  |
| ------------  |-------------         |    ------------     | --------------                          |---------------|
| index | GET | /products | http://localhost:5000/products | Retrieves an index of every record stored in the products table. |\

Product Query Parameters
| Name | Data Type | Required/Optional | Description |
| ------------  |-------------         |    ------------     | --------------  |
| description | string | optional | Lists the description of a given record. |\


Orders API
|      Name     |      HTTP Method     |     Parameter       |       Path       |  Description  |
| ------------  |-------------         |    ------------     | --------------   |---------------|
| index | GET | /orders | http://localhost:5000/orders | Retrieves an index of every record stored in the orders table. |\


Order Query Parameters
| Name | Data Type | Required/Optional | Description |
| ------------  |-------------         |    ------------     | --------------  |
| account_id | integer | optional | Lists the account_id associated with an order record. |
| brand_id | integer | optional | Lists the brand_id associated with an order record. |
| product_id | integer | optional | Lists the product_id associated with an order record. |
| product_quantity | integer | optional | Lists the product_quantity associated with an order record. |\

\
Parcels API
|      Name     |      HTTP Method     |     Parameter       |       Path                              |  Description  |
| ------------  |-------------         |    ------------     | --------------                          |---------------|
| index | GET | /parcels | http://localhost:5000/parcels | Retrieves an index of every record stored in the parcels table. |\

Parcel Query Parameters
| Name | Data Type | Required/Optional | Description |
| ------------  |-------------         |    ------------     | --------------  |
| customer_id | integer | optional |  Lists the customer_id associated with a parcel record. |
| distributor_id | integer | optional |  Lists the distributor_id associated with a parcel record. |
| estimated_delivery_date | date | optional |  Lists the estimated delivery date associated with a parcel record. |
| shipment_date | date | optional |  Lists the shipment date associated with a parcel record. |\


## Retrospective Analysis

Designing an ER-Diagram encompassing all of the entities, attributes, and relationships needed for initial database creation was key. This provides an allowance to focus later efforts on developing a more efficient database. Next, shifting focus on creating table structures with raw SQL based on many-to-many, one-to-many, and one-to-one relationships presented in the ER-Diagram lead to a reassessment of entity relations, helping to further optimize and strengthen database architecture. Raw SQL statements were then converted to ORM statements using SQLAlchemy with Flask using CRUD operations to set up the database. Data was inputted into the database using PostgreSQL insert statements on the pgAdmin 4 local server. HTTP-based API was developed and interacted with using Insomnia. \
\
The application was implemented with ORM due to it's known advantage of speeding up the development process. And with ORM, database migration is simplified when leveraging object-oriented programming methods in Python via SQLAlchemy. Python automates the process of database maintenance, so upgrades may occur on a scheduled basis with the click of a button. \
\
Improvements to the database design include modifying Blueprint related functions to dump as a string literals when converting to JSON in order to instantiate GET, POST, PUT/PATCH method requests. This would allow the app to manage, retrieve, and update data related to price points, tracking information, and other important data stored on the database in numerical decimal form. Further adding relationships between entities is another method we could explore, allowing us to retrieve datasets that may not immediately seem useful in the nearterm, but could prove invaluable in the long term (i.e.understanding which products ship out the most from what distribution channels in a given time frame. Unfortunately, without a larger dataset collected over a much larger time frame, predicting the effectiveness of tentative entity relationships is merely speculative in nature. Fortunately, ORM will allow for such upgrades to occur quite reactively as database relationship opportunities present themselves.


