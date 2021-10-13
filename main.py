import math

def citire_lista():
    lista = []
    string_lista = input("Introduceti lista: ")

    string_elemente = string_lista.split(sep=" ")

    for string_element in string_elemente:
        element = int(string_element )
        lista.append(element)

    return lista


def is_odd(n):
    '''
    verifica daca numarul este impar
    :param n: numarul pentru care verificam paritatea
    :return: rezultatul verificarii
    '''
    if n % 2 == 1:
        return True
    else:
        return False

def product_list_is_odd(lista):
    '''
    Verifica daca produsul elementelor este impar
    :param lista: lista ce contine elementele de inmultit
    :return: rezultatul verificarii
    '''
    p = math.prod(lista)
    return is_odd(p)

def get_longest_product_is_odd(lista):
    '''
    Gaseste si returneaza cea mai lunga secventaa listei pt care produsul elementelor este un nr impar
    :param lista: lista in care va cauta subsecventa cu proprietatea ceruta
    :return: secventa maxima care implineste proprietatea ceruta
    '''
    secventa_maxima = []
    for start in range(0,len(lista)):
        for end in range(start + 1, len(lista) + 1):
            if product_list_is_odd(lista[start:end]):
                secventa_maxima.append(lista[start:end])
    secventa_maxima_finala = []
    for lista_elemente in secventa_maxima:
        if len(lista_elemente) > len(secventa_maxima_finala):
            secventa_maxima_finala = lista_elemente
    return secventa_maxima_finala

def test_get_longest_product_is_odd():
    assert(get_longest_product_is_odd([4, 5, 1, 2])) == [5, 1]
    assert(get_longest_product_is_odd([11, 15, 6, 1, 7, 9, 11])) == [1, 7, 9, 11]
    assert(get_longest_product_is_odd([1, 3, 11, 9, 2])) == [1, 3, 11, 9]
    assert(get_longest_product_is_odd([11])) == [11]
    assert(get_longest_product_is_odd([2, 4, 8])) == []

def concatenare_string(lista):
    str_conc = ''
    for element in lista:
        str_conc = str_conc + str(element)
    concatenare = int(str_conc)
    return concatenare


def ordine_crescatoare(n):
    m = n
    while m:
        if m % 10 < (m // 10) % 10 :
            return False
        m //= 10
    return True

def get_longest_concat_digits_asc(lista):
    secventa_maxima = []
    for start in range(0, len(lista)):
        for end in range(start + 1, len(lista) + 1):
            numar = concatenare_string(lista[start:end])
            if ordine_crescatoare(numar):
                secventa_maxima.append(lista[start:end])
    secventa_maxima_finala = []
    for lista_elemente in secventa_maxima:
        if len(lista_elemente) > len(secventa_maxima_finala):
            secventa_maxima_finala = lista_elemente
    return secventa_maxima_finala

def test_get_longest_concat_digits_asc():
    assert(get_longest_concat_digits_asc([12, 34, 56, 84])) == [12, 34, 56]
    assert(get_longest_concat_digits_asc([51, 24, 57])) == [24, 57]
    assert(get_longest_concat_digits_asc([23, 58])) == [23, 58]
    assert(get_longest_concat_digits_asc([82, 43])) == []

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    d=2
    while d <= int(math.sqrt(n)) + 1:
        if n % d == 0:
            return False
        d += 1
    return True

def get_longest_concat_is_prime(lista):
    secventa_maxima = []
    for start in range(0, len(lista)):
        for end in range(start + 1, len(lista) + 1):
            numar = concatenare_string(lista[start:end])
            if is_prime(numar):
                secventa_maxima.append(lista[start:end])
    secventa_maxima_finala = []
    for lista_elemente in secventa_maxima:
        if len(lista_elemente) > len(secventa_maxima_finala):
            secventa_maxima_finala = lista_elemente
    return secventa_maxima_finala

def main():
    while True:
        print("1. Citire lista ")
        print("2. Produsul numerelor este impar")
        print("3. Concatenarea numerelor din subsecvență are cifrele în ordine crescătoare")
        print("4. Concatenarea numerelor din subsecvență este număr prim.")
        print("5. Iesire din program - exit")
        optiune = input("Alege optiunea: ")
        if optiune == "1":
            lista = citire_lista()
        elif optiune == "2":
            print(" Cea mai lunga subsecventa este ", get_longest_product_is_odd(lista))
        elif optiune == "3":
            print(get_longest_concat_digits_asc(lista))
        elif optiune == "4":
            print(get_longest_concat_is_prime(lista))
        elif optiune == "5":
            break
        else:
            print("Optiune invalida!")

test_get_longest_product_is_odd()
main()