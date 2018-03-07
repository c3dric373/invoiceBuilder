#coding: utf-8

"""
Author: Cedric Milinaire (c3dric373), milinaire.c@gmail.com

A little python script that writes the missing data in my invoice files and builds a pdf that will be send to the client, the latex template files are taken from https://github.com/d-koppenhagen/latex-rechnung.git, I readapted them to my need.
The user only needs to specify how many hours are being charged, the invoice number and the month the invoice refers to.
"""

import os
import subprocess
import re
import time
from  fileHelper import *

# Getting data from user
training_hours = input("How much did you work this month ?\n")
invoice_number = input("Invoice number please: \n")
month_of_invoice = input("Please give the month of the inovice in: \n")

# Data
invoice_template_directory = '/home/c3dric/Perso/Klein Unternehmen/latex-rechnung/KMFC/'
invoice_directory = '/home/c3dric/Perso/Klein Unternehmen/rechnungen/2018/'
tmp_directory = '/tmp/rechnungen/'
invoice_name = "Facture" + invoice_number + ".pdf"
invoice_path = invoice_directory + invoice_name
body = "Hallo Markus und Manuela,\n\n im Anhang findet ihr die Rechnung zum Monat " +         month_of_invoice + ".\n\n Viele Grüße,\n\n Cédric"

# Creating a temporary directory to build the pdf file later
subprocess.run(['cp','-r',invoice_template_directory,tmp_directory])

# Moving to directory where templates file are stored
os.chdir(invoice_template_directory)

# Building the invoice file
openAndReplace("invoice.tex","/tmp/rechnungen/invoice.tex", ["#training_hours"],[ training_hours])

# Getting the date of today and two weeks from now
year = subprocess.run(['date', '+%Y'], stdout=subprocess.PIPE).stdout.decode('utf-8')
date = subprocess.run(['date', '+%d.%m.%y'], stdout=subprocess.PIPE).stdout.decode('utf-8')
due_date = subprocess.run(['date',"--date=+14 day", '+%d.%m.%y'], stdout=subprocess.PIPE).stdout.decode('utf-8')

# Removing unused newline
date = date.rstrip('\n')
due_date = due_date.rstrip('\n')

# Building the data file
openAndReplace("data.tex","/tmp/rechnungen/data.tex",["#date","#due_date","#invoice_number"],[ date,due_date,invoice_number])

# Building the main file
openAndReplace("main.tex","/tmp/rechnungen/main.tex",[ "#monthYear"],[ month_of_invoice + " " + year])

# Building the pdf file moving int into the correct directory and deleting the /tmp/rechnungen directory
os.chdir(tmp_directory)
subprocess.run(['pdflatex','main.tex'])
subprocess.run(['mv','main.pdf',invoice_path])
subprocess.run(['rm','-rf', tmp_directory])

# Sending the made invoice via mail
client_mail = "to=KravMaga-FightClub@gmx.de"
attachment = ",attachment=" + invoice_path
subject = ",subject=Rechnung " + month_of_invoice
tmp_file = open("/tmp/body.txt","w",encoding='utf-8')
tmp_file.write(body)
tmp_file.close()
message = ",message=/tmp/body.txt"

# Thunderbird needs to start from home directory
os.chdir("/home/c3dric/")
subprocess.run(['thunderbird','-compose',(client_mail+subject+message+attachment)])
time.sleep(1)
subprocess.run(['rm','/tmp/body.txt'])
