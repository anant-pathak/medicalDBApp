import psycopg2





def choice(connectionObj):

    while True:
        choice_text = {
            1: "In which state a particular hospital is located?",
            2: "Which hospitals are specialised in particular department",
            3: "What are the specializations of a particular hospital?",
            4: "What is the rating of a particular hospital?",
            5: "List all the hospitals that provide emergency services in a particular zip.",
            6: "List top 10 rated hospitals in a particular zip? ",
            7: "How many hospitals are there in each zip which provides emergency services and have rating > 3.",
            8: "What is the per year patient count of the hospital and "
               "arrange from maximum to minimum patients visited?",
            9: "List all specialities that Hospitals treat.",
            10: "List all general diseases.",
            11: "Which is the most visited department of a hospital?",
            12: "List all hospitals in the order of average expense? ",
            13: "List all specialities of one particular hospital and their HODs:",
            14: "Exit",
        }
        for eachChoice in choice_text:
            print(eachChoice, choice_text[eachChoice])
        x = input("Enter  a number from the above: ")
        x = x.strip()
        if not x.isnumeric():
            print("Plz enter only the number in range")
            continue
        if int(x) == 14:
            break
        choice_def[int(x)](connectionObj)
        yesAndNo = input("Show menu again? y | n : ")
        if yesAndNo == 'n':
            break




def query1(connectionObj):
    cursor = connectionObj.cursor()
    x = input("enter hospital name : ")
    query = "Select location.state " \
             "From location NATURAL JOIN hospital NATURAL JOIN Hospital_Location_rel " \
             "Where hospital.hname= %s;"
    # query = "Select * From hospital Where hospital.hname= 'YUMA REGIONAL MEDICAL CENTER';"
    try:
        cursor.execute(query, (x,))
    except Exception as e:
        print('Error! Code: {c}, Message, {m}'.format(c=type(e).__name__, m=str(e)))
    col_names = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    print(col_names)
    for row in rows:
        print(row)
    cursor.close()

def query2(connectionObj):
    cursor = connectionObj.cursor()
    x = input("enter speciality : ")
    query = "Select hospital.hname AS Hospital_Name " \
            "From hospital NATURAL JOIN doctor " \
            "Where speciality=%s;"
    try:
        cursor.execute(query, (x,))
    except Exception as e:
        print('Error! Code: {c}, Message, {m}'.format(c=type(e).__name__, m=str(e)))
    col_names = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    print(col_names)
    for row in rows:
        print(row)
    cursor.close()

def query3(connectionObj):
    cursor = connectionObj.cursor()
    x = input("enter hospital name : ")
    query = "Select DISTINCT(speciality) " \
            "From hospital NATURAL JOIN doctor " \
            "Where hospital.hname= %s;"
    try:
        cursor.execute(query, (x,))
    except Exception as e:
        print('Error! Code: {c}, Message, {m}'.format(c=type(e).__name__, m=str(e)))
    col_names = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    print(col_names)
    for row in rows:
        print(row)
    cursor.close()


def query4(connectionObj):
    cursor = connectionObj.cursor()
    x = input("enter hospital name : ")
    query = "Select hrating " \
            "From hospital " \
            "Where hname= %s;"
    try:
        cursor.execute(query, (x,))
    except Exception as e:
        print('Error! Code: {c}, Message, {m}'.format(c=type(e).__name__, m=str(e)))
    col_names = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    print(col_names)
    for row in rows:
        print(row)
    cursor.close()

def query5(connectionObj):
    cursor = connectionObj.cursor()
    x = int(input("enter zip code : "))
    query = "Select hospital.hname " \
            "From hospital NATURAL JOIN hospital_location_rel " \
            "Where hospital.emergency='TRUE' AND hospital_location_rel.zip=%s;"
    try:
        cursor.execute(query, (x,))
    except Exception as e:
        print('Error! Code: {c}, Message, {m}'.format(c=type(e).__name__, m=str(e)))
    col_names = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    print(col_names)
    for row in rows:
        print(row)
    cursor.close()

def query6(connectionObj):
    cursor = connectionObj.cursor()
    x = int(input("enter zip code : "))
    query = "Select hospital.hname, hospital.hrating " \
            "From hospital NATURAL JOIN hospital_location_rel " \
            "Where hospital_location_rel.zip= %s " \
            "ORDER BY hospital.hrating "
    try:
        cursor.execute(query, (x,))
    except Exception as e:
        print('Error! Code: {c}, Message, {m}'.format(c=type(e).__name__, m=str(e)))
    col_names = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    print(col_names)
    for row in rows:
        print(row)
    cursor.close()

def query7(connectionObj):
    cursor = connectionObj.cursor()
    query = "Select zip, count(hid) " \
            "From hospital NATURAL JOIN hospital_location_rel " \
            "Where hospital.hrating >'3' AND hospital.emergency = 'TRUE' " \
            "GROUP BY zip  " \
            "ORDER BY count(hid) desc "
    try:
        cursor.execute(query)
    except Exception as e:
        print('Error! Code: {c}, Message, {m}'.format(c=type(e).__name__, m=str(e)))
    col_names = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    print(col_names)
    for row in rows:
        print(row)
    cursor.close()

def query8(connectionObj):
    cursor = connectionObj.cursor()
    query = "Select hid, sum(visitors_count) " \
            "From hospital_disease_visitors_rel " \
            "Group by hid " \
            "Order by SUM(visitors_count) desc "
    try:
        cursor.execute(query)
    except Exception as e:
        print('Error! Code: {c}, Message, {m}'.format(c=type(e).__name__, m=str(e)))
    col_names = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    print(col_names)
    for row in rows:
        print(row)
    cursor.close()

def query9(connectionObj):
    cursor = connectionObj.cursor()
    query = "Select distinct doctor.speciality " \
            "From doctor, hospital " \
            "Where doctor.hid=hospital.hid; "
    try:
        cursor.execute(query, )
    except Exception as e:
        print('Error! Code: {c}, Message, {m}'.format(c=type(e).__name__, m=str(e)))
    col_names = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    print(col_names)
    for row in rows:
        print(row)
    cursor.close()

def query10(connectionObj):
    cursor = connectionObj.cursor()
    query = "Select * " \
            "From disease_type; "
    try:
        cursor.execute(query, )
    except Exception as e:
        print('Error! Code: {c}, Message, {m}'.format(c=type(e).__name__, m=str(e)))
    col_names = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    print(col_names)
    for row in rows:
        print(row)
    cursor.close()

def query11(connectionObj):
    cursor = connectionObj.cursor()
    query = "SELECT V.hid, V.dname, V.visitors_count " \
            "FROM hospital_disease_visitors_rel as V , (SELECT hid, MAX(visitors_count) as vcount " \
                                                        "FROM hospital_disease_visitors_rel " \
                                                          "GROUP BY hid) as G " \
            "WHERE G.hid = V.hid and G.vcount = V.visitors_count  and V.visitors_count > 0; "
    try:
        cursor.execute(query)
    except Exception as e:
        print('Error! Code: {c}, Message, {m}'.format(c=type(e).__name__, m=str(e)))
    col_names = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    print(col_names)
    for row in rows:
        print(row)
    cursor.close()

def query12(connectionObj):
    cursor = connectionObj.cursor()
    query = "Select hid, avg(payment) AS expense " \
            "From measure_hospital_rel " \
            "Group by hid " \
            "Order by expense desc;"
    try:
        cursor.execute(query, )
    except Exception as e:
        print('Error! Code: {c}, Message, {m}'.format(c=type(e).__name__, m=str(e)))
    col_names = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    print(col_names)
    for row in rows:
        try:
            expense = int(row[1])
        except:
            expense = 0
            pass
        print(row[0], " $", expense)
    cursor.close()

def query13(connectionObj):
    cursor = connectionObj.cursor()
    x = input("Enter hospital id: ")
    query = "Select distinct doctor.speciality, doctor.dname, doctor.credential " \
            "From doctor NATURAL JOIN hospital " \
            "Where hid = %s ; "
    try:
        cursor.execute(query, (x,))
    except Exception as e:
        print('Error! Code: {c}, Message, {m}'.format(c=type(e).__name__, m=str(e)))
    col_names = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    print(col_names)
    for row in rows:
        print("Speciality: ", row[0], " --HOD: ", row[1], " | ", row[2])
    cursor.close()


# def query8(connectionObj):
#     cursor = connectionObj.cursor()
#     x = input("enter hospital name : ")
#     query = "Select DISTINCT(speciality) " \
#             "From hospital NATURAL JOIN doctor " \
#             "Where hospital.hname= %s;"
#     cursor.execute(query, (x,))
#     try:
#         cursor.execute(query, (x,))
#     except Exception as e:
#         print('Error! Code: {c}, Message, {m}'.format(c=type(e).__name__, m=str(e)))
#     col_names = [desc[0] for desc in cursor.description]
#     rows = cursor.fetchall()
#     print(col_names)
#     for row in rows:
#         print(row)
#     cursor.close()
#
# def query9(connectionObj):
#     cursor = connectionObj.cursor()
#     x = input("enter hospital name : ")
#     query = "Select DISTINCT(speciality) " \
#             "From hospital NATURAL JOIN doctor " \
#             "Where hospital.hname= %s;"
#     cursor.execute(query, (x,))
#     try:
#         cursor.execute(query, (x,))
#     except Exception as e:
#         print('Error! Code: {c}, Message, {m}'.format(c=type(e).__name__, m=str(e)))
#     col_names = [desc[0] for desc in cursor.description]
#     rows = cursor.fetchall()
#     print(col_names)
#     for row in rows:
#         print(row)
#     cursor.close()
#
# def query10(connectionObj):
#     cursor = connectionObj.cursor()
#     x = input("enter hospital name : ")
#     query = "Select DISTINCT(speciality) " \
#             "From hospital NATURAL JOIN doctor " \
#             "Where hospital.hname= %s;"
#     cursor.execute(query, (x,))
#     try:
#         cursor.execute(query, (x,))
#     except Exception as e:
#         print('Error! Code: {c}, Message, {m}'.format(c=type(e).__name__, m=str(e)))
#     col_names = [desc[0] for desc in cursor.description]
#     rows = cursor.fetchall()
#     print(col_names)
#     for row in rows:
#         print(row)
#     cursor.close()




choice_def = {
        1: query1,
        2: query2,
        3: query3,
        4: query4,
        5: query5,
        6: query6,
        7: query7,
        8: query8,
        9: query9,
        10: query10,
        11: query11,
        12: query12,
        13: query13,
    }


