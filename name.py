class Name():
    def __init__(self, value: str):
        if not value:
            raise IndexError("1文字以上入力してください")
        else:
            self.value = value

    