"""
Author: Cedric Milinaire(c3dric373), milinaire.c@gmail.com
Building new templates file for a new client, templates file are inspired by https://github.com/d-koppenhagen/latex-rechnung.git
"""
import os
import subprocess
from fileHelper import *

firma = input("Firma: \n")
name =  input("Name: \n")
street =  input("Street: \n")
zip_c =  input("ZIP: \n")
city =  input("City: \n")
service = input("Service: \n")
fee = input("Fee: \n")
training_hours = input("Training hours: \n")

new_data = [firma, name, street, zip_c, city]
template_data = ["#firma","#name","#street","#zip","#city"]
new_invoice_data = [service,fee,training_hours]
template_invoice_data = ["#service","#fee","#training_hours"]

# Building the new data  file
invoice_template_directory = '/home/c3dric/Perso/Klein Unternehmen/latex-rechnung/' + firma + name
os.makedirs(invoice_template_directory)
os.chdir(invoice_template_directory)
subprocess.run(['cp','-a','/home/c3dric/Perso/Klein Unternehmen/latex-rechnung/original/.', invoice_template_directory])
openAndReplace('data.tex','data.tex',template_data,new_data)

# Building the new invoice file
openAndReplace('invoice.tex','invoice.tex',template_invoice_data, new_invoice_data)
