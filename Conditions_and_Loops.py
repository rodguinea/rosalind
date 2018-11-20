def sum_all_odd(a, b):
    complete_numbers = list(range(a, b + 1))
    odd_numbers = []
    for n in complete_numbers:
        if n % 2 != 0:
            odd_numbers.append(n)
    return sum(odd_numbers)
