weight = int(input()) / 2.20462
height = int(input()) * 0.0254
imt = round(weight/height**2, 2)
print(imt)
#works incorrectly