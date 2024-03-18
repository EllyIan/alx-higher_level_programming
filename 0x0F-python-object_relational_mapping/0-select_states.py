#!/usr/bin/python3
"""
Module that connects a python script to a database
"""

if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    """ Connect database using command-line arguments
     # Create cursor obj to interact with database
      # Execute a SELECT query to fetch data
       # fetch all the data returned by the query
       # Iterate through the fetched data and print each row
       # Close all cursors"""
    my_db = MySQLdb.connect(host='localhost', user=argv[1], password=argv[2],
                            db=argv[3], port=3306)
    my cusor = my_db.cursor()
    
    my_cursor.execute("SELECT * FROM states ORDER BY states.id ASC;")

        my_data = my_cursor.fetchall()

        for row in my_data:
        print(row)

    my_cursor.close()

    # Close all databases
    my_db.close()
