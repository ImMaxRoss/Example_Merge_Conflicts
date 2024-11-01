def sum_numbers(a, b):
    return a + b

def compute_average(a, b):
    my_sum = sum_numbers(a, b)
    return my_sum / 2

a = 10
b = 20
result = compute_average(a,b)
print(f"The average of {a} and {b} is {result}")