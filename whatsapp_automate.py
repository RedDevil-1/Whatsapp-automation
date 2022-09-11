import pandas as pd
import pywhatkit
import datetime


df= pd.read_excel('name_list.xlsx', header=None) #loading the excel file
for index, row in df.iloc[90:100].iterrows(): #for looping for rows in a dataframe
    pywhatkit.sendwhatmsg(f'number ', f'custom message', datetime.datetime.now().hour, datetime.datetime.now().minute +1,20) #sending message


