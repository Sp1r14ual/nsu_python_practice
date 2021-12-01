weight = int(input()) / 2.20462
height = int(input()) * 0.0254

imt = round(weight/height**2, 2)

if imt < 16:
    print("выраженный дефицит массы тела")
elif imt >= 16 and imt <= 18.49:
    print("недостаточная масса тела")
elif imt >= 18.5 and imt <= 24.99:
    print("норма")
elif imt >= 25 and imt <= 29.99:
    print("избыточная масса тела")
elif imt >= 30 and imt <= 34.99:
    print("ожирение первой степени")
elif imt >= 35 and imt <= 39.99:
    print("ожирение второй степени")
else:
    print("ожирение третьей степени")