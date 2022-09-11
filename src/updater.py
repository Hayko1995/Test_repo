from threading import Thread
from src.gSheet import GSheet

def activate_tread():
    gsheet = GSheet()
    new_thread = Thread(target=gsheet.update).start()