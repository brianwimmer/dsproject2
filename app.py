import os
import mysql.connector
from datetime import datetime
from chalice import Chalice
import requests
import json

app = Chalice(app_name='dsproject24')
app.debug = True

HOST = 'dsproject24-rds.cfojcr9rybat.us-east-1.rds.amazonaws.com'
USER = 'brianwimmer'
PASS = 'brianwimmer'

db = mysql.connector.connect(host=HOST,user=USER,passwd=PASS,database='ds3002')

c = db.cursor()
value_insert = """INSERT INTO PROJECT_DATA (factor,pi,time) VALUES (%s, %s, %s)"""
results = value_insert
print(results)


def table_values(factor,pi,time):
        db
        c
        results
        variables = (factor,pi,time)
        c.execute(results,variables)
        db.commit()

@app.schedule('cron(0-59 * ? * * *)')
def cron_tab(event):
        url = "https://4feaquhyai.execute-api.us-east-1.amazonaws.com/api/pi"
        r = requests.get(url)
        p = json.loads(r.text)
        table_values(p['factor'],p['pi'],p['time'])
