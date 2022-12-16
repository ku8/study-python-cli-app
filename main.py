from name import Name
from phonenumber import Phonenumber
from birthday import Birthday
import datetime

def getName():
    inputname = input("名前を入力してください: ")
    try:
        name = Name(inputname)  
    except IndexError as ie:
        print(ie)
        return getName()
    except:
        print("予期せぬエラーが発生しました")
    else:
        return name

def getPhonenumber():
    inputphonenumber = input("電話番号を入力してください: ")
    try:
        phonenumber = Phonenumber(inputphonenumber)
    except IndexError as ie:
        print(ie)
        phonenumber = getPhonenumber()
        return phonenumber
    except:
        print("予期せぬエラーが発生しました")
    else:
        return phonenumber

def getBirthday():
    inputdate = input("誕生日を入力してください（YYYY-MM-dd）: ")
    try:
        date_formatted = datetime.datetime.strptime(inputdate, "%Y-%m-%d")
        birthday = Birthday(date_formatted)
    except ValueError:
        print("入力形式が違います。")
        return getBirthday()
    except IndexError as ie:
        print(ie)
        return getBirthday()
    except:
        print("予期せぬエラーが発生しました")
    else:
        return birthday

def outputInfo(name: Name, phonenumber: Phonenumber, birthday: Birthday):
    print("名前: " + name.value)
    print("電話番号: " + phonenumber.value)
    print("誕生日: " + birthday.date.strftime("%Y-%m-%d"))


def main():
    name = getName()
    phonenumber = getPhonenumber()
    birthday = getBirthday()

    outputInfo(name, phonenumber, birthday)

if __name__ == "__main__":
    main()