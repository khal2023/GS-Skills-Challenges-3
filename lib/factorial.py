def factorial(n):
    product = 1
    while n > 0:
        product *= n
        n -= 1
    return product

print(factorial(5))
# Expected: 120 (the result of: 5 * 4 * 3 * 2 * 1)
# Actual: 24