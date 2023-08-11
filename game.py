import random 

oyunTahtası = [' ' for x in range(10)]  # 1'den 9'a kadar olan sayıları belirtir.


def ekranaGöster():
    print(' ' + oyunTahtası[1] + ' ' + '|' + ' ' + oyunTahtası[2] + ' ' + '|' + ' ' + oyunTahtası[3])
    print("----------")
    print(' ' + oyunTahtası[4] + ' ' + '|' + oyunTahtası[5] + ' ' + '|' + ' ' + oyunTahtası[6])
    print("----------")
    print(' ' + oyunTahtası[7] + ' ' + '|' + ' ' + oyunTahtası[8] + ' ' + '|' + ' ' + oyunTahtası[9])


def harfKoy(harf, konum):
    oyunTahtası[konum] = harf


def alanBosMu(konum):
    return oyunTahtası[konum] == ' '


def tahtaDolu():
    if oyunTahtası.count(' ') > 1:
        return False
    else:
        return True


def kazanan(oyunTahtası, harf):
    return (oyunTahtası[1] == harf and oyunTahtası[2] == harf and oyunTahtası[3] == harf) or \
           (oyunTahtası[4] == harf and oyunTahtası[5] == harf and oyunTahtası[6] == harf) or \
           (oyunTahtası[7] == harf and oyunTahtası[8] == harf and oyunTahtası[9] == harf) or \
           (oyunTahtası[1] == harf and oyunTahtası[4] == harf and oyunTahtası[7] == harf) or \
           (oyunTahtası[2] == harf and oyunTahtası[5] == harf and oyunTahtası[8] == harf) or \
           (oyunTahtası[3] == harf and oyunTahtası[6] == harf and oyunTahtası[9] == harf) or \
           (oyunTahtası[1] == harf and oyunTahtası[5] == harf and oyunTahtası[9] == harf) or \
           (oyunTahtası[3] == harf and oyunTahtası[5] == harf and oyunTahtası[7] == harf)


def oyuncuHareketi():
    konum = int(input("Enter a number between 1 and 9: "))
    if 1 <= konum <= 9:
        if alanBosMu(konum):
            harfKoy('X', konum)
            if kazanan(oyunTahtası, 'X'):
                ekranaGöster()
                print("Congratulations! You win...")
                exit()
            ekranaGöster()
            print("**************************************")
        else:
            print("The location you entered is not available. Please enter again:")
            oyuncuHareketi()
    else:
        print("Invalid location. Please enter a number between 1 and 9:")
        oyuncuHareketi()


def bilgisayarHareketi():
    müsait_konumlar = [konum for konum, harf in enumerate(oyunTahtası) if harf == ' ' and konum != 0]

    hareket = 0
    for harf in ['O', 'X']:
        for i in müsait_konumlar:
            kopyaTahta = oyunTahtası[:]
            kopyaTahta[i] = harf
            if kazanan(kopyaTahta, harf):
                hareket = i
                return hareket

    köşeler = []
    for i in müsait_konumlar:
        if i in [1, 3, 7, 9]:
            köşeler.append(i)

    if len(köşeler) > 0:
        hareket = random.choice(köşeler)
        return hareket

    if 5 in müsait_konumlar:
        hareket = 5
        return hareket

    içerisi = []
    for i in müsait_konumlar:
        if i in [2, 4, 6, 8]:
            içerisi.append(i)

    if len(içerisi) > 0:
        hareket = random.choice(içerisi)
        return hareket


def oyun():
    print("---WELCOME TO XOX GAME---")
    ekranaGöster()

    while not tahtaDolu():
        oyuncuHareketi()
        if tahtaDolu():
            print("Game over. No winner...")
            exit()

        bilgisayar_hareket = bilgisayarHareketi()
        harfKoy('O', bilgisayar_hareket)
        if kazanan(oyunTahtası, 'O'):
            ekranaGöster()
            print("The winner is computer, try agin.")
            exit()
        ekranaGöster()

    if tahtaDolu():
        print("Game over, no winner.")


oyun()

