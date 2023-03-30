import itertools

students = [
  'TestStudent',
]

passwords = [
  'Testing42',
]
for (student, password) in zip(students, passwords):
    print("USE [LaborStatisticsDB]")
    print("GO")
    print("DROP USER " + student + ";")
    print("GO")
    print("USE [AdventureWorks2019]")
    print("GO")
    print("DROP USER " + student + ";")
    print("GO")
    print("USE [BooksDB]")
    print("GO")
    print("DROP USER " + student + ";")
    print("GO")
    print("USE [RideShareDB]")
    print("GO")
    print("DROP USER " + student + ";")
    print("GO")
    print("USE [master]")
    print("GO")
    print("DROP LOGIN " + student + ";")
    print("GO")
    