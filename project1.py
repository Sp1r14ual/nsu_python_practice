#variant 3 - "Gallon of Gasoline in numbers"

gallons_of_gasoline = float(input("Введите количество галлонов: "))

#По информации из открытых источников 1 галлон бензина = 3,78541 литров
litres_of_gasoline = gallons_of_gasoline * 3.78541
print("Литры:",litres_of_gasoline)

barrels_of_oil_required = gallons_of_gasoline / 19.5
print("Баррелей нефти, требующиеся для производства бензина:",barrels_of_oil_required)

pounds_of_co2 = gallons_of_gasoline * 20
print("Количество фунтов выпускаемого углекислого газа:",pounds_of_co2)

BTU = gallons_of_gasoline * 115000
gallons_of_ethanol = BTU / 75700
print("Эквивалентный объём Этанола (в галлонах):",gallons_of_ethanol)

total_cost = gallons_of_gasoline * 3
print("Общая стоимость бензина (в долларах США):",total_cost)

#Данные из открытых источников: В среднем на человека требуется 656 галлонов бензина в год
#Средний объём бензина, расходуемый на человека (исходим из того, что человек использует автомобиль ежедневно):
gasoline_required_per_person = 656 * 3.78541 / 365 #в литрах в день
print("Средний объём бензина, расходуемого на человека (в день, в литрах):",gasoline_required_per_person)


#На 2020 год в Новосибирске зарегистрировано почти 500.000 автомобилей
gasoline_average_consumption_in_novosibirsk = gasoline_required_per_person * 500000 #в литрах в день
print("Примерный расход бензина в Новосибирске в день (в литрах):",gasoline_average_consumption_in_novosibirsk)

#на 1 января 2021 года в России зарегистрировано порядка 60.000.000 автомобилей
gasoline_average_consumption_in_russia = gasoline_required_per_person * 60000000
print("Примерный расход бензина в России в год (в литрах):",gasoline_average_consumption_in_russia)