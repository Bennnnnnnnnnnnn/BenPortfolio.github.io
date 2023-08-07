const { google } = require('googleapis');
const { GoogleAuth } = require('google-auth-library');

async function Login(enteredUsername, enteredPassword) {
  const auth = new GoogleAuth({
    keyFile: 'C:/Users/ranga/Desktop/PyProjects/NISHUB/templates/assets/nishub-a90b0195acea.json',
    scopes: ['https://www.googleapis.com/auth/spreadsheets.readonly'],
  });

  const sheets = google.sheets({ version: 'v4', auth });
  const spreadsheetId = '1cvYtJ8W70GT7gXdgDNCpITBossXCNejCmq5_5xF66r4';
  const range = 'Login!A:B';

  sheets.spreadsheets.values.get({
    spreadsheetId,
    range,
  }).then((response) => {
    const rows = response.data.values;
    if (rows.length) {
      console.log('Usernames and passwords:');
      rows.forEach((row) => {
        console.log(`${row[0]}: ${row[1]}`);
        if (row[0] === enteredUsername && row[1] === enteredPassword) {
          window.location.href = 'landing.html';
        }
      });
    } else {
      console.log('No data found.');
    }
  }).catch((err) => {
    console.log(`The API returned an error: ${err}`);
  });
}