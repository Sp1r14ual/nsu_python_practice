seconds = int(input())
minutes = int(seconds // 60)
hours = int(minutes // 60)
minutes -= hours * 60
seconds -= hours * 60 * 60 + minutes * 60
print(hours,"часов",minutes,"минут",seconds,"секунд")

