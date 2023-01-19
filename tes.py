import pandas as pd
import numpy as np
import seaborn as sbn
import matplotlib.pyplot as plt
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow,Flow
from google.auth.transport.requests import Request
import os
import pickle
import xgboost as xgb

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# here enter the id of your google sheet
SAMPLE_SPREADSHEET_ID_input = '19T6DAOMgsbGSO2jRHFAOh1ATq9c_3OMiWZsH_LuTvs4'
SAMPLE_RANGE_NAME = 'A1:AA1000'

def main():
    global values_input, service, df
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES) # here enter the name of your downloaded JSON file
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result_input = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID_input,
                                range=SAMPLE_RANGE_NAME).execute()
    values_input = result_input.get('values', [])
    df=pd.DataFrame(values_input[0:], columns=values_input[0])
    


    if not values_input and not values_expansion:
        print('No data found.')


def consulta_simple():
    nombre = input("Introduce el nombre ")
    h_nombre = input("Introduce el nombre del Heroe ")
    newdf = df[(df.Nombre == nombre) & (df.Nombre_del_Héroe == h_nombre)]
    print(newdf)

main()


nombre = input("Introduce el nombre ")
h_nombre = input("Introduce el nombre del Heroe ")
newdf = df[(df.Nombre == nombre) & (df.Nombre_del_Héroe == h_nombre)]
print(newdf.)

