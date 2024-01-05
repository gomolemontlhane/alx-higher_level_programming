#!/usr/bin/python3
Rectangle = __import__('6-rectangle').Rectangle

my_rectangle_1 = Rectangle(2, 4)
my_rectangle_2 = Rectangle(3, 3)

print(Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2))

my_rectangle_2.width = 10
my_rectangle_2.height = 5
print(Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2))
