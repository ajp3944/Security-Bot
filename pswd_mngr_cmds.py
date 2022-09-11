'''
Executes commands to be sent to password manager database
'''
import mysql.connector

mysqlUsername = "poncho"
localhost = "localhost"
mysqlPassword = "whatsaponcho"
databaseName = "pswd_mngr_database"
userID = 3484324
userPassword = "feaf"

#establishing the connection
connection = mysql.connector.connect(
    host=localhost, user=mysqlUsername, passwd=mysqlPassword, database=databaseName)

#Creating a cursor object using the cursor() method
cursor = connection.cursor()

def main():
    print("here")
    statement = "CREATE USER 'poncho'@'localhost' IDENTIFIED BY 'whatsaponcho'"
    show_statement = "SELECT Host, User FROM mysql.user WHERE User='poncho';"
    try:
        cursor.execute(show_statement)
        cursor.execute(statement)
    except:
        connection.rollback()   # Rolling back in case of error
    
    insert_to_loginInfo(userID, userPassword, databaseName)
    close_connection()
main()

# Closes connection to mysql
def close_connection():
    connection.close()


def insert_to_loginInfo(userID, usernameLogin, userPassword):
    # Preparing SQL query to INSERT a record into login information table.
        insert_into_loginInfo = (
        "INSERT INTO loginInfo(userID, username, userPassword)"
        "VALUES (%s, %s, %s)"
        )
        data = (userID, usernameLogin, userPassword)

        # Execute command and close connection
        try:
            cursor.execute(insert_into_loginInfo, data)
            connection.commit()     # Commit your changes in the database
        except:
            connection.rollback()   # Rolling back in case of error

def delete_user_from_loginInfo(userID):
    sql_delete = "DELETE FROM loginInfo WHERE userID = %s"
    sql_data = (userID,)

    # Delete from relation table
    sql_delete_other = "DELETE FROM userAppRelation WHERE userID = %s"
    sql_data_other = (userID,)

    # Execute command, rollback if failure
    try:
        cursor.execute(sql_delete, sql_data)
        connection.commit()
        cursor.execute(sql_delete_other, sql_data_other)
        connection.commit()
    except:
        connection.rollback()

# Add username/password of an application or site
def insert_to_applicationList(applicationName, appUsername, appPassword):
    # Preparing SQL query to INSERT a record into application/site information table.
        insert_into_applicationList = (
        "INSERT INTO applicationList(applicationName, appUsername, appPassword)"
        "VALUES (%s, %s, %s)"
        )
        data = (applicationName, appUsername, appPassword)

        # Execute command and close connection
        try:
            cursor.execute(insert_into_applicationList, data)
            connection.commit()     # Commit changes in the database
        except:
            connection.rollback()   # Rollback in case of error

def delete_user_from_applicationList(applicationName):
    sql_delete = "DELETE FROM applicationList WHERE applicationName = %s"
    sql_data = (applicationName,)

    # Delete from relation table
    sql_delete_other = "DELETE FROM userAppRelation WHERE applicationName = %s"
    sql_data_other = (applicationName,)

    # Execute command, rollback if failure
    try:
        cursor.execute(sql_delete, sql_data)
        connection.commit()
        cursor.execute(sql_delete_other, sql_data_other)
        connection.commit()
    except:
        connection.rollback()

# Adds info from other two tables
def insert_to_userAppRelation(userAppID, userID, applicationName):
    # Preparing SQL query to INSERT a record into application/site information table.
        insert_into_userAppRelation = (
        "INSERT INTO userAppRelation(userAppID, userID, applicationName)"
        "VALUES (%s, %s, %s)"
        )
        data = (userAppID, userID, applicationName)

        # Execute command and close connection
        try:
            cursor.execute(insert_into_userAppRelation, data)
            connection.commit()     # Commit changes in the database
        except:
            connection.rollback()   # Rollback in case of error

# Remove info from editing other two tables
def delete_user_from_userAppRelation(userAppID):
    sql_delete = "DELETE FROM applicationList WHERE applicationName = %s"
    sql_data = (userAppID,)

    # Execute command, rollback if failure
    try:
        cursor.execute(sql_delete, sql_data)
        connection.commit()
    except:
        connection.rollback()

# Returns a string of information from applicationList table
def query_applicationList():
    sql_select_Query = "SELECT * FROM applicationList"
    cursor.execute(sql_select_Query)

    # get all records
    records = cursor.fetchall()

    string_info = ""
    for row in records:
        string_info += ("{", "Application Name: ", row[0]) + (", Application Username: ", row[1])
        + (", Application Password: ", row[2], "}")
    return string_info

# Returns a string of information from userAppRelation table
def query_userAppRelation():
    sql_select_Query = "SELECT * FROM userAppRelation"
    cursor.execute(sql_select_Query)

    # get all records
    records = cursor.fetchall()

    string_info = ""
    for row in records:
        string_info += ("{", "User Application ID: ", row[0]) + (", User Login ID: ", row[1])
        + (", Application Name: ", row[2], "}")
    return string_info