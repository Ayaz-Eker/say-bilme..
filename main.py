import random

print("Sayı Tahmin Oyununa Hoş Geldin!")
# 1 ile 100 arasında rastgele bir sayı seçer
gizli_sayi = random.randint(1, 100)
tahmin = 0

while tahmin != gizli_sayi:
    tahmin = int(input("1 ile 100 arasında bir sayı tahmin et: "))
    
    if tahmin < gizli_sayi:
        print("Daha büyük bir sayı söyle!")
    elif tahmin > gizli_sayi:
        print("Daha küçük bir sayı söyle!")
    else:
        print("Tebrikler, doğru bildin!")
