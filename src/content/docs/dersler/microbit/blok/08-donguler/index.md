---
title: "8. Hafta – Döngüler"
description: Her zaman, tekrarla ve olduğunda döngüleriyle tekrar eden işleri kısaltıyor; LED animasyonları ve geri sayım yapıyoruz.
sidebar:
  order: 8
hafta: 8
seviye: Blok
sure: 2 ders saati
kazanimlar:
  - Döngünün ne olduğunu ve neden kullanıldığını açıklar.
  - Her zaman, tekrarla ve olduğunda döngülerini ayırt eder.
  - Belirli sayıda tekrar eden bir döngü yazar.
  - Koşula bağlı bir döngüyle geri sayım programı yazar.
makecode: ""
video: ""
---

## Bu hafta ne öğreneceğiz?

Bir şarkının nakaratını tekrar söyleriz, egzersizde "10 kez zıpla" deriz. Bilgisayarlar da aynı işi tekrar tekrar yapmakta çok iyidir. Tekrar eden adımlara **döngü** denir. Bu hafta üç çeşit döngüyü öğrenecek, animasyon ve geri sayım yapacağız.

**Malzemeler:** micro:bit v2, USB kablo, bilgisayar.

---

## 1. Döngü nedir?

**Döngü**, bir grup adımı tekrar tekrar çalıştıran yapıdır. Döngü olmasaydı aynı bloğu defalarca alt alta koymak zorunda kalırdık.

**Döngüsüz:** simgeyi göster, simgeyi göster, simgeyi göster, simgeyi göster… (10 kez yaz!)
**Döngüyle:** 10 kere tekrarla → simgeyi göster (bir kez yaz!)

**Günlük hayattan döngüler:**

| Etkinlik | Döngü türü |
| --- | --- |
| Kalbin atması | Hiç durmaz → **her zaman** |
| "10 şınav çek" | Belli sayıda → **tekrarla** |
| "Su kaynayana kadar bekle" | Koşul doğru oldukça → **olduğunda** |

---

## 2. Üç çeşit döngü

![Üç döngü türü: her zaman hiç durmaz; tekrarla belli sayıda tekrar edip devam eder; olduğunda koşul doğru oldukça tekrar eder, koşul yanlış olunca biter.](./dongu-turleri.svg)

| Döngü | Ne zaman durur? | Kategori |
| --- | --- | --- |
| her zaman | Hiç durmaz (kart kapanana kadar) | Temel |
| … kere tekrarla | Yazdığın sayı kadar tekrar edince | Döngüler |
| … olduğunda | Koşul yanlış olunca | Döngüler |

:::tip[Her zaman bloğunu tanıyorsun]
2. haftadan beri kullandığımız **her zaman** bloğu da aslında bir döngüdür!
:::

---

## 3. Proje: Yanıp sönen kare ve geri sayım

**Tekrarla:** A'ya basınca kare ile küçük kare 3 kez yanıp sönsün, sonra ekran temizlensin.

**Olduğunda:** B'ye basınca 5'ten geriye saysın; sayı 0'dan büyük oldukça sayıyı gösterip 1 saniye beklesin ve sayıyı 1 azaltsın. Döngü bitince onay simgesi göstersin.

![Tekrarla örneği: A'ya basınca kare ve küçük kare simgeleri 3 kez gösterilir, sonra ekran temizlenir. Olduğunda örneği: B'ye basınca sayı 5 yapılır; sayı 0'dan büyük oldukça sayı gösterilir, 1 saniye beklenir ve sayı 1 azaltılır; sonunda evet simgesi gösterilir.](./dongu-bloklari.png)

**Canlı dene:** <a href="https://makecode.microbit.org/_MEKRT63Wj0Ru" target="_blank" rel="noopener noreferrer">Bu projeyi MakeCode'da aç</a> ve simülatörde çalıştığını gör.

<div class="etkinlik">
<strong>Düşün:</strong> Geri sayımda "sayı değişkenini −1 değiştir" bloğunu unutursak ne olur? Sayı hiç azalmaz, koşul hep doğru kalır ve döngü hiç bitmez. Buna <strong>sonsuz döngü</strong> denir.
</div>

MicroPython'da `for` (belli sayıda) ve `while` (koşul doğru oldukça) döngüleri vardır:

```python
from microbit import *

while True:
    if button_a.was_pressed():
        for i in range(3):
            display.show(Image.SQUARE)
            sleep(300)
            display.show(Image.SQUARE_SMALL)
            sleep(300)
        display.clear()

    if button_b.was_pressed():
        sayi = 5
        while sayi > 0:
            display.show(sayi)
            sleep(1000)
            sayi -= 1
        display.show(Image.YES)
```

Python'da döngünün içindeki satırlar **girintiyle** (satır başındaki boşlukla) belirlenir. Bloklardaki "içine koyma" işinin Python'daki karşılığı budur.

---

## Kendini dene

1. Yanıp sönme sayısını 3'ten 5'e çıkar ve aradaki bekleme süresini değiştir.
2. Geri sayımı 10'dan başlat ve bitince bir melodi çal.
3. Bir LED'in ekranın üst satırında soldan sağa yürümesini **tekrarla** ve **led yak** bloğuyla yap.
4. Sonsuz döngü deneyi: Geri sayımdaki azaltma bloğunu çıkar, simülatörde ne olduğunu gözlemle, sonra hatayı düzelt.

---

## Mini quiz

1. Döngü ne işe yarar?  
   a) Adımları tekrar tekrar çalıştırır  
   b) Rastgele sayı seçer  
   c) Değişken oluşturur
2. "10 kez zıpla" komutu hangi döngüye benzer?  
   a) her zaman  
   b) tekrarla  
   c) olduğunda
3. "olduğunda" döngüsü ne zaman durur?  
   a) Hiç durmaz  
   b) Koşul yanlış olunca  
   c) 4 kez tekrar edince
4. Geri sayımda sayıyı azaltmayı unutursak ne olur?  
   a) Döngü hemen biter  
   b) Sonsuz döngü olur  
   c) Kart kapanır
5. Hangi blok aslında bir döngüdür?  
   a) program başladığında  
   b) her zaman  
   c) simgeyi göster

<details>
<summary>Cevap anahtarı</summary>

1-a · 2-b · 3-b · 4-b · 5-b

</details>

---

## Öğretmen notu

- **1. ders saati:** Döngü kavramı ve "tekrar dansı" ısınması (10 dk), üç döngü türü (15 dk), tekrarla ile yanıp sönen kare (15 dk).
- **2. ders saati:** İken ile geri sayım (15 dk), sonsuz döngü deneyi (5 dk), kendini dene (15 dk), mini quiz (5 dk).
- Isınma önerisi: "3 kez el çırp, sonra zıpla" gibi komutlarla tekrarla döngüsünü; "Ben dur diyene kadar yürü" ile olduğunda döngüsünü bedenle canlandırın.
- Sonsuz döngüyü bilerek yaptırmak, öğrencilerin hatayı tanıyıp düzeltmesini sağlar. Simülatörde yeniden başlat düğmesiyle kolayca çıkılabildiğini gösterin.
- Bu hafta blok döneminin ilk yarısını tamamlıyor. 9. hafta proje haftasında 2–8. haftaların tüm bloklarıyla refleks oyunu yapılacak; öğrencilerden bloklar arasında ne öğrendiklerini kısaca not etmelerini isteyebilirsiniz.
