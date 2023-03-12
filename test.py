import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='password',
    db='mydatabase',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

# write data in database

try:
    with conn.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('john@example.com', 'mypassword'))

    # Commit changes
    conn.commit()

    print("Record inserted successfully")
finally:
    conn.close()

# update data in database
try:
    with conn.cursor() as cursor:
        # Update a record
        sql = "UPDATE `users` SET `password`=%s WHERE `email`=%s"
        cursor.execute(sql, ('newpassword', 'john@example.com'))

    # Commit changes
    conn.commit()

    print("Record updated successfully")
finally:
    conn.close()

# delete data in database
try:
    with conn.cursor() as cursor:
        # Delete a record
        sql = "DELETE FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('john@example.com',))

    # Commit changes
    conn.commit()

    print("Record deleted successfully")
finally:
    conn.close()

# read data in database
try:
    with conn.cursor() as cursor:
        # Read data from database
        sql = "SELECT * FROM `users`"
        cursor.execute(sql)

        # Fetch all rows
        rows = cursor.fetchall()

        # Print results
        for row in rows:
            print(row)
finally:
    conn.close()
    