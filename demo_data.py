import sqlite3
#Sprintchallenge 09252020
# DB_FILEPATH = os.path.join(os.path.dirname(__file__), "demo_data.sqlite3")
conn = sqlite3.connect("demo_data.sqlite3")
cursor = conn.cursor()

# Drop table to create a new one
cursor.execute('DROP TABLE IF EXISTS demo')

create_table_query = '''
CREATE TABLE IF NOT EXISTS demo (
    s TEXT,
    x INT, 
    y INT)
'''
cursor.execute(create_table_query)

sample_data = [
    ('g', 3, 9),
    ('v', 5, 7),
    ('f', 8, 7)
]

for row in sample_data:
    insert_data_query = f'''INSERT INTO demo (s, x, y)
        VALUES {row}
    '''
    cursor.execute(insert_data_query)

conn.commit()

# Count how many rows you have - it should be 3!
query1 = 'SELECT COUNT(*) FROM demo'
result1 = cursor.execute(query1).fetchone()
print(result1)

# How many rows are there where both `x` and `y` are at least 5?
query2 = 'SELECT COUNT(*) FROM demo WHERE x AND y'
result2 = cursor.execute(query2).fetchone()
print(result2)

# How many unique values of `y` are there (hint - `COUNT()` can accept a keyword `DISTINCT`)?
query3 = 'SELECT COUNT(DISTINCT y) FROM demo'
result3 = cursor.execute(query3).fetchone()
print(result3)