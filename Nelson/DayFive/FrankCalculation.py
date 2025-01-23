def gcd(x, y):
    """求最大公约数"""
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor

def lcm(x, y):
    """求最小公倍数"""
    return x * y // gcd(x, y)

# Input two numbers
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

# Calculate GCD and LCM
result_gcd = gcd(x, y)
result_lcm = lcm(x, y)

# Print results
print(f"GCD of {x} and {y} is: {result_gcd}")
print(f"LCM of {x} and {y} is: {result_lcm}")
