import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
os.environ['DJANGO_SETTINGS_MODULE'] = 'wineshop.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from django.conf import settings
from reports.models import *
from products.models import *
from datetime import date
import csv

import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

class DailyReport():

	def generate_daily_report(self):
		self.today = date.today()
		today_sales_list = DailySales.objects.filter(soled_on=self.today).values('categorie','products','qunatity','count','soled_on')
		self.final_list = []
		for each in today_sales_list:
			categorie_obj = Categorie.objects.get(pk=each['categorie'])
			product_obj = Product.objects.get(pk=each['products'])
			qunatity_obj = Qunatite.objects.get(pk=each['qunatity'])
			total_price = (int(each['count'])) * (int(product_obj.price))
			
			kwargs = {
			"categorie":categorie_obj.name,
			"products":product_obj.name,
			"qunatity":qunatity_obj.name,
			"count":each['count'],
			"price":total_price,
			"soled_on":each['soled_on']

			}

			self.final_list.append(kwargs)
		return self.final_list

	def generate_csv(self):
		self.filename = "/home/user/Desktop/daily_report.csv"
		self.generate_daily_report()

		headers = ['categorie','products','qunatity','count','price','soled_on'] 

		with open(self.filename, 'w') as csvfile: 
			# creating a csv dict writer object 
			writer = csv.DictWriter(csvfile, fieldnames = headers) 
			  
			# writing headers (field names) 
			writer.writeheader() 
			  
			# writing data rows 
			writer.writerows(self.final_list) 

	def send_mail_alert(self,filepath):
		msg = MIMEMultipart() 

	  	"""storing the sender and recevier mail with subject"""
	  	msg['From'] = "deepikaduggirala7@gmail.com"
	  	msg['To'] = "deepikaduggirala7@gmail.com"
	  	msg['Cc'] = "deepikaduggirala7@gmail.com"
	  	msg['Subject'] = "Today your products sales"

	  	"""attach the body"""
	  	body = "kindly find the attachment"
	  	msg.attach(MIMEText(body, 'plain')) 

	  	"""attachment"""
	  	attachment = open(filepath, "rb") 
	  	mail_attach = MIMEBase('application', 'octet-stream') 
	  	mail_attach.set_payload((attachment).read()) 
	  	encoders.encode_base64(mail_attach) 
	  	mail_attach.add_header('Content-Disposition', "attachment; filename= %s" % "practise2.csv") 
	  	msg.attach(mail_attach) 

	  	"""creating a session"""
	  	mail_server = smtplib.SMTP('smtp.gmail.com', 587)
	  	"""start TLS for security """
	  	mail_server.starttls()
	  	mail_server.login("deepikaduggirala7@gmail.com", "deepika649") 
	  	text = msg.as_string() 
	  	mail_server.sendmail(msg['From'],msg['To'],text) 
	  	mail_server.quit() 


if __name__ == '__main__':
	da_rep_obj = DailyReport()
	da_rep_obj.generate_daily_report()
	da_rep_obj.generate_csv()
	# da_rep_obj.send_mail_alert("/home/user/Desktop/daily_report.csv")

