import mysql.connector
from flask import  session
import datetime
# from login import loggedin_user
 
db_connection = mysql.connector.connect(
    # host="localhost",
    # user="sneha",  # Replace with your MySQL username
    # password="sneh@$123",  # Replace with your MySQL password
    # database="onlinepayment"  # Replace with your database name 
    host="localhost",  # Or use the IP address of your Docker container
    port=8001,         # Port you mapped when starting the container
    user="root",       # Root user by default
    password="12345",  # Password you set when starting the container
    database="mydb"    # Optional: specify the database you want to connect to
)


def register_user(fn,mail,ln,country,ph,dob):
    try:
        # Execute SQL query to insert user
        if db_connection.is_connected():
            print("Connected to MySQL database")
            cursor = db_connection.cursor()
            insert_register = "INSERT INTO registration (fn, email,ln,country,phone,dob) VALUES (%s, %s,%s, %s,%s, %s)"
            register_data = (fn,mail,ln,country,ph,dob)
            cursor.execute(insert_register, register_data)

        # Commit changes to the database
            db_connection.commit()
            print("Data added to register table successfully")

    except mysql.connector.Error as error:
        print("Error inserting data to registration:", error)

    finally:
        # Close the cursor and database connection
        if 'cursor' in locals():
            cursor.close()
        if 'db_connection' in locals() and db_connection.is_connected():
            db_connection.close()
            print("Database connection closed")


def insert_user(username, password,key,iv, user_key):
    try:
        # Check if the connection is successful
        if db_connection.is_connected():
            print("Connected to MySQL database")

            # Execute SQL query to insert user
            cursor = db_connection.cursor()
            
            insert_login = "INSERT INTO login (username, password,secretkey,iv,pwdkey) VALUES (%s, %s,%s,%s,%s)"
            login_data = (username, password,key,iv,user_key)
            cursor.execute(insert_login, login_data)

            # Commit changes to the database
            db_connection.commit()
            print("User inserted successfully")

    except mysql.connector.Error as error:
        print("Error inserting user:", error)

    finally:
        # Close the cursor and database connection
        if 'cursor' in locals():
            cursor.close()
        if 'db_connection' in locals() and db_connection.is_connected():
            db_connection.close()
            print("Database connection closed")
            
def card_details(cardtype,cardno,expdate,cvv, loggedin_user):	
    try:
        # Check if the connection is successful
        if db_connection.is_connected():
            print("Connected to MySQL database")

            # Execute SQL query to insert user
            cursor = db_connection.cursor()
            username = loggedin_user
            print("username ",username)
            
            insert_cardd = "INSERT INTO carddetails (userid, cardno,cardtype, expdate, cvv)VALUES ((SELECT loginid FROM login WHERE username = %s),%s,%s,%s,%s)"
            cardd_data = (username,cardno,cardtype,expdate,cvv)
            cursor.execute(insert_cardd, cardd_data)

            # Commit changes to the database
            db_connection.commit()
            print("User card details inserted successfully")

    except mysql.connector.Error as error:
        print("Error inserting user card details :", error)

    finally:
        # Close the cursor and database connection
        if 'cursor' in locals():
            cursor.close()
        if 'db_connection' in locals() and db_connection.is_connected():
            db_connection.close()
            print("Database connection closed")
            
                      
def login_user(username,pwd):
    try:

        # Check if the connection is successful
        if db_connection.is_connected():
            print("Connected to MySQL database")

            # Execute SQL query to insert user
            cursor = db_connection.cursor()
        
            query = "SELECT secretkey,iv,pwdkey FROM login WHERE username = %s AND password = %s"
            cursor.execute(query, (username, pwd))
            print("cursor ", cursor, pwd)
            # Fetch results
            result = cursor.fetchall()

            if result:
                print("User found in the database", result)
                return result
            else:
                print("User not found or invalid credentials", result)   

    except mysql.connector.Error as error:
        print("Error fetching user:", error)

    finally:
        # Close the cursor and database connection
        if 'cursor' in locals():
            cursor.close()
        if 'db_connection' in locals() and db_connection.is_connected():
            db_connection.close()
            print("Database connection closed")

def check_cvv(card_type, card_no,cvv,loggedin_user):
    try:
        # Check if the connection is successful
        if db_connection.is_connected():
            print("Connected to MySQL database")

            # Execute SQL query to insert user
            cursor = db_connection.cursor()
            username = loggedin_user
            print("username ",username,":",type(username))

            check_query = "SELECT c.cvv FROM login AS l JOIN carddetails AS c ON l.loginid = c.userid WHERE l.username =%s and c.cardno =%s and c.cardtype=%s"
            check_user_data=(username,card_no,card_type)
            cursor.execute(check_query, check_user_data)
            
            result = cursor.fetchone()
            
            print("result ",result," : ",type(result))
            if result is not None:
                if result[0] == cvv:
                    return cvv
                else:
                    print("CVV does not match.")
                    return None
            else:
                print("User not found.")

    except mysql.connector.Error as error:
        print("Error inserting user:", error)

    finally:
        # Close the cursor and database connection
        if 'cursor' in locals():
            cursor.close()
        if 'db_connection' in locals() and db_connection.is_connected():
            db_connection.close()
            print("Database connection closed")

def wallet(amt,loggedin_user):	
    try:
        # Check if the connection is successful
        if db_connection.is_connected():
            print("Connected to MySQL database")

            # Execute SQL query to insert user
            cursor = db_connection.cursor()
            username = loggedin_user
        
            current_timestamp = datetime.datetime.now()
            insert_amt = "INSERT INTO walletd (userid ,balance,createdat)VALUES ((SELECT loginid FROM login WHERE username = %s),%s,%s)"
            amt_data = (username,amt,current_timestamp)
            cursor.execute(insert_amt, amt_data)

            # Commit changes to the database
            db_connection.commit()
            print("Amount added to wallet successfully")

    except mysql.connector.Error as error:
        print("Error adding amount to wallet:", error)

    finally:
        # Close the cursor and database connection
        if 'cursor' in locals():
            cursor.close()
        if 'db_connection' in locals() and db_connection.is_connected():
            db_connection.close()
            print("Database connection closed")
            
            
def payment(tophone,card_no,transamt,loggedin_user):	
    try:
        # Check if the connection is successful
        if db_connection.is_connected():
            print("Connected to MySQL database")

            # Execute SQL query to insert user
            cursor = db_connection.cursor()
            username = loggedin_user

            current_timestamp = datetime.datetime.now()
            insert_pay = "INSERT INTO transaction (userid,cardid,tophone,transamt,status,paymethod,timestamp)VALUES ((SELECT loginid FROM login WHERE username = %s),(Select cardid from carddetails where cardno = %s),%s,%s,%s,%s,%s)"
            pay_data = (username,card_no,tophone,transamt,"Success","Offline",current_timestamp)
            cursor.execute(insert_pay, pay_data)

            # Commit changes to the database
            db_connection.commit()
            print("User inserted successfully")

    except mysql.connector.Error as error:
        print("Error inserting user:", error)

    finally:
        # Close the cursor and database connection
        if 'cursor' in locals():
            cursor.close()
        if 'db_connection' in locals() and db_connection.is_connected():
            db_connection.close()
            print("Database connection closed")
            
            
            
def transaction(loggedin_user):
        try:
            # Check if the connection is successful
            if db_connection.is_connected():
                print("Connected to MySQL database")

                # Execute SQL query to insert user
                cursor = db_connection.cursor()
                username = loggedin_user
                print("username ",username)
                
                SHOW_trans = "SELECT timestamp,tophone,paymethod,transamt FROM login AS l JOIN transaction AS t ON l.loginid = t.userid WHERE l.username = %s"
                trans_data = (username,)
                cursor.execute(SHOW_trans, trans_data)
                result = cursor.fetchall()
                
                print("result : ",result)
                print("User inserted successfully")
                return result

        except mysql.connector.Error as error:
            print("Error inserting user:", error)

        finally:
            # Close the cursor and database connection
            if 'cursor' in locals():
                cursor.close()
            if 'db_connection' in locals() and db_connection.is_connected():
                db_connection.close()
                print("Database connection closed")

def cards(cardtype,loggedin_user):
        try:
            # Check if the connection is successful
            if db_connection.is_connected():
                print("Connected to MySQL database")

                # Execute SQL query to insert user
                cursor = db_connection.cursor()
                username = loggedin_user
                print("username ",username)
                
                SHOW_trans = "SELECT c.cardno FROM login AS l JOIN carddetails AS c ON l.loginid = c.userid WHERE l.username = %s and c.cardtype=%s"
                trans_data = (username,cardtype)
                cursor.execute(SHOW_trans, trans_data)
                result = cursor.fetchall()
                
                print("result : ",result)
            
                print("Data fetched")
                return result

        except mysql.connector.Error as error:
            print("Error inserting user:", error)

        finally:
            # Close the cursor and database connection
            if 'cursor' in locals():
                cursor.close()
            if 'db_connection' in locals() and db_connection.is_connected():
                db_connection.close()
                print("Database connection closed")

def close_connection(self):
    if self.is_connected():
        self.close()
        print("Database connection closed")

# import mysql.connector
# from flask import  session
# import datetime
# # from login import loggedin_user
 
# db_connection = mysql.connector.connect(
#     host="localhost",  # Or use the IP address of your Docker container
#     port=8001,         # Port you mapped when starting the container
#     user="root",       # Root user by default
#     password="12345",  # Password you set when starting the container
#     database="mydb"    # Optional: specify the database you want to connect to
# )


# def register_user(fn,mail,ln,country,ph,dob):
#     try:
#         # Execute SQL query to insert user
#         if db_connection.is_connected():
#             print("Connected to MySQL database")
#             cursor = db_connection.cursor()
#             insert_register = "INSERT INTO registration (fn, email,ln,country,phone,dob) VALUES (%s, %s,%s, %s,%s, %s)"
#             register_data = (fn,mail,ln,country,ph,dob)
#             cursor.execute(insert_register, register_data)
        
#         # insert_login = "INSERT INTO login (username, password) VALUES (%s, %s)"
#         # login_data = (name, password)
#         # cursor.execute(insert_login, login_data)

#         # Commit changes to the database
#             db_connection.commit()
#             print("User inserted successfully")

#     except mysql.connector.Error as error:
#         print("Error inserting user:", error)

#     finally:
#         # Close the cursor and database connection
#         if 'cursor' in locals():
#             cursor.close()
#         if 'db_connection' in locals() and db_connection.is_connected():
#             db_connection.close()
#             print("Database connection closed")


# def insert_user(username, password,key,iv, user_key):
#     try:
#         # Check if the connection is successful
#         if db_connection.is_connected():
#             print("Connected to MySQL database")

#             # Execute SQL query to insert user
#             cursor = db_connection.cursor()
            
#             insert_login = "INSERT INTO login (username, password,secretkey,iv,pwdkey) VALUES (%s, %s,%s,%s,%s)"
#             login_data = (username, password,key,iv,user_key)
#             cursor.execute(insert_login, login_data)

#             # Commit changes to the database
#             db_connection.commit()
#             print("User inserted successfully")

#     except mysql.connector.Error as error:
#         print("Error inserting user:", error)

#     finally:
#         # Close the cursor and database connection
#         if 'cursor' in locals():
#             cursor.close()
#         if 'db_connection' in locals() and db_connection.is_connected():
#             db_connection.close()
#             print("Database connection closed")
            
# def card_details(cardtype,cardno,expdate,cvv, loggedin_user):
# # cardtype	cardno	expmonth	expyear	cvv	
#     try:
#         # Check if the connection is successful
#         if db_connection.is_connected():
#             print("Connected to MySQL database")

#             # Execute SQL query to insert user
#             cursor = db_connection.cursor()
#             username = loggedin_user
#             print("username ",username)
            
            
#             # insert_cardd = "INSERT INTO carddetails (userid,cardno,expdate,cvv) VALUES (%s,%s, %s,%s)"
            
#             insert_cardd = "INSERT INTO carddetails (userid, cardno,cardtype, expdate, cvv)VALUES ((SELECT loginid FROM login WHERE username = %s),%s,%s,%s,%s)"
#             cardd_data = (username,cardno,cardtype,expdate,cvv)
#             cursor.execute(insert_cardd, cardd_data)

#             # Commit changes to the database
#             db_connection.commit()
#             print("User inserted successfully")

#     except mysql.connector.Error as error:
#         print("Error inserting user:", error)

#     finally:
#         # Close the cursor and database connection
#         if 'cursor' in locals():
#             cursor.close()
#         if 'db_connection' in locals() and db_connection.is_connected():
#             db_connection.close()
#             print("Database connection closed")
            
                      
# def login_user(username,pwd):
# # cardtype	cardno	expmonth	expyear	cvv	
#     try:

#         # Check if the connection is successful
#         if db_connection.is_connected():
#             print("Connected to MySQL database")

#             # Execute SQL query to insert user
#             cursor = db_connection.cursor()
        
#             query = "SELECT secretkey,iv,pwdkey FROM login WHERE username = %s AND password = %s"
#             cursor.execute(query, (username, pwd))
#             print("cursor ", cursor, pwd)
#             # Fetch results
#             result = cursor.fetchall()

#             if result:
#                 print("User found in the database", result)
#                 return result
#             else:
#                 print("User not found or invalid credentials", result)   

#     except mysql.connector.Error as error:
#         print("Error fetching user:", error)

#     finally:
#         # Close the cursor and database connection
#         if 'cursor' in locals():
#             cursor.close()
#         if 'db_connection' in locals() and db_connection.is_connected():
#             db_connection.close()
#             print("Database connection closed")

# def check_cvv(card_type, card_no,cvv,loggedin_user):
#     try:
#         # Check if the connection is successful
#         if db_connection.is_connected():
#             print("Connected to MySQL database")

#             # Execute SQL query to insert user
#             cursor = db_connection.cursor()
#             username = loggedin_user
#             print("username ",username,":",type(username))
#             check_query = "SELECT c.cvv FROM login AS l JOIN carddetails AS c ON l.loginid = c.userid WHERE l.username =%s and c.cardno =%s and c.cardtype=%s"
#             check_user_data=(username,card_no,card_type)
#             cursor.execute(check_query, check_user_data)
#             print("cursor ",cursor)
#             result = cursor.fetchone()
            
#             print("result ",result," : ",type(result))
#             if result is not None:
#                 if result[0] == cvv:
#                     return cvv
#                 else:
#                     print("CVV does not match.")
#                     return None
#             else:
#                 print("User not found.")

#     except mysql.connector.Error as error:
#         print("Error inserting user:", error)

#     finally:
#         # Close the cursor and database connection
#         if 'cursor' in locals():
#             cursor.close()
#         if 'db_connection' in locals() and db_connection.is_connected():
#             db_connection.close()
#             print("Database connection closed")

# def wallet(amt,loggedin_user):
# # cardtype	cardno	expmonth	expyear	cvv	
#     try:
#         # Check if the connection is successful
#         if db_connection.is_connected():
#             print("Connected to MySQL database")

#             # Execute SQL query to insert user
#             cursor = db_connection.cursor()
#             username = loggedin_user
        
#             # insert_cardd = "INSERT INTO carddetails (userid,cardno,expdate,cvv) VALUES (%s,%s, %s,%s)"
#             current_timestamp = datetime.datetime.now()
#             insert_amt = "INSERT INTO walletd (userid ,balance,createdat)VALUES ((SELECT loginid FROM login WHERE username = %s),%s,%s)"
#             amt_data = (username,amt,current_timestamp)
#             cursor.execute(insert_amt, amt_data)

#             # Commit changes to the database
#             db_connection.commit()
#             print("User inserted successfully")

#     except mysql.connector.Error as error:
#         print("Error inserting user:", error)

#     finally:
#         # Close the cursor and database connection
#         if 'cursor' in locals():
#             cursor.close()
#         if 'db_connection' in locals() and db_connection.is_connected():
#             db_connection.close()
#             print("Database connection closed")
            
            
# def payment(tophone,card_no,transamt,loggedin_user):
# # cardtype	cardno	expmonth	expyear	cvv	
#     try:
#         # Check if the connection is successful
#         if db_connection.is_connected():
#             print("Connected to MySQL database")

#             # Execute SQL query to insert user
#             cursor = db_connection.cursor()
#             username = loggedin_user
                    
#             # insert_cardd = "INSERT INTO carddetails (userid,cardno,expdate,cvv) VALUES (%s,%s, %s,%s)"
#             current_timestamp = datetime.datetime.now()
#             insert_pay = "INSERT INTO transactiond (userid,cardid,tophone,transamt,status,paymethod,timestamp)VALUES ((SELECT loginid FROM login WHERE username = %s),(Select cardid from carddetails where cardno = %s),%s,%s,%s,%s,%s)"
#             pay_data = (username,card_no,tophone,transamt,"Success","Offline",current_timestamp)
#             cursor.execute(insert_pay, pay_data)

#             # Commit changes to the database
#             db_connection.commit()
#             print("User inserted successfully")

#     except mysql.connector.Error as error:
#         print("Error inserting user:", error)

#     finally:
#         # Close the cursor and database connection
#         if 'cursor' in locals():
#             cursor.close()
#         if 'db_connection' in locals() and db_connection.is_connected():
#             db_connection.close()
#             print("Database connection closed")
            
            
            
# def transaction(loggedin_user):
# # cardtype	cardno	expmonth	expyear	cvv	
#         try:
#             # Check if the connection is successful
#             if db_connection.is_connected():
#                 print("Connected to MySQL database")

#                 # Execute SQL query to insert user
#                 cursor = db_connection.cursor()
#                 username = loggedin_user
#                 print("username ",username)
                
#                 SHOW_trans = "SELECT timestamp,tophone,paymethod,transamt FROM login AS l JOIN transactiond AS t ON l.loginid = t.userid WHERE l.username = %s"
#                 trans_data = (username,)
#                 cursor.execute(SHOW_trans, trans_data)
#                 result = cursor.fetchall()
                
#                 # result = cursor.fetchall()
                
#                 print("result : ",result)
            

#                 # Commit changes to the database
#                 print("User inserted successfully")
#                 return result

#         except mysql.connector.Error as error:
#             print("Error inserting user:", error)

#         finally:
#             # Close the cursor and database connection
#             if 'cursor' in locals():
#                 cursor.close()
#             if 'db_connection' in locals() and db_connection.is_connected():
#                 db_connection.close()
#                 print("Database connection closed")

# def cards(cardtype,loggedin_user):
# # cardtype	cardno	expmonth	expyear	cvv	
#         try:
#             # Check if the connection is successful
#             if db_connection.is_connected():
#                 print("Connected to MySQL database")

#                 # Execute SQL query to insert user
#                 cursor = db_connection.cursor()
#                 username = loggedin_user
#                 print("username ",username)
                
#                 SHOW_trans = "SELECT c.cardno FROM login AS l JOIN carddetails AS c ON l.loginid = c.userid WHERE l.username = %s and c.cardtype=%s"
#                 trans_data = (username,cardtype)
#                 cursor.execute(SHOW_trans, trans_data)
#                 result = cursor.fetchall()
                
#                 # result = cursor.fetchall()
                
#                 print("result : ",result)
            

#                 # Commit changes to the database
#                 print("Data fetched")
#                 return result

#         except mysql.connector.Error as error:
#             print("Error inserting user:", error)

#         finally:
#             # Close the cursor and database connection
#             if 'cursor' in locals():
#                 cursor.close()
#             if 'db_connection' in locals() and db_connection.is_connected():
#                 db_connection.close()
#                 print("Database connection closed")

# def close_connection(self):
#     if self.is_connected():
#         self.close()
#         print("Database connection closed")