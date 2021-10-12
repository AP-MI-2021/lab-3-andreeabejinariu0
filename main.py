import math

def citire_lista():
    result_list = []
    string_lista = input("Introduceti lista: ")

    string_elemente = string_lista.split(sep=" ")

    for string_element in string_elemente:
        element = int(string_element )
        result_list.append(element)

    return result_list


def is_odd(n):
    if n % 2 == 1:
        return True
    else:
        return False

def product_list_is_odd(lista):
    p = math.prod(lista)
    return is_odd(p)

def get_longest_product_is_odd(lista):
    secventa_maxima = []
    secventa = []
    for start in range(0,len(lista)):
        for end in range(start + 1, len(lista) + 1):
            if product_list_is_odd(lista[start:end]):
                secventa_maxima.append(lista[start:end])
    secventa_maxima_finala = []
    for string_elemente in secventa_maxima:
        if len(string_elemente) > len(secventa_maxima_finala):
            secventa_maxima_finala = string_elemente
    return secventa_maxima_finala

def test_get_longest_product_is_odd():
    assert(get_longest_product_is_odd([4, 5, 1, 2])) == [5, 1]
    assert(get_longest_product_is_odd([11, 15, 6, 1, 7, 9, 11])) == [1, 7, 9, 11]
    assert(get_longest_product_is_odd([1, 3, 11, 9, 2])) == [1, 3, 11, 9]
    assert(get_longest_product_is_odd([11])) == [11]
    assert(get_longest_product_is_odd([2, 4, 8])) == []


def main():
    while True:
        print("1. Citire lista ")
        print("2. Produsul numerelor este impar")
        print("4. Iesire din program - exit")
        optiune = input("Alege optiunea: ")
        lista = []
        if optiune == "1":
            lista = citire_lista()
        elif optiune == "2":
            print(" Cea mai lunga subsecventa este ", get_longest_product_is_odd(lista))
        elif optiune ==  "4":
            break
        else:
            print("Optiune invalida!")

test_get_longest_product_is_odd()
main()