# Week 1.3, Session 2: Email Extractor

raw_emails = ["UserA@gmail.com", "admin@site.com", "usera@gmail.com", "UserB@yahoo.com", "admin@site.com"]


# set comprehension to extract a clean, unique set of lowercase email addresses

<<<<<<< HEAD
clean_email = {item.lower() for item in raw_emails}

# print the clean set of email addressed

print(clean_email)
=======
cleanemail = {x.lower() for x in raw_emails}
# print the clean set of email addressed
print(cleanemail) 
>>>>>>> refs/remotes/origin/main

# Optional - consider the case where some of the emails are not valid (i.e., without the @ in the email address).
raw_emails2 = ["UserA@gmail.com", "SYSTEM_ALERT", "usera@gmail.com", "admin@site.com", "UserB@yahoo.com"]
# write another set comprehension for this case to extract a clean, unique set of valid, lowercase email addresses
<<<<<<< HEAD

cleaner_email = {item.lower() for item in raw_emails2 if item[-4: ] == ".com"}
print(cleaner_email)
=======
cleaneremail = {x.lower() for x in raw_emails2 if x[-4: ] == ".com"}
>>>>>>> refs/remotes/origin/main
