#Soal 1
def calculate_final_return(principal, interest, tax, time):
    return_before_tax = (principal * (1 + interest)**time)
    return_after_tax = return_before_tax - (0.18 * 0.05 * return_before_tax)
    return(return_after_tax)

def calculate_years(principal, interest, tax, desired):
    for time in range(1, 101):
        final_return = calculate_final_return(principal, interest, tax, time)
        if final_return >= desired:
            return(time)
print(calculate_years(1000, 0.05, 0.18, 1100))
#Soal 2
def expandedForm(num):
    if num <= 10:
        print(num)
    elif num > 10 and num <= 100:
        i = 0
        while (num)>10:
            num -= 10
            i += 10
        print(str(i) + " + " + str(num))
    elif num > 100 and num <= 1000:
        j = 0
        while (num)>100:
            num -= 100
            j += 100
        i = 0
        while (num)>10:
            num -= 10
            i += 10
        print(str(j) + " + " + str(i) +  " + "+ str(num))
    elif num > 1000 and num <= 10000:
        k = 0
        while (num)>1000:
            num -= 1000
            k += 1000
        j = 0
        while (num)>100:
            num -= 100
            j += 100
        i = 0
        while (num)>10:
            num -= 10
            i += 10
        print(str(k) + " + "+ str(j) + " + " + str(i) + "+ " + str(num))
    elif num > 10000 and num <= 100000:
        m = 0
        while (num)>10000:
            num -= 10000
            m += 10000
        k = 0
        while (num)>1000:
            num -= 1000
            k += 1000
        j = 0
        while (num)>100:
            num -= 100
            j += 100
        i = 0
        while (num)>10:
            num -= 10
            i += 10
        print(str(m) + " + " + str(k) + " + " + str(j) + " + " + str(i) + " + " + str(num))
    elif num > 100000 and num < 1000000:
        n = 0
        while (num)>100000:
            num -= 100000
            n+=100000
        m = 0
        while (num)>10000:
            num -= 10000
            m += 10000
        k = 0
        while (num)>1000:
            num -= 1000
            k += 1000
        j = 0
        while (num)>100:
            num -= 100
            j += 100
        i = 0
        while (num)>10:
            num -= 10
            i += 10
        print(str(n) + " + " + str(m) + " + " + str(k) + " + " + str(j) + " + " + str(i) + " + " + str(num))
    else:
        o = 0
        while (num)> 1000000:
            num -= 1000000
            o += 1000000
        n = 0
        while (num)>100000:
            num -= 100000
            n+=100000
        m = 0
        while (num)>10000:
            num -= 10000
            m += 10000
        k = 0
        while (num)>1000:
            num -= 1000
            k += 1000
        j = 0
        while (num)>100:
            num -= 100
            j += 100
        i = 0
        while (num)>10:
            num -= 10
            i += 10
        print(str(o) + " + " + str(n) + " + " + str(m) + " + " + str(k) + " + " + str(j) + " + " + str(i) + " + " + str(num))
            
expandedForm(2345)
#Soal 3

def floor_builder(w, h, space):
    for i in range(0, h):
        for j in range(0, w):
            space += '*'
        if i < h-1:
            space += '\n'
        else:
            space += ''
    print(space)

def space_builder(w):
    space=''
    for y in range(w):
        space+=' '
    return space

def tower_builder(n_floors, block_size):
    w, h = block_size
    if w <= 0 or h <= 0 or n_floors <= 0:
        print('')
    else:
        for a in range(n_floors+1):
            f = space_builder(w)
            floor_builder(a * w, h, f)
tower_builder(6, (2,1))