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
    annual_income += income
    print("Доход: " + str(annual_income))

if choice == "1":
    if 0 <= annual_income <= 9075:
        tax = annual_income * 0.1
    elif 9076 <= annual_income <= 36900:
        tax = 907.5 + (annual_income - 9075) * 0.15
    elif 36901 <= annual_income <= 89350:
        tax = 5088.75 + (annual_income - 36900) * 0.25
    elif 89351 <= annual_income <= 186350:
        tax = 18201.25 + (annual_income - 89350) * 0.28
    elif 186351 <= annual_income <= 405100:
        tax = 45361.25 + (annual_income - 186350) * 0.33
    elif 405101 <= annual_income <= 406750:
        tax = 117548.75 + (annual_income - 405100) * 0.35
    elif annual_income >= 406751:
        tax = 118126.25 + (annual_income - 406750) * 0.396
        
    print("Налог равен " + str(round(tax, 2)) + " долларов")

elif choice == "2":
    if 0 <= annual_income <= 18150:
        tax = annual_income * 0.1
        
    elif 18151 <= annual_income <= 73800:
        tax = 18150 * 0.1 + (annual_income - 18150) * 0.15
        
    elif 73801 <= annual_income <= 148850:
        tax = 18150 * 0.1 + 55650 * 0.15 + (annual_income - 73800) * 0.25
        
    elif 148851 <= annual_income <= 226850:
        tax = 18150 * 0.1 + 55650 * 0.15 + 75050 * 0.25 + (annual_income - 148850) * 0.28
        
    elif 226851 <= annual_income <= 405100:
        tax = 18150 * 0.1 + 55650 * 0.15 + 75050 * 0.25 + 78000 * 0.28 + (annual_income - 226850) * 0.33
        
    elif 405101 <= annual_income <= 457600:
        tax = 18150 * 0.1 + 55650 * 0.15 + 75050 * 0.25 + 78000 * 0.28 + 178250 * 0.33 + (annual_income - 405100) * 0.35
        
    elif annual_income >= 457601:
        tax = 18150 * 0.1 + 55650 * 0.15 + 75050 * 0.25 + 78000 * 0.28 + 178250 * 0.33 + 52500 * 0.35 + (annual_income - 457600) * 0.396
        
    print("Ваш налог составляет " + str(round(tax, 2)) + " долларов")

elif choice == "3":
    if 0 <= annual_income <= 12950:
        tax = annual_income * 0.1
        
    elif 12951 <= annual_income <= 49400:
        tax = 12951 * 0.1 + (annual_income - 18150) * 0.15
        
    elif 49401 <= annual_income <= 127550:
        tax = 12951 * 0.1 + 55650 * 0.15 + (annual_income - 73800) * 0.25
        
    elif 127551 <= annual_income <= 206600:
        tax = 12951 * 0.1 + 55650 * 0.15 + 75050 * 0.25 + (annual_income - 148850) * 0.28
        
    elif 206601 <= annual_income <= 405100:
        tax = 12951 * 0.1 + 55650 * 0.15 + 75050 * 0.25 + 78000 * 0.28 + (annual_income - 226850) * 0.33
        
    elif 405101 <= annual_income <= 432200:
        tax = 12951 * 0.1 + 55650 * 0.15 + 75050 * 0.25 + 78000 * 0.28 + 178250 * 0.33 + (annual_income - 405100) * 0.35
        
    elif annual_income >= 432201:
        tax = 12951 * 0.1 + 36450 * 0.15 + 78150 * 0.25 + 79050 * 0.28 + 198500 * 0.33 + 27100 * 0.35 + (annual_income - 457600) * 0.396
        
    print("Ваш налог составляет " + str(round(tax, 2)) + " долларов")

else:
    print("Некорректные входные данные")