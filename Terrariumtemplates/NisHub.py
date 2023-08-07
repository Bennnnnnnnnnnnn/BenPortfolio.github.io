import eel
import io
import os.path
import tkinter as tk
from tkinter import ttk
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from tqdm import tqdm
import time
import os
import threading

version = "0.0.1"


# Set the credentials for the Google Sheets API
creds = service_account.Credentials.from_service_account_file('C:/Users/ranga/Desktop/PyProjects/NISHUB/templates/assets/nishub-a90b0195acea.json')

# Create a Sheets API client
sheets_service = build('sheets', 'v4', credentials=creds)

# Set the ID of the spreadsheet and the range of the cell to check
spreadsheet_id = '1cvYtJ8W70GT7gXdgDNCpITBossXCNejCmq5_5xF66r4'
range_name = 'Sheet1!A2'

# Create a GUI window
root = tk.Tk()

# Create a label widget to show a message while the progress bar is loading
label = tk.Label(root, text='Checking for updates...')
label.pack(pady=10)

# Create a progress bar widget
progress_bar = ttk.Progressbar(root, orient='horizontal', length=200, mode='determinate')
progress_bar.pack(pady=10)

# Define a function to update the progress bar
def update_progress_bar(value):
    progress_bar['value'] = value
    root.update_idletasks()

# Call the function to update the progress bar
update_progress_bar(10)

def check_for_updates():
    try:
        update_progress_bar(50)
        # Add a delay of 10 seconds
        update_progress_bar(76)
        root.after(1000, lambda: update_progress_bar(95))
        
        # Get the value of the cell
        result = sheets_service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
        value = result.get('values', [[]])[0][0]
        update_progress_bar(99)
        root.after(3000, lambda: update_progress_bar(100), root.destroy())
        # Check the version number
        if value > version:
            print('A new version is available.')
            label['text'] = 'A new version is available!'
        else:
            print('No update available.')
            label['text'] = 'You are up to date!'

        

        # Print the value of the cell
        print(value)

    except HttpError as error:
        print(f'An error occurred: {error}')

# Call the check_for_updates function after a delay of 4 seconds
root.after(2000, check_for_updates)

# Start the GUI event loop
root.mainloop()

# Define a function to start the eel GUI application
def start_eel():
    eel.init(r'C:\Users\ranga\Desktop\PyProjects\NISHUB\templates')
    eel.start('index.html', size=(300, 200))

# Start the eel GUI application in a separate thread
eel_thread = threading.Thread(target=start_eel)
eel_thread.start()

os.system('python C:/Users/ranga/Desktop/PyProjects/NISHUB/templates/LoginPy.py')