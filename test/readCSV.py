# -*- coding: utf-8 -*-
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

import pandas as pd
from datetime import datetime,date
import re


# Read the CSV file
df = pd.read_csv('treasure.csv')

df['Urgency'] = pd.to_datetime(df['Urgency'],errors='coerce')
print(df['Urgency'].dt.day)
df['Month'] = df['Urgency'].dt.month
print(df.head())


today = date.today()
# df['DDL'] = (today - df['Urgency']).dt.days
A = (pd.to_datetime(df['Urgency'], format='%Y-%m-%d').dt.date-today).apply(lambda x: int(re.findall(r'\d+', str(x))[0]))
print(A)
# A = A.apply(lambda x: pd.Timestamp(x.to_timedelta()))
print(type(df['Urgency'][0]))
print(type(A[0]))
print(A.dtype)
df['DDL'] = A

# Print the first few rows of the DataFrame
print(df.head())
# print(df.head().to_string(encoding='utf-8'))
print("能显示中文吗？")
