import smtplib

sender = 'it@domain.com'
receivers = ['admin@domain.com']

employee_name = raw_input("New employee FULL name: ")
phone = raw_input("Enter the phone number: ")
extension = raw_input("Enter the extension: ")

# Split the name into firstname + last first letter
email = (employee_name.split()[0] + employee_name.split()[1][0]).lower() + "@domain.com"
message = """From: IT Automation <it@domain.com>
To: Admin <admin@rushingco.com>
Subject: New Employee Created : {0}

User {1} has been created, and may receive emails.
Phone Number: {2}
Extension: {3}

*This message was sent by a robot. Beep boop*
"""

formatted_message = message.format(employee_name, email, phone, extension)

# print (formatted_message)
try:
   smtpObj = smtplib.SMTP('exchange_server', 25)
   smtpObj.sendmail(sender, receivers, formatted_message)
   print "Successfully sent email"
except smtplib.SMTPException:
   print "Error: unable to send email"
