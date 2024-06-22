# input: format: dd/mm/yyyy
date = input("Nhap ngay voi dinh dang dd/mm/yyyy: ")
# cat chuoi => data list: day, month, year
date = date.split("/")  # list: 3 items
# khai bao bien ket qua
result = ""
# handler exception
# kiem tra day
if len(date[0]) < 2:
    result += f"Ngay 0{date[0]}"
else:
    result += f"Ngay {date[0]}"
# kiem tra month
if len(date[1]) < 2:
    result += f" Thang 0{date[1]}"
else:
    result += f" Thang {date[1]}"
# kiem tra year (yy - yyyy)
if len(date[2]) == 2:
    if int(date[2]) > 24:
        result += f' Nam 19{date[2]}'
    else:
        result += f' Nam 20{date[2]}'
elif len(date[2]) == 4:
    result += f' Nam {date[2]}'

# print ket qua
print(result)
