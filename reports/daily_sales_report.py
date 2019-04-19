import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
os.environ['DJANGO_SETTINGS_MODULE'] = 'wineshop.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from django.conf import settings
from reports.models import *
from datetime import date

class DailyReport():

	def generate_daily_report(self):
		today = date.today()
		print today
		today_sales_list = DailySales.objects.filter(created_at=today)
		print today_sales_list
		

if __name__ == '__main__':
	da_rep_obj = DailyReport()
	da_rep_obj.generate_daily_report()
