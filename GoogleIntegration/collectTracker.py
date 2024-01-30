import gspread

class Tracker():
    def __init__(self):
        self.url = ""
        gc = gspread.service_account()
        self.tracker = gc

    def get_url(self):
        return self.url
    
    def set_url(self, url_in):
        self.url = url_in

    def retreive_sheet(self):
        self.tracker = gc.open_by_url(self.get_url())

