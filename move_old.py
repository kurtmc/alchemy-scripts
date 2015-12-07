import os
import dateutil.parser as dparser
from subprocess import Popen, PIPE
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Moveds all old pdfs into a subdirector named expired

def exec_cmd(cmd):
	return os.popen(cmd).read()

working_dir = "/home/kurt/alchemy-workspace/Product Data Sheet Stuff/Product_Data_Sheets"

pdfs = dict()


os.chdir(working_dir)

for i in os.listdir(working_dir):
	if i.endswith(".pdf"): 
		creation_date = exec_cmd("pdfinfo \"" +  i + "\" 2> /dev/null| grep CreationDate 2> /dev/null")
		creation_date = creation_date[16:]
		creation_date = creation_date.strip()
		if (len(creation_date) > 2):
			try:
				actual_date = dparser.parse(creation_date, fuzzy=True)
				pdfs[i] = actual_date
			except ValueError:
				pass
			
	else:
		continue


five_years_ago = datetime.now() - relativedelta(years=5)

expired = []

for key in pdfs:
	if (pdfs[key] < five_years_ago):
		expired.append(key)

exec_cmd("mkdir expired")

for f in expired:
	exec_cmd("mv \"" + f + "\" expired/")
