# Tuples
cars = ("Limo","Range","Mercedes","Porsche","Nissan","Toyota")
print(cars[2])
for gari in cars:
    print(gari)

slicedCars = cars[0:4:-1][::-1]
for sG in slicedCars:
    print(sG)

# Lists
students = ["Samson","Chris","Emmanuel","Owen"]
students.append("Ted")
students.insert(1,"Mfalme")
# students.remove("Ted")
# students.pop(0)
# students[1] = "Mwangi"
# students[0],students[2] = students[2],students[0]
for student in students:
    print(student)
# Dictionaries
users = {"c@test.com":"Chris","e@test.com":"Emmanuel",
         "s@test.com":"Samson","o@test.com":"Owen"}
print(users["c@test.com"])

for user in users.values():
    print(user)

for user in users.keys():
    print(user)

