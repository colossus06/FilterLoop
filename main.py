# Write a simple program to filter the results
#We can use an if statement in the for loop to catch the thing we are looking for.
import time
num = [5,78,101,55,47]
print("This is a simple program to filter the results")
print("Here comes the numbers: ",num)
answer= input("Do you want to see which of them are higher than 50? yes/no ...")

if answer == "yes":
  time.sleep(1)
  for value in num:
    if value>50:
      print(value)
  print("Now you got all the numbers.")
time.sleep(2)
print("Ok, come back if you want to know, bye...")