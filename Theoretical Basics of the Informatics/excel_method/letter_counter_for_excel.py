import sys
import os

if not 'xlsxwriter' in sys.modules:
    os.system("pip3 install XlsxWriter")

import xlsxwriter

workbook = xlsxwriter.Workbook('toi.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write("A1", 'Символы')
worksheet.write("B1", 'Количество')
worksheet.write("C1", 'Вероятность')

dic = dict()
file = open("input.txt", "r", encoding='UTF8')
total_symbols = 0
for string in file:
    for symbol in string:
        total_symbols += 1
        char = symbol.lower()
        dic[char] = dic.get(char, 0) + 1

non_letter_symbols = [".", ",", ":", ";", "?", "!", "-", "/", "\\", '"', "'", "\n", "`", "~", "_", "+", "=", "%", "$", "&", "*", "<", ">", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

index = 2

for key in dic:
    if not key in non_letter_symbols:
        worksheet.write(f'A{index}', key)
        worksheet.write(f'B{index}', dic[key])
        worksheet.write(f'C{index}', dic[key] / total_symbols)
        index += 1

workbook.close()
exit()