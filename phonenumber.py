import re

class Phonenumber:

    def __init__(self, value: str):
        
        if re.match("^\d{10}$", value):
            self.value = value
        elif re.match("^\d{11}$", value):
            self.value = value
        else:
            raise IndexError("電話番号は数字の10 or 11桁で入力してください")