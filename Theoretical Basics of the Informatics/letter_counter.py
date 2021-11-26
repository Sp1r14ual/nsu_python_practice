dic = dict()
file = open("input.txt", "r", encoding='UTF8')
output = open("output.txt", "w")
total_symbols = 0
for string in file:
    for symbol in string:
        total_symbols += 1
        char = symbol.lower()
        dic[char] = dic.get(char, 0) + 1

non_letter_symbols = [".", ",", ":", ";", "?", "!", "-", "/", "\\", '"', "'", "\n", "`", "~", "_", "+", "=", "%", "$", "&", "*", "<", ">", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

for key in dic:
    output.write(key + " = " + str(dic[key]) + "\n")
    if not key in non_letter_symbols:
        output.write("Possibility for character " + key + " is " + str(dic[key]/total_symbols)+ "\n")
    output.write("\n")
