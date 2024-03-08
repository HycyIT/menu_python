def count(el1, el2, el3, *el):
    numbers = (el1, el2, el3, *el)
    print(numbers)
    wynik = sum(numbers)
    return wynik


print(count(2, 4, 1, 2, 4, 5, 10, 11, 22, 33, 44))
