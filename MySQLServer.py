import mysql.connector
from mysql.connector import Error
import getpass


def create_database():
    """
    Creates the alx_book_store database if it doesn't exist
    """
    connection = None
    
    try:
        # Get MySQL credentials from user
        username = input("Enter MySQL username (default: root): ") or "root"
        password = getpass.getpass("Enter MySQL password: ")
        
        connection = mysql.connector.connect(
            host='localhost',
            user=username,
            password=password
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            
            print("Database 'alx_book_store' created successfully!")
            
            cursor.close()
            
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        
    finally:
        if connection is not None and connection.is_connected():
            connection.close()


if __name__ == "__main__":
    create_database()