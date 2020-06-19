
def asalmi(a):
    dongus = 2
    cikti = "Bu bir asal sayıdır."
    while dongus < a:
        if a % dongus == 0:
            cikti = "Bu sayı asal sayı değildir"
        dongus += 1
    print(cikti)
    return a


print("*******************************************\n",
      "Asal sayı tespit programına hoş geldiniz.\n",
      "*******************************************\n")

print("Asal olup olmadığını öğrenmek istediğiniz sayıyı giriniz: ")
sayi = asalmi(int(input()))
