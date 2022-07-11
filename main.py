# ©Copyright ItzVouzz - 2022. All Rights Reserved
# Tool By ItzVouzz


print(""); print("")
print("AUTOMATIC CALCULATE SYSTEM")
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

        sisi = str(sisi)
        luasPersegi = str(luasPersegi)

        print("")
        print("The wide of a square if the length of the sides is " + sisi + " = " + luasPersegi + "cm2")
        print("")

    if(perintahBangunDatar == "2"):
        panjang = int(input("How long are the sides (cm)? "))
        lebar = int(input("How wide are the sides (cm)? "))
        luasPersegiPanjang = panjang * lebar

        panjang = str(panjang)
        lebar = str(lebar)
        luasPersegiPanjang = str(luasPersegiPanjang)

        print("")
        print("The wide of a Rectangular if the length of the sides is " + panjang + " and the wide of the sides is " + lebar + " = " + luasPersegiPanjang + "cm2")
        print("")

    if(perintahBangunDatar == "3"):
        alas = int(input("How length is the base (cm)? "))
        tinggi = int(input("How height is the triangle (cm)? "))
        luasSegitiga = alas * tinggi // 2

        alas = str(alas)
        tinggi = str(tinggi)
        luasSegitiga = str(luasSegitiga)

        print("")
        print("The wide of a Triangle if the length of the base is " + alas + " and the height of the triangle is " + tinggi + " = " + luasSegitiga + "cm2")
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

        sisi = str(sisi)
        kelilingPersegi = str(kelilingPersegi)

        print("")
        print("The perimeter of a square if the length of the sides is " + sisi + " = " + kelilingPersegi + "cm")
        print("")

    if(perintahBangunDatar == "2"):
        panjang = int(input("How long are the sides (cm)? "))
        lebar = int(input("How wide are the sides (cm)? "))
        kelilingPersegiPanjang = panjang + lebar + panjang + lebar

        panjang = str(panjang)
        lebar = str(lebar)
        kelilingPersegiPanjang = str(kelilingPersegiPanjang)

        print("")
        print("The perimeter of a Rectangular if the length of the sides is " + panjang + " and the wide of the sides is " + lebar + " = " + kelilingPersegiPanjang + "cm")
        print("")

    if(perintahBangunDatar == "3"):
        sisiSegitiga1 = int(input("How length is the side 1 (cm)? "))
        sisiSegitiga2 = int(input("How length is the side 2 (cm)? "))
        sisiSegitiga3 = int(input("How length is the side 3 (cm)? "))
        kelilingSegitiga = sisiSegitiga1 + sisiSegitiga2 + sisiSegitiga3

        sisiSegitiga1 = str(sisiSegitiga1)
        sisiSegitiga2 = str(sisiSegitiga2)
        sisiSegitiga3 = str(sisiSegitiga3)
        kelilingSegitiga = str(kelilingSegitiga)

        print("")
        print("The perimeter of a Triangle if the length of the side 1 is " + sisiSegitiga1 + " , side 2 is " + sisiSegitiga2 + " , and the side 3 is " + sisiSegitiga3 + " = " + kelilingSegitiga + "cm")
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

        bilanganPertama = str(bilanganPertama)
        bilanganKedua = str(bilanganKedua)
        hasilTambah = str(hasilTambah)

        print("")
        print("The result of addition the numbers " + bilanganPertama + " and " + bilanganKedua + " = " + hasilTambah)
        print("")

    if(perintahOther == "2"):
        bilanganPertama = int(input("What is the first number? "))
        bilanganKedua = int(input("What is the second number? "))
        hasilKurang = bilanganPertama - bilanganKedua

        bilanganPertama = str(bilanganPertama)
        bilanganKedua = str(bilanganKedua)
        hasilKurang = str(hasilKurang)

        print("")
        print("The result of subtraction the numbers " + bilanganPertama + " and " + bilanganKedua + " = " + hasilKurang)
        print("")

    if(perintahOther == "3"):
        bilanganPertama = int(input("What is the first number? "))
        bilanganKedua = int(input("What is the second number? "))
        hasilKali = bilanganPertama * bilanganKedua

        bilanganPertama = str(bilanganPertama)
        bilanganKedua = str(bilanganKedua)
        hasilKali = str(hasilKali)

        print("")
        print("The result of multiplication the numbers " + bilanganPertama + " and " + bilanganKedua + " = " + hasilKali)
        print("")

    if(perintahOther == "4"):
        bilanganPertama = int(input("What is the first number? "))
        bilanganKedua = int(input("What is the second number? "))
        hasilBagi = bilanganPertama / bilanganKedua
        hasilBagiDibulatkan = round(hasilBagi)

        bilanganPertama = str(bilanganPertama)
        bilanganKedua = str(bilanganKedua)
        hasilBagi = str(hasilBagi)
        hasilBagiDibulatkan = str(hasilBagiDibulatkan)

        print("")
        print("The result of division the numbers " + bilanganPertama + " and " + bilanganKedua + " = " + hasilBagi + " or when rounded = " + hasilBagiDibulatkan)
        print("")

    if(perintahOther == "5"):
        bilanganPertama = int(input("What is the first number? "))
        bilanganKedua = int(input("What is the second number? "))
        hasilPangkat = bilanganPertama ** bilanganKedua

        bilanganPertama = str(bilanganPertama)
        bilanganKedua = str(bilanganKedua)
        hasilPangkat = str(hasilPangkat)

        print("")
        print("The result of " + bilanganPertama + " to the power " + bilanganKedua + " = " + hasilPangkat)
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