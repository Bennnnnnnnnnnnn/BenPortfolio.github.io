from flask import Flask, render_template, request, jsonify
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Function to read data from Google Sheets and check login details
def read_google_sheet(username, password):
    print('Reading Google Sheet')
    # Set the credentials for the Google Sheets API
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('C:/Users/ranga/Desktop/PyProjects/NISHUB/templates/assets/nishub-a90b0195acea.json', scope)
    client = gspread.authorize(creds)
    # Open the Google Sheet and select the second worksheet
    sheet_url = 'https://docs.google.com/spreadsheets/d/1cvYtJ8W70GT7gXdgDNCpITBossXCNejCmq5_5xF66r4/edit#gid=512769293'
    sheet = client.open_by_url(sheet_url).worksheet('Login')
    # Get all the data from the worksheet
    data = sheet.get_all_values()
    print('AAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH') 
    # Convert the set object to a list
    data = list(data)
    # Search for the username and password in the data
    for row in data:
        if row[0] == username and row[1] == password:
            print('success, we found a match' + row[0] + ' ' + row[1])
            # Create a dictionary with the plugin access information
            plugin_access = {
                'Wolf Spider': row[2],
                'Wombat': row[3],
                'Sentipede': row[4],
                'Moss': row[5],
                'Possum': row[6],
                'Bonsai': row[7],
                'Millipede': row[8],
                'Tarantula': row[9]
            }
            # Return the login status and plugin access information
            print(plugin_access)
            return {'status': 'success', 'plugins': plugin_access}
            
    # If the username and password are not found, return an error message
    return {'status': 'error', 'message': 'Invalid username or password'}
    

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    # Get the username and password from the request
    username = request.form['username']
    password = request.form['password']

    # Call the read_google_sheet() function with the username and password
    result = read_google_sheet(username, password)

    # Return the result as JSON
    return jsonify(result)

if __name__ == '__main__':
    app.run()