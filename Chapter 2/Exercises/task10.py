choice = input("Собака короткошерстной породы? ").lower()
if choice == "да":
    choice = input("Рост собаки менее 50 см? ").lower()
    if choice == "да":
        choice = input("У собаки короткий хвост? ").lower()
        if choice == "да":
            print("английский бульдог")
        else:
            choice = input("У собаки длинные уши? ").lower()
            if choice == "да":
                print("гончая")
            else:
                choice = input("У собаки короткое тело? ").lower()
                if choice == "да":
                    print("мопс")
                else:
                    print("чихуахуа")
    else:
        choice = input("Собака весит более 50 кг? ").lower()
        if choice == "да":
            print("датский дог")
        else:
            print("фоксхаунд")
else:
    choice = input("Рост собаки менее 50 см? ").lower()
    if choice == "да":
        choice = input("У собаки доброжелательный характер? ").lower()
        if choice == "да":
            print("кокер-спаниэль")
        else:
            print("ирландский сеттер")
    else:
        choice = input("У собаки рост менее 70 см? ").lower()
        if choice == "да":
            choice = input("У собаки длинные уши? ").lower()
            if choice == "да":
                print("большой вандейский грифон")
            else:
                print("колли")
        else:
            choice = input("Окрас рыжий с белыми отметинами? ").lower()
            if choice == "да":
                print("сенбернар")
            else:
                choice = input("Белоснежный окрас? ").lower()
                if choice == "да":
                    print("ирландский волкодав")
                else:
                    print("ньюфаундленд")


#Дебилизм какой-то, я ещё должен и подгонять код под забаганную систему отладки?
#Подгорело