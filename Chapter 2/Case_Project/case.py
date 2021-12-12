# Team
# Panasenko Sergey - 50%
# Lysenko Matvey - 25%
# Yachin Denis - 25%

print('Выберете статус налогоплательщика:')
print('1. Для одного субъекта')
print('2. Для супружеской пары')
print('3. Для родителя-одиночки')

choice = input("Введите номер подходящего варианта: ")

print("Введите ваши доходы для соответствующего месяца")
months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']

annual_income = 0

for month in months:
    print(f"{month}")
    income = float(input())
    if income < 0:
        print("Некорректные входные данные")
        exit()
    annual_income += income
    print("Годовой доход: " + str(annual_income))

if choice == "1":
    if 0 <= annual_income <= 9075:
        tax = annual_income * 0.1
    elif 9076 <= annual_income <= 36900:
        tax = annual_income * 0.15 - 453.75
    elif 36901 <= annual_income <= 89350:
        tax = annual_income * 0.25 - 4136.25
    elif 89351 <= annual_income <= 186350:
        tax = annual_income * 0.28 - 6816.75
    elif 186351 <= annual_income <= 405100:
        tax = annual_income * 0.33 - 16134.25
    elif 405101 <= annual_income <= 406750:
        tax = annual_income - 130236.25
    elif annual_income >= 406751:
        tax = annual_income - 42946.75

elif choice == "2":
    if 0 <= annual_income <= 18150:
        tax = annual_income * 0.1
    elif 18151 <= annual_income <= 73800:
        tax = annual_income * 0.15 - 907.5
    elif 73801 <= annual_income <= 148850:
        tax = annual_income * 0.25 - 8287.5
    elif 148851 <= annual_income <= 226850:
        tax = annual_income * 0.28 - 12753
    elif 226851 <= annual_income <= 405100:
        tax = annual_income * 0.33 - 24095.5
    elif 405101 <= annual_income <= 457600:
        tax = annual_income * 0.35 - 32197.5
    elif annual_income >= 457601:
        tax = annual_income * 0.396 - 53247.1

elif choice == "3":
    if 0 <= annual_income <= 12950:
        tax = annual_income * 0.1
    elif 12951 <= annual_income <= 49400:
        tax = annual_income * 0.15 - 1427.4
    elif 49401 <= annual_income <= 127550:
        tax = annual_income * 0.25 - 8807.4
    elif 127551 <= annual_income <= 206600:
        tax = annual_income * 0.28 - 13272.9
    elif 206601 <= annual_income <= 405100:
        tax = annual_income * 0.33 - 24615.4
    elif 405101 <= annual_income <= 432200:
        tax = annual_income * 0.35 - 32717.4
    elif annual_income >= 432201:
        tax = annual_income * 0.396 - 57785.5

else:
    print("Некорректные входные данные")
    exit()

print("Налог равен " + str(round(tax, 2)) + " долларов")
