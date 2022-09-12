from __future__ import print_function
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account
from src.database import Database
import time


class GSheet(Database):
    def __init__(self):

        self.SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
        self.SERVICE_ACCOUNT_FILE = 'keys.json'

        self.credentials = service_account.Credentials.from_service_account_file(
            self.SERVICE_ACCOUNT_FILE, scopes=self.SCOPES)
        self.SAMPLE_SPREADSHEET_ID = '14pQEczfnpTI2Amwl-l7w-xMaYOZLDdg37Wg9blonLKo'

    def get_from_gsheet(self):
        try:
            service = build('sheets', 'v4', credentials=self.credentials)

            # Call the Sheets API
            sheet = service.spreadsheets()

            result = sheet.values().get(spreadsheetId=self.SAMPLE_SPREADSHEET_ID,
                                        range="Лист1!A1:AA1000").execute()

            values = result.get('values', [])

        except HttpError as err:
            print(err)

        return values

    def init_db(self):
        """Shows basic usage of the Docs API.
        Prints the title of a sample document.
        """
        values = self.get_from_gsheet()

        self.creat_table(values[0])
        head = values.pop(0)
        self.insert_into_db(head, values)

    def update(self):
        self.init_db()
        while(1):
            result = self.get_from_gsheet()
            head = result.pop(0)
            _, db_res = self.get_from_database()
            db_res = list(map(list, [x[:-1] for x in db_res]))
            if not result == db_res:
                self.drop_table()
                self.creat_table(head)
                self.insert_into_db(head, result)
            time.sleep(1)
