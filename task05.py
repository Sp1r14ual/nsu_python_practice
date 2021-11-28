print("Как зовут главных героев компьютерной игры Minecraft?")
first_character = input("Имя первого героя: ")
second_character = input("Имя второго героя: ")
print("Верно" if (first_character == "Стив" and second_character == "Алекс") or (first_character == "Алекс" and second_character == "Стив") else "Неверно")
