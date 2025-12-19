#!/usr/bin/env python3
"""
Script to create alx_book_store database in MySQL server
"""

import mysql.connector


def create_database():
    """
    Creates the alx_book_store database if it doesn't exist
    """
    connection = None
    
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',          # Replace with your MySQL username
            password='your_password'  # Replace with your MySQL password
        )
        
        if connection.is_connected():
            # Create cursor object
            cursor = connection.cursor()
            
            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            
            print("Database 'alx_book_store' created successfully!")
            
            # Close cursor
            cursor.close()
            
    except mysql.connector.Error as e:
        # Handle connection errors
        print(f"Error while connecting to MySQL: {e}")
        
    finally:
        # Close the database connection
        if connection is not None and connection.is_connected():
            connection.close()


if __name__ == "__main__":
    create_database()