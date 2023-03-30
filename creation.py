import itertools

students = [
  'TestStudent',
]

passwords = [
  'Testing42',
]
for (student, password) in zip(students, passwords):
  print("USE master")
  print("CREATE LOGIN " + student)
  print("WITH PASSWORD = '" + password + "';")
  print("GO")
  print("USE [LaborStatisticsDB]")
  print("CREATE USER " + student + " FOR LOGIN " + student + ";")
  print("GO")
  print("USE [LaborStatisticsDB]")
  print("GO")
  print("ALTER ROLE [db_datareader] ADD MEMBER [" + student + "]")
  print("GO")
  print("USE [AdventureWorks2019]")
  print("GO")
  print("CREATE USER " + student + " FOR LOGIN " + student + ";")
  print("GO")
  print("USE [AdventureWorks2019]")
  print("GO")
  print("ALTER ROLE [db_datareader] ADD MEMBER [" + student + "]")
  print("GO")
  print("USE [BooksDB]")
  print("GO")
  print("CREATE USER " + student + " FOR LOGIN " + student + ";")
  print("GO")
  print("USE [BooksDB]")
  print("GO")
  print("ALTER ROLE [db_datareader] ADD MEMBER [" + student + "]")
  print("GO")
  print("USE [RideShareDB]")
  print("GO")
  print("CREATE USER " + student + " FOR LOGIN " + student + ";")
  print("GO")
  print("USE [RideShareDB]")
  print("GO")
  print("ALTER ROLE [db_datareader] ADD MEMBER [" + student + "]")
  print("GO")
  print("USE [JunkDB]")
  print("GO")
  print("CREATE USER " + student + " FOR LOGIN " + student + ";")
  print("GO")
  print("USE [JunkDB]")
  print("GRANT CREATE TABLE TO " + student + ";")
  print("GRANT CREATE PROCEDURE TO " + student + ";")
  print("GRANT CREATE VIEW TO " + student + ";")
  print("GRANT CREATE FUNCTION TO " + student + ";")
  print("GO")
  print("USE [JunkDB]")
  print("GO")
  print("CREATE SCHEMA " + student + " AUTHORIZATION " + student)
  print("GO")
  print()
  print()