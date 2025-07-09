import calculate

lenght = float(input("Enter the length of the rectangle: "))
width = (input("Enter the width of the rectangle: "))

area = calculate.area(length, width)
perimeter = calculate.perimeter(length, width)

print(f"The area of the rectangle is: {area}")
print(f"The perimeteter of the rectangle is {perimeter}")

