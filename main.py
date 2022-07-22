# ©Copyright ItzVouzz - 2022. All Rights Reserved
# Tool By ItzVouzz



print(""); print("")
print("CALCULATE SYSTEM")
print("BY ITZVOUZZ")
print("")
print("[1] Wide")
print("[2] Perimeter")
print("[3] Other")
print("")

perintahAwal = input("What Are You Looking For? ")

if(perintahAwal == "1"):
    print("")
    print("[1] Square")
    print("[2] Rectangular")
    print("[3] Triangle")
    print("")
    perintahBangunDatar = input("Which wide of Two-Dimentional figure are you looking for? ")

    if(perintahBangunDatar == "1"):
        sisi = int(input("How length are the sides (cm)? "))
        luasPersegi = sisi * sisi

        print("")
        print(f"The wide of a square if the length of the sides is {str(sisi)} = {str(luasPersegi)}cm2")
        print("")

    elif(perintahBangunDatar == "2"):
        panjang = int(input("How long are the sides (cm)? "))
        lebar = int(input("How wide are the sides (cm)? "))
        luasPersegiPanjang = panjang * lebar

        print("")
        print(f"The wide of a Rectangular if the length of the sides is {str(panjang)} and the wide of the sides is {str(lebar)} = {str(luasPersegiPanjang)}cm2")
        print("")

    elif(perintahBangunDatar == "3"):
        alas = int(input("How length is the base (cm)? "))
        tinggi = int(input("How height is the triangle (cm)? "))
        luasSegitiga = alas * tinggi / 2
        luasSegitigaBulat = round(luasSegitiga)

        print("")
        print(f"The wide of a Triangle if the length of the base is {str(alas)} and the height of the triangle is {str(tinggi)} = {str(luasSegitiga)}cm2 or when rounded = {str(luasSegitigaBulat)}cm2")
        print("")
        
    else:
        print("")
        print("YOU MUST ENTER BETWEEN 1, 2, OR 3")
        print("")  

elif(perintahAwal == "2"):
    print("")
    print("[1] Rectangle")
    print("[2] Rectangular")
    print("[3] Triangle")
    print("")
    perintahBangunDatar = input("Which perimeter of Two-Dimentional figure are you looking for? ")

    if(perintahBangunDatar == "1"):
        sisi = int(input("How length are the sides (cm)? "))
        kelilingPersegi = 4 * sisi

        print("")
        print(f"The perimeter of a square if the length of the sides is {str(sisi)} {str(kelilingPersegi)}cm")
        print("")

    elif(perintahBangunDatar == "2"):
        panjang = int(input("How long are the sides (cm)? "))
        lebar = int(input("How wide are the sides (cm)? "))
        kelilingPersegiPanjang = panjang + lebar + panjang + lebar

        print("")
        print(f"The perimeter of a Rectangular if the length of the sides is {str(panjang)} and the wide of the sides is {str(lebar)} = {str(kelilingPersegiPanjang)}cm")
        print("")

    elif(perintahBangunDatar == "3"):
        sisiSegitiga1 = int(input("How length is the side 1 (cm)? "))
        sisiSegitiga2 = int(input("How length is the side 2 (cm)? "))
        sisiSegitiga3 = int(input("How length is the side 3 (cm)? "))
        kelilingSegitiga = sisiSegitiga1 + sisiSegitiga2 + sisiSegitiga3

        print("")
        print(f"The perimeter of a Triangle if the length of the side 1 is {str(sisiSegitiga1)}, side 2 is {str(sisiSegitiga2)}, and the side 3 is {str(sisiSegitiga3)} = {str(kelilingSegitiga)}cm")
        print("")

    else:
        print("YOU MUST ENTER BETWEEN 1, 2, OR 3")
        print("") 

elif(perintahAwal == "3"):
    print("")
    print("[1] Addition")
    print("[2] Subtraction")
    print("[3] Multiplication")
    print("[4] Division")
    print("[5] Powers Of Numbers")
    print("")
    print("NOTE:\nYOU CAN ADD 2 NUMBERS ONLY FOR THE OPERATION\nFOR 3 NUMBERS FEATURES OR MORE WILL BE ADDED ON NEXT UPDATE")
    print("")
    perintahOther = input("What operation do you want to run? ")

    if(perintahOther == "1"):
        bilanganPertama = int(input("What is the first number? "))
        bilanganKedua = int(input("What is the second number? "))
        hasilTambah = bilanganPertama + bilanganKedua

        print("")
        print(f"The result of addition the numbers {str(bilanganPertama)} and {str(bilanganKedua)} = {str(hasilTambah)}")
        print("")

    elif(perintahOther == "2"):
        bilanganPertama = int(input("What is the first number? "))
        bilanganKedua = int(input("What is the second number? "))
        hasilKurang = bilanganPertama - bilanganKedua

        print("")
        print(f"The result of subtraction the numbers {str(bilanganPertama)} and {str(bilanganKedua)} = {str(hasilKurang)}")
        print("")

    elif(perintahOther == "3"):
        bilanganPertama = int(input("What is the first number? "))
        bilanganKedua = int(input("What is the second number? "))
        hasilKali = bilanganPertama * bilanganKedua

        print("")
        print(f"The result of multiplication the numbers {str(bilanganPertama)} and {str(bilanganKedua)} = {str(hasilKali)}")
        print("")

    elif(perintahOther == "4"):
        bilanganPertama = int(input("What is the first number? "))
        bilanganKedua = int(input("What is the second number? "))
        hasilBagi = bilanganPertama / bilanganKedua
        hasilBagiBulat = round(hasilBagi)

        print("")
        print(f"The result of division the numbers {str(bilanganPertama)} and {str(bilanganKedua)} = {str(hasilBagi)} or when rounded = {str(hasilBagiBulat)}")
        print("")

    elif(perintahOther == "5"):
        bilanganPertama = int(input("What is the first number? "))
        bilanganKedua = int(input("What is the second number? "))
        hasilPangkat = bilanganPertama ** bilanganKedua

        bilanganPertama = str(bilanganPertama)
        bilanganKedua = str(bilanganKedua)
        hasilPangkat = str(hasilPangkat)

        print("")
        print(f"The result of {str(bilanganPertama)} to the power {str(bilanganKedua)}  = {str(hasilPangkat)}")
        print("")

    else:
        print("")
        print("YOU MUST ENTER BETWEEN 1, 2, 3, 4, OR 5")
        print("")

else:
    print("")
    print("YOU MUST ENTER BETWEEN 1, 2, OR 3")
    print("")

print("THANKS FOR USING MY TOOL")
print("©Copyright ItzVouzz - 2022")
print("")
