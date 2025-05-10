# import smtplib

# # Define your email address and password
# from_email = "chipichapamanumini@outlook.com"
# password = "Manumini"

# # Define the recipient's email address
# to_email = "manuminichipichapa@outlook.com"

# # Create the email message
# msg = "Subject: Test Email\n\nThis is a test email sent using smtplib in Python."

# # Connect to the SMTP server and send the email
# server = smtplib.SMTP("gmail.com", 587)
# server = smtplib.SMTP_SSL('smtp.server.com',465)
# server.starttls()
# server.login(from_email, password)
# server.sendmail(from_email, to_email, msg)
# server.quit()

# print("Email sent successfully.")
#!/usr/bin/python3    
import smtplib    
sender_mail = 'dikkshi963@gmail.com'    
receivers_mail = ['gayathri232@gmail.com']    
message = """From: From Person %s  
To: To Person %s  
Subject: Sending SMTP e-mail   
This is a test e-mail message.  
"""%(sender_mail,receivers_mail)    
try:    
#    smtpObj = smtplib.SMTP('localhost')
   smtpObj = smtplib.SMTP("gmail.com", 587)    
   smtpObj.sendmail(sender_mail, receivers_mail, message)    
   print("Successfully sent email")    
except Exception:    
   print("Error: unable to send email") 