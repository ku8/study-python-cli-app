import datetime

class Birthday:
    def __init__(self, date: datetime.datetime):
        now = datetime.datetime.today()
        if date > now:
            raise IndexError("未来の日付が入力されています")
        else:
            self.date = date
