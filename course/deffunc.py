def get_max(numbers:list[float]) -> float:
    max = numbers[0]
    for i in numbers:
        if i > max:
            max = i
    return float(max)

result = get_max([12.5, 34, 2424.82222, 14, 10])

print(result)