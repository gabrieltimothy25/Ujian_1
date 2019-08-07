#Soal Satu
""" def find_short(s):
    lst = s.split()
    shortest = len(lst[0])
    for l in lst:
        if len(l) < shortest:
            shortest = len(l)
    return(shortest)
print(find_short("Create new file after this morning")) """

#Soal Dua
""" def persistence(n):
    count = 0
    product = n 
    while True:
        if product > 10:
            arr = []
            sum1 = []
            strnum = str(product)
            for s in strnum:
                arr.append(int(s))
            product = arr[0]
            for i in range(1, len(arr)):
                product = product * arr[i]
            count += 1
        else:
            return count
print(persistence(9631)) """
#Soal Tiga

""" def multiplication_table(row, col):
    z = ''
    for i in range(1, row+1):
        first = 0
        multiple = i
        for j in range(1, col+1):
            first += multiple
            z += str(first)
            z += ' '
        z += '\n'
    return z
print(multiplication_table(4,6)) """

#Soal Empat
""" def alphabet_position(text):
    main_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26,}
    arr = text.split()
    z = ''
    for word in arr:
        for letter in word.lower():
            if letter in main_dict:
                z += str(main_dict[letter])
                z += ' '
            else:
                pass
    return z
print(alphabet_position("it's never too late to try")) """

#Soal Lima
""" def is_prime(num):
    prime_list = [2]
    num2 = 3
    #append prime terus ampe sedeket mungkin ama num
    while prime_list[-1] < num:
        for p in prime_list:
            if num2 % p == 0:
                break
        else:
            prime_list.append(num2)
        num2 += 2
    #kalo loopnya stop pas tepat di num
    if prime_list[-1] == num:
        return True
    #kalo loop stop pas beda sama num
    else:
        return False 
print(is_prime(1))
print(is_prime(2))
print(is_prime(-1))   
print(is_prime(5099)) """


            
