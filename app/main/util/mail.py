import smtplib 

from_email = "XXXXXXX@gmail.com"
password = "XXXXXXXXX"
smtp_server = "smtp.gmail.com"
mail_port = 587

class Mail:
	def __init__(self):
		self.address = from_email
		self.password = password
	def send_email(self, message):
		# creates SMTP session 
		s = smtplib.SMTP(smtp_server, mail_port) 
		  
		# start TLS for security 
		s.starttls()
		  
		# Authentication 
		s.login(self.address, self.password) 
		  
		# sending the mail
		s.sendmail(self.address, self.address, message) 
		  
		# terminating the session 
		s.quit() 