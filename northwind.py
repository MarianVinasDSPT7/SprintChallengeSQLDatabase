import sqlite3
#sprintChallenge 09252020 
conn = sqlite3.connect("northwind_small.sqlite3")
cursor = conn.cursor()

# 1.What are the ten most expensive items (per unit price) in the database?
query1 = '''
SELECT
	ProductName,
	UnitPrice
FROM Product
ORDER BY Unitprice ASC
LIMIT 10;
'''
result1 = cursor.execute(query1).fetchall()
print(f'The 10 most expensive items: {result1}')

# 2.What is the average age of an employee at the time of their hiring? 
# (Hint: alot of arithmetic works with dates.)
query2 = '''
SELECT
	(HireDate - BirthDate) as Age,
	AVG((HireDate - BirthDate))
FROM Employee
'''
result2 = cursor.execute(query2).fetchall()
print(f'The average age of an employee at the time of their hiring: {result2}')

# PART3:
# 1.What are the ten most expensive items (per unit price) in the database *and* their suppliers?
query3 = '''
SELECT
	Product.Id,
    Product.ProductName,
	Product.UnitPrice,
	Supplier.Id
FROM Product
JOIN Supplier ON Product.Id = Supplier.Id
ORDER BY UnitPrice ASC
LIMIT 10;
'''
result3 = cursor.execute(query3).fetchall()
print(f'The 10 most expensive items with suppliers data: {result3}')

# 2.What is the largest category (by number of unique products in it)?
query4 = '''
SELECT
	Product.Id,
	Product.ProductName,
	Product.UnitPrice,
	Supplier.Id,
	Category.Id,
	count(distinct Product.Id) as ProductId
FROM Product
JOIN Supplier ON Product.Id = Supplier.Id
JOIN Category ON Product.Id = Category.Id
GROUP BY Category.Id
ORDER BY UnitPrice ASC
LIMIT 1;
'''
result4 = cursor.execute(query4).fetchall()
print(f'The largest category: {result4}')