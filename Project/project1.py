#variant 3 - "Gallon of Gasoline in numbers"

gallons_of_gasoline = float(input("Введите количество галлонов: "))

#По информации из открытых источников 1 галлон бензина = 3,78541 литров
litres_of_gasoline = round(gallons_of_gasoline * 3.78541, 2)
print("Литры:",litres_of_gasoline)

barrels_of_oil_required = round(gallons_of_gasoline / 19.5, 2)
print("Баррелей нефти, требующиеся для производства бензина:",barrels_of_oil_required)

pounds_of_co2 = round(gallons_of_gasoline * 20, 2)
print("Количество фунтов выпускаемого углекислого газа:",pounds_of_co2)

BTU = gallons_of_gasoline * 115000
gallons_of_ethanol = round(BTU / 75700, 2)
print("Эквивалентный объём Этанола (в галлонах):",gallons_of_ethanol)

total_cost = round(gallons_of_gasoline * 3, 2)
print("Общая стоимость бензина (в долларах США):",total_cost)

#Данные из открытых источников: В среднем на человека требуется 656 галлонов бензина в год
#Средний объём бензина, расходуемый на человека (исходим из того, что человек использует автомобиль ежедневно):
gasoline_required_per_person = round(656 * 3.78541 / 365, 2) #в литрах в день
print("Средний объём бензина, расходуемого на человека (в день, в литрах):",gasoline_required_per_person)


#На 2020 год в Новосибирске зарегистрировано почти 500.000 автомобилей
gasoline_average_consumption_in_novosibirsk = round(gasoline_required_per_person * 500000, 2) #в литрах в день
print("Примерный расход бензина в Новосибирске в день (в литрах):",gasoline_average_consumption_in_novosibirsk)

#на 1 января 2021 года в России зарегистрировано порядка 60.000.000 автомобилей
gasoline_average_consumption_in_russia = round(gasoline_required_per_person * 60000000, 2)
print("Примерный расход бензина в России в год (в литрах):",gasoline_average_consumption_in_russia)