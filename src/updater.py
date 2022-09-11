from threading import Thread
from database import Database
from gSheet import GSheet

gsheet = GSheet()
new_thread = Thread(target=gsheet.update).start()