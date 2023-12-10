import time

applicant = []
email = [ ]

print ("Hello, Welcome to our software engineer interview! Thank you for joining us. ")

print(" ")
time.sleep(1)

job = input("Are you looking for a job position as a software engineer? ")

if job.lower() == "yes":
  print(" ")
  print("Excellent! ")
elif job.lower() == "no":
  print("Unfortunately we aren't hiring for any other position.")
  print(" ")
  stay = input( "Do you want to continue this interview? ")
  if stay == "Yes" or stay == "yes" or stay == "yea": 
    print("Great!")
  elif stay.lower() == "no":
    time.sleep(1)
    print("")
    print("Thank you for coming in. You can leave now.")
    exit()
  else: 
    print( "We will continue the interview!")
else: 
  print("")
  print("Thank you for coming today. Hopefully you will be interested! ")

name = input( "Please type in your name: ")
print("Nice to meet you", name, ".")
time.sleep(1)
print("We will now begin the interview. Please answer the following questions.")
print(" ")

age = int(input("How old are you? Please enter a number:  "))
if age > 55:
  print(" ")
  print("Sorry, unfortunately you aren't in the age range that we are looking for. Thank you for coming in. ")
  exit()
elif age >= 22 :
  print("")
  print("Great, you meet the age requirement for this job!") 
else:
  print(" ")
  print( "Sorry, you don't meet the age requirement for this job.  Hopefully we can see you in the future!")
  exit()

print("")
time.sleep(1)
degree = input( "Do you have a bachelor's degree or any certification in the technology field? ")

if degree.lower() == "yes":
  print("Good! We are looking for someone who is certified.")
elif degree.lower() == "no":
  print("Sorry, we are looking for someone who is certified. Thank you for coming in. ")
  exit()
else:
  print("This isn't a valid answer. Thank you for coming in.")
  exit()
  

time.sleep(1)
print("")
platform = input("Are you familiar with the following programming languages : JavaScript, HTML/CSS, Python? Please enter 'yes' or 'no': ")

print(" ")
time.sleep(1)
portfolio = input("Do you have a portfolio of your past projects that you can share with us? ")

if platform.lower() == "yes" and portfolio.lower() == "yes":
 print(" ")
 print("Excellent! These languages are vital for this job. It's always good to have a portfolio as well. ")
  
elif platform.lower() == "yes" and portfolio.lower() == "no":
 time.sleep(1)
 print("")
 print("Sorry, having a portfolio is required for this job. Thank you for coming, it was nice to meet you.")
 exit()

elif platform.lower() == "no" and portfolio.lower()== "yes":
 print(" ")
 time.sleep(1)
 print("It's good that you have a portfolio. Unfortunately, we need someone who knows these programming languages. Thank you for coming in.")
 exit()

else:
 time.sleep(1)
 print()
 print("Sorry, you don't seem to have the skills that are required for this job. Thank you for coming in.")
 exit()

time.sleep(1)
print(" ")
group= input("Do you like working in groups? ")
if group.lower() == "yes" or group.lower() == "yea":
  print("Great, we are looking for someone who is able to work and communicate with others. ")

elif group.lower() == "no":
  print("")
  print("Sorry, we are looking for someone who is able to work and communicate with others. Thank you for coming in.")
  exit()
else:
  print("Sorry, we are looking for someone who is able to work and communicate with others. Thank you for coming in") 
  exit()
  
print(" ")

time.sleep(2)
print("We will now begin the coding part of this interview. You'll be shown 2 codes and will be asked 3 questions in total. You must answer all questions correctly.")

print("")
time.sleep(3)
print("Here is question one. The code is written in Python.")
time.sleep(2)
print(" ")
print(" ' x = 6 , y = 7 ,  print = (x >= y) ' " )

question = input("What would print after writing this code? " )

if question.lower() == "true":
  print("Sorry, that answer is incorrect. Thank you for coming in.")
  exit()

elif question.lower() == "false":
  print("Correct!!")

else:
  print(" ")
  print("That is incorrect. Thank you for coming in, you can see yourself out.")
  exit()

print("")
time.sleep(1)

print("Next question. Read the following code. This is also written in Python.")
time.sleep(2)
print(" ")
print(" number = input (What month number is December?)  ")

time.sleep(1)
print("")
questiontwo = input("In order to make the code run, what needs to be added? Please spell it out ")
if questiontwo.lower() == "quote" or questiontwo.lower()== "quotes":
   print(" ")
   print("Correct. Great Job.")
else:
 print("Wrong :(")
 print("Unfortunately. we have to let you go. Thank you for coming in.")
 exit()

time.sleep(2)
print("")
print("This last question will also be about the last code.")
print("Here is the code")
print(" ")
print(" 'number = input (What month number is December?)'  ")
print(" ")
time.sleep(2)
last= input("What function needs to be added in order for the question to only accept whole numbers? ")

if last.lower() == "int()" or last.lower() == "int" or last.lower()== "integer function" or last.lower()== "integer":
  print(" ")
  print("Correct! You got all three correct.")
else:
  print("Incorrect")
  print("")
  time.sleep(1)
  print("Glad you made it this far. Unfortunately, you needed to answer all questions correctly. Thank you for coming in.")
  exit()

print("")
time.sleep(1)

salary = int(input("How much money do you want to earn as a software engineer. Please type the number. "))
if salary <= 98000 :
 print("")
 print("Great, this is something we can offer you.")

elif salary >= 100000:
  print(" ")
  print("Unfortunately, this is more than we can offer. You were a great candidate, thank you for coming in. ")
  exit()
else: 
  print("This isn't a valid answer. Thank you for coming in. ")
  exit()


print(" ")
time.sleep(1)
print("You have made it through the first part of our interview for this job. You're an amazing applicant. ")
applicant.append(name)
print("")
information = input("Please enter you email: ")
print("")
print(information)
print(" ")
correct= input("Is this email correct? Please enter yes or no: ")
if correct.lower() == "yes":
  email.append(correct)
  time.sleep(1)
  print("")
  print("We will contact you through email for the second part of the interview. It was nice to meet you", name , ". We'll be in touch soon.")
elif correct.lower() == "no":
  print(" ")
  enter = input("Please enter email correctly: ")
  print("")
  print("Your email is: ", enter,)
  time.sleep(1)
  email.append(enter)
  print("")
  time.sleep(2)
  print("We will contact you through email for the second part of the interview. It was nice to meet you", name , ". We'll be in touch soon.")
else:
   print("We will contact you through email for the second part of the interview. It was nice to meet you", name , ". We'll be in touch soon.")

print(" ")
print("Applicant = ", applicant)
print( "Email = ", email)