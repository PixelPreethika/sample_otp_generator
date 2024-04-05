
import mysql.connector

def create_tables():
    try:
        # Establish a connection to the MySQL server
        connection = mysql.connector.connect(
            host="localhost",  # Or use the IP address of your Docker container
            port=8001,         # Port you mapped when starting the container
            user="root",       # Root user by default
            password="12345",  # Password you set when starting the container
            database="mydatabase"    # Optional: specify the database you want to connect to
        )

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Define the SQL statements to create tables
        create_queries = [
            """
            CREATE TABLE IF NOT EXISTS login (
                loginid INT(6) AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(50),
                password VARCHAR(12)
            )""",
            """
            CREATE TABLE IF NOT EXISTS carddetails (
                cardid INT(6) AUTO_INCREMENT PRIMARY KEY,
                userid INT(6),
                cardtype VARCHAR(50),
                cardno VARCHAR(16),
                expdate VARCHAR(5),
                cvv VARCHAR(3),
                FOREIGN KEY (userid) REFERENCES login(loginid)
            )""",
            """
            CREATE TABLE IF NOT EXISTS otptoken (
                otpid INT(6) AUTO_INCREMENT PRIMARY KEY,
                userid INT(6),
                otpvalue INT(12),
                exp_time TIME,
                timestamp TIMESTAMP,
                FOREIGN KEY (userid) REFERENCES login(loginid)
            )""",
            """
            CREATE TABLE IF NOT EXISTS transactiond (
                transid INT(6) AUTO_INCREMENT PRIMARY KEY,
                userid INT(6),
                tophone INT(10),
                transamt INT(3),
                cardid INT(6),
                status VARCHAR(50),
                paymethod VARCHAR(50),
                timestamp TIMESTAMP,
                FOREIGN KEY (userid) REFERENCES login(loginid),
                FOREIGN KEY (cardid) REFERENCES carddetails(cardid)
            )""",
            """
            CREATE TABLE IF NOT EXISTS walletd (
                walletid INT(6) AUTO_INCREMENT PRIMARY KEY,
                userid INT(6),
                balance FLOAT(4),
                createdat TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updatedat TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                FOREIGN KEY (userid) REFERENCES login(loginid)
            )""",
            """
            CREATE TABLE IF NOT EXISTS registration (
                registerid INT(6) AUTO_INCREMENT PRIMARY KEY,
                fn VARCHAR(50),
                ln VARCHAR(50),
                dob DATE,
                email VARCHAR(50),
                country VARCHAR(50),
                phn INT(10)
            )"""
        ]

        # Execute each table creation query
        for query in create_queries:
            cursor.execute(query)

        print("Tables created successfully!")

        # Commit changes and close cursor and connection
        connection.commit()
        cursor.close()
        connection.close()

    except mysql.connector.Error as error:
        print(f"Failed to create tables: {error}")

# Call the function to create tables
create_tables()

