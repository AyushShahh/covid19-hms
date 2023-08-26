import mysql.connector
# from faker import Faker
# import random


def db():
  return mysql.connector.connect(
    host="localhost",
    user="ayush",
    password="ayush@9104#!mysql",
    database="hms"
  )

def hospitals(mydb):
  with mydb.cursor() as db:
    db.execute('SELECT * FROM hospitals')
    return db.fetchall()
  
def people(mydb):
  with mydb.cursor() as db:
    db.execute('SELECT * FROM people')
    return db.fetchall()
  
def medicines(mydb):
  with mydb.cursor() as db:
    db.execute('SELECT * FROM medicines')
    return db.fetchall()
  
def laboratory(mydb):
  with mydb.cursor() as db:
    db.execute('SELECT * FROM laboratory')
    return db.fetchall()

# fake = Faker()

# insert_hospitals_query = """
# INSERT INTO hospitals (name, area, staff, total_nbed, ava_nbed, total_vbed, ava_vbed, oxygen_cylinders, nebulizers, phone_number, city)
# VALUES
#     ("zydus", "gota", 50, 100, 20, 20, 5, 150, 100, "+91 123456", "ahmedabad"),
#     ("civil", "shahibaug", 300, 500, 100, 200, 40, 350, 400, "+91 565656", "ahmedabad"),
#     ("sterling", "gurukul", 100, 200, 80, 88, 69, 30, 50, "+91 545362", "ahmedabad"),
#     ("vj", "dummas", 20, 100, 100, 20, 15, 150, 100, "+91 541532", "surat"),
#     ("nirmal hospital", "naranpura", 56, 300, 50, 100, 5, 43, 50, "+91 5132435", "surat"),
#     ("aditi hospital", "udhna", 50, 100, 20, 20, 5, 150, 100, "+91 545351", "surat")
# """

# cursor = mydb.cursor()
# cursor.execute(insert_hospitals_query)


# for _ in range(500):
#     name = fake.name().lower()
#     gender = random.choice(['male', 'female'])
#     age = random.randint(1, 100)
#     health_condition = random.choice(['mild', 'moderate', 'severe'])
#     city = random.choice(['ahmedabad', 'surat'])
#     area = fake.street_name().lower()
#     hospital = random.randint(1, 3) if city == 'ahmedabad' else random.randint(4, 6)
    
#     insert_query = "INSERT INTO people (name, gender, age, health_condition, city, area, hospital) " \
#                    "VALUES (%s, %s, %s, %s, %s, %s, %s)"
#     data = (name, gender, age, health_condition, city, area, hospital)
    
#     cursor.execute(insert_query, data)

# names = set(range(1, 501))
# for _ in range(40):
#     person = random.choice(list(names))
#     names.remove(person)
#     status = random.choice(['positive', 'negative', 'pending'])
#     city = random.choice(['ahmedabad', 'surat'])
#     name = fake.name().lower()
    
    
#     insert_query = "INSERT INTO laboratory (person, status, city, name) " \
#                    "VALUES (%s, %s, %s, %s)"
#     data = (person, status, city, name)
    
#     cursor.execute(insert_query, data)


# insert_medicines_query = """
# INSERT INTO medicines (name, city, stock)
# VALUES
#     ("covaxin", "ahmedabad", 10000),
#     ("covaxin", "surat", 9000),
#     ("covishield", "ahmedabad", 7000),
#     ("covishield", "surat", 2000),
#     ("remedivisir", "ahmedabad", 2000),
#     ("remedivisir", "surat", 800)
# """


# mydb.commit()
# cursor.execute('SELECT * FROM medicines')
# result = cursor.fetchall()
# for r in result:
#     print(r)
# cursor.close()
# mydb.close()