# SprintChallengeSQLDatabase
SprintChallenge - SQL and Database 09252020

### Part 4 - Questions (and your Answers)
 
Answer the following questions, baseline ~3-5 sentences each, as if they were
interview screening questions (a form you fill when applying for a job):
 
- In the Northwind database, what is the type of relationship between the
 `Employee` and `Territory` tables?
 #Employees' table provides personal information about the employee that includes where he/she reports to while Territories' table provides information about the employees' exact territory location that includes the territoryID. This shows that multiple Employees can be assigned to a different territories. You can join both tables using territoryID.

- What is a situation where a document store (like MongoDB) is appropriate, and
 what is a situation where it is not appropriate?
#A document is a representation of a single entity of data in the MongoDB database. It is appropriate if a collection consists of one or more related objects. In MongoDB, documents can contain embedded subdocuments, providing a much closer inherent data model to your applications.
A collection acts similarly to a table in a traditional SQL database. Its not appropriate if a collection is not enforced by a strict schema. Instead, documents in a collection can have a slightly different structure from one another, as needed. This reduces the need to break items in a document into several different tables, as is often done in SQL implementations.

- What is "NewSQL", and what is it trying to achieve?
#NewSQL databases represent the marriage of the ACID–based transactional consistency and reliability of OLTP databases to the high availability, horizontal scalability, and fault tolerance found in NoSQL databases. NewSQL is trying to achieve the best of traditional relational systems with the inherent scalability formerly found only in NoSQL. The expectation is that NewSQL systems are about 50 times faster than traditional OLTP RDBMS.
