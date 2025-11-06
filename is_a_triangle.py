def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

def my_is_a_right_triangle(a, b, c):
    if is_a_triangle(a, b, c) == False:
        return False
    if a>b and a>c:
        return a**2 == b**2 + c**2
    if b>a and b>c:
        return b**2 == a**2 + c**2
    if c>a and c>b:
        return c**2 == a**2 + b**2

def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2

print(my_is_a_right_triangle(5, 3, 4))
print(is_a_right_triangle(5, 3, 4))

print(my_is_a_right_triangle(1, 3, 4))
print(is_a_right_triangle(1, 3, 4))