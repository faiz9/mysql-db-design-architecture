import os
# database.py
# Handles all the methods interacting with the database of the application.
# Students must implement their own methods here to meet the project requirements.

import pymysql.cursors

db_host = os.environ['DB_HOST']
db_username = os.environ['DB_USER']
db_password = os.environ['DB_PASSWORD']
db_name = os.environ['DB_NAME']
my_secret = os.environ['DISCORD_TOKEN']


def connect():
  try:
        conn = pymysql.connect(host=db_host,
                               port=3306,
                               user=db_username,
                               password=db_password,
                               db=db_name,
                               charset="utf8mb4", cursorclass=pymysql.cursors.DictCursor)
        print("Bot connected to database {}".format(db_name))
        return conn
  except:
      print("Bot failed to create a connection with your database because your secret environment variables " +
              "(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME) are not set".format(db_name))
      print("\n")

def handle_msg(msg):
     response = ""
     args = msg.split()
     command = args[0]
     param = ""
     for each in args:
        if each != command:
          param += each
          param += " "
          #rule1
        if command == "\find_appointment_payment_method<installment>":
          result = business_rule1(param)
        for each in result:
          toAppend = each['apptID'] + ", " + each['date'] + ", " + each['custID'] + ", " + each['type'] + ", " + each['amt'] +"\n"
          response += toAppend
          #rule2
        if command == "\names_customers<appointment>multiple<locations>":
          result = business_rule2(param)
        for each in result:
          toAppend = each['fname'] + ", " + each['lname'] + ", " + each['appointment'] + ", " + each['locID'] +"\n"
          response += toAppend
          #rule3
        if command == "\names_customers<dob >= 25>":
          result = business_rule3(param)
        for each in result:
          toAppend = each['customerID'] + ", " + each['fname'] + ", " + each['lname'] + ", " + each['floor'] +"\n"
          response += toAppend
          #rule6
        if command == "\nameemployees<salary >=1000><doh >= 3 years>":
          result = business_rule6(param)
        for each in result:
          toAppend = each['empID'] + ", " + each['fname'] + ", " + each['lname'] + ", " + each['doh'] +"," + each['salary'] + "\n"
          response += toAppend
          #rule 7
        if command == "\name_employees<senoirity>":
          result = business_rule7(param)
        for each in result:
          toAppend = each['fname'] + ", " + each['lname'] + ", " + each['doh']  + "\n"
          response += toAppend
          #rule10
        if command == "average-employee<salary><seniority>":
          result = business_rule10(param)
        for each in result:
          toAppend = each['doh'] + ", " + each['salary']  + "\n"
          response += toAppend
          #rule12
          if command == "\names_locations_address<owners>":
           result = business_rule12(param)
        for each in result:
          toAppend = each['name'] + ", " + each['city']  + each['fname'] 
          each['lname'] + each['ownerID'] + "\n"
          response += toAppend
          #rule13
          if command == "\names_customers<locationname>":
           result = business_rule13(param)
        for each in result:
          toAppend = each['name'] + ", " + each['city']  + each['fname'] 
          each['lname'] + each['ownerID'] + "\n"
          response += toAppend
          #rule14
          if command == "\revenue-stats":
           result = business_rule14(param)
        for each in result:
          toAppend = each['name'] + ", " + each['transaction']  + each['date'] + "\n"
          response += toAppend
          #rule15
          if command == "\appointment-stats":
           result = business_rule15(param)
        for each in result:
          toAppend = each['name'] + ", " + each['locID']  + each['date'] + "\n"
          response += toAppend
          #rule16
          if command == "\name_customer_highest_number_of_appointment":
           result = business_rule16(param)
        for each in result:
          toAppend = each['fname'] + ", " + each['lname']  + each['amt'] + "\n"
          response += toAppend
          #rule 17
          if command == "\name_customer_highest_number_of_payment":
           result = business_rule17(param)
        for each in result:
          toAppend = each['fname'] + ", " + each['lname']  + each['custID'] +  each['payment'] + each['amt'] + "\n"
          response += toAppend       
     else:
        response = "Unknown command"
     return response



def business_rule1(appID, paymentID, amt):
    conn = connect()
    cursor = conn.cursor()
    print(appID)
    print(paymentID)
    cursor.execute("""SELECT * FROM appointment JOIN payment ON 
     appointment.custID = payment.custID where amt > 100 AND type = 
     'installment';""")
    query_result = cursor.fetchall()
    cursor.close()
    return query_result

def business_rule2(fname, lname, appointment, locID):
    conn = connect()
    cursor = conn.cursor()
    print(fname)
    print(lname)
    print(appointment)
    print(locID)
    cursor.execute("""SELECT fname, lname from customer WHERE customerID IN 
(SELECT custID FROM appointment GROUP BY custID
HAVING COUNT(locID) = 1);""")
    query_result = cursor.fetchall()
    cursor.close()
    return query_result

def business_rule3(customerID, fname, lname, appointment, floor):
    conn = connect()
    cursor = conn.cursor()
    print(customerID)
    print(fname)
    print(lname)
    print(floor)
    cursor.execute("""SELECT customerID, fname, lname, Floor(datediff( curdate(), dob)/365) FROM customer WHERE
Floor(datediff( curdate(), dob)/365) > 25;""")
    query_result = cursor.fetchall()
    cursor.close()
    return query_result

def business_rule6(empID, fname, lname, doh, salary):
    conn = connect()
    cursor = conn.cursor()
    print(empID)
    print(fname)
    print(lname)
    print(doh)
    print(salary)
    cursor.execute("""SELECT empID, fname, lname, doh, salary from employees WHERE salary > 10000 
AND Floor(datediff( curdate(), doh)/365) > 3;""")
    query_result = cursor.fetchall()
    cursor.close()
    return query_result

def business_rule7( fname, lname, doh):
    conn = connect()
    cursor = conn.cursor()
    print(fname)
    print(lname)
    print(doh)
    cursor.execute("""SELECT fname, lname, doh from employees ORDER BY doh;""")
    query_result = cursor.fetchall()
    cursor.close()
    return query_result

def business_rule10(salary, doh):
    conn = connect()
    cursor = conn.cursor()
    print(doh)
    print(salary)
    cursor.execute("""SELECT AVG(salary), AVG(datediff( curdate(), doh)/365) FROM employees;""")
    query_result = cursor.fetchall()
    cursor.close()
    return query_result

def business_rule12(name, city, fname, lname, ownerID):
    conn = connect()
    cursor = conn.cursor()
    print(name)
    print(city)
    print(fname)
    print(lname)
    print(ownerID)
    cursor.execute("""SELECT name, city, fname, lname FROM location JOIN owner
ON location.owner_ownerID = owner.ownerID;""")
    query_result = cursor.fetchall()
    cursor.close()
    return query_result

def business_rule13(fname, lname, custID, locID, date):
    conn = connect()
    cursor = conn.cursor()
    print(fname)
    print(lname)
    print(custID)
    print(locID)
    print(date)
    cursor.execute("""SELECT fname, lname FROM customer WHERE customerID IN (SELECT custID FROM appointment GROUP BY custID HAVING COUNT(locID) = 1);""")
    query_result = cursor.fetchall()
    cursor.close()
    return query_result

def business_rule14(name, transaction, date):
    conn = connect()
    cursor = conn.cursor()
    print(name)
    print(transaction)
    print(date)
    cursor.execute("""SELECT name, sum(transaction) FROM location JOIN revenue
ON location.locationID = revenue.locID
GROUP BY name ORDER BY sum(transaction) DESC;""")
    query_result = cursor.fetchall()
    cursor.close()
    return query_result

def business_rule15(name, locID, date):
    conn = connect()
    cursor = conn.cursor()
    print(name)
    print(locID)
    print(date)
    cursor.execute("""SELECT name, COUNT(locID) FROM location JOIN appointment ON
location.locationID = appointment.locID GROUP BY
name ORDER BY COUNT(locID) DESC;""")
    query_result = cursor.fetchall()
    cursor.close()
    return query_result

def business_rule16(fname, lname, amt):
    conn = connect()
    cursor = conn.cursor()
    print(fname)
    print(lname)
    print(amt)
    cursor.execute("""SELECT fname, lname, COUNT(*) FROM customer JOIN appointment ON
appointment.custID = customer.customerID 
GROUP BY fname, lname
ORDER BY COUNT(*) DESC;""")
    query_result = cursor.fetchall()
    cursor.close()
    return query_result


def business_rule17(fname, lname, custID, payment, amt):
    conn = connect()
    cursor = conn.cursor()
    print(fname)
    print(lname)
    print(custID)
    print(payment)
    print(amt)
    cursor.execute("""SELECT fname, lname, SUM(amt)FROM customer JOIN payment
ON customer.customerID = payment.custID
GROUP BY fname, lname
ORDER BY SUM(amt) DESC;""")
    query_result = cursor.fetchall()
    cursor.close()
    return query_result
