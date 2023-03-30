import itertools

students = [
  'TestStudent',
]

passwords = [
  'Testing42',
]
  
for (student, password) in zip(students, passwords):
  print("Your personal Azure Data Studio Login:")
  print("UserName = " + student)
  print("Password = " + password)
  print()
  print("Junk Database: JunkDB_KC")
  print("Schema name = " + student)
  print()
  print("-------------------------------------------------------")
  print()