---
title: "3. Hafta – LED Ekran"
description: micro:bit ekranında simge, kendi çizimimiz, yazı ve sayı gösteriyor; basit animasyonlar yapıyoruz.
sidebar:
  order: 3
hafta: 3
seviye: Blok
sure: 2 ders saati
kazanimlar:
  - LED ekranın 5x5 yapısını ve koordinat sistemini açıklar.
  - Hazır simgeleri ve kendi çizdiği deseni ekranda gösterir.
  - Yazı ve sayıları ekranda kaydırır.
  - Duraklat ve ekranı temizle bloklarıyla basit bir animasyon oluşturur.
makecode: ""
video: ""
---

## Bu hafta ne öğreneceğiz?

Geçen hafta ekranda bir kalp gösterdik. Bu hafta LED ekranı yakından tanıyacak; kendi simgelerimizi çizecek, adımızı kaydıracak ve küçük animasyonlar yapacağız.

**Malzemeler:** micro:bit v2, USB kablo, bilgisayar. Bilgisayarsız etkinlik için kareli kâğıt ve kırmızı kalem.

---

## 1. LED ekran nasıl çalışır?

micro:bit ekranı 5 sütun ve 5 satırdan oluşan **25 LED**'den yapılmıştır. Her LED'in bir adresi vardır: **x** soldan sağa sütunu, **y** yukarıdan aşağı satırı gösterir.

![LED ekranın koordinatları: x sütunları soldan sağa 0'dan 4'e, y satırları yukarıdan aşağı 0'dan 4'e numaralanır. x 3, y 1 konumundaki LED yanıyor.](./led-koordinat.svg)

:::tip[Dikkat: sayma 0'dan başlar]
Bilgisayarlar saymaya genellikle 0'dan başlar. Bu yüzden ilk sütun x = 0, son sütun x = 4'tür.
:::

**Bilgisayarsız etkinlik – Piksel oyunu:** Kareli kâğıda 5x5'lik bir kare çiz. Arkadaşın sana koordinatlar söylesin ("x = 2, y = 0"), sen o kareyi boya. Sonunda hangi resim çıktı?

Tek bir LED'i yakmak için **Led** kategorisindeki koordinat bloğunu kullanırız: x ve y değerlerini yazarız, o LED yanar.

---

## 2. Hazır simgeler

**Temel** kategorisindeki **simge göster** bloğunda kalp, mutlu yüz, üzgün yüz, ok, ördek, ev gibi hazır çizimler vardır. Bloktaki küçük resme tıklayıp istediğini seçebilirsin.

---

## 3. Kendi çizimin: LED'leri göster

Hazır simgeler yetmezse **LED'leri göster** bloğuyla kendi resmini çizersin. Bloktaki 25 kareden yanmasını istediklerine tıkla; tıklanan kareler kırmızı olur.

**Etkinlik:** Önce kareli kâğıtta bir simge tasarla (güneş, ağaç, baş harfin…), sonra **LED'leri göster** bloğuyla ekrana aktar.

---

## 4. Yazı ve sayı göstermek

| Blok | Ne yapar? | Örnek |
| --- | --- | --- |
| yazı göster | Yazıyı ekranda sağdan sola kaydırır | "Merhaba" |
| sayı göster | Sayıyı gösterir; birden çok basamaklıysa kaydırır | 7, 2026 |
| ekranı temizle | Tüm LED'leri söndürür | — |

:::note[Türkçe karakterler]
micro:bit ekranı ç, ğ, ı, ö, ş, ü harflerini gösteremeyebilir. Yazılarında bu harfler yerine c, g, i, o, s, u kullanmayı dene.
:::

---

## 5. Animasyon yapmak

Çizgi filmler, art arda gösterilen resimlerden oluşur. Her resme **kare** denir. micro:bit'te de birkaç simgeyi art arda göstererek animasyon yaparız.

- **duraklat (ms):** Bir sonraki kareye geçmeden bekler. 1000 ms = 1 saniye.
- **sürekli** bloğunun içine koyduğun animasyon hiç durmadan tekrar eder.

---

## 6. Proje: İsim kartı

Kart açıldığında "Merhaba" yazsın, sonra sürekli olarak adını ve kendi çizdiğin simgeyi göstersin.

![İsim kartı kodu: başlangıçta Merhaba yazısı ve mutlu simge; sürekli bloğunda isim yazısı, kendi çizimin, duraklat, ekranı temizle ve duraklat blokları.](./isim-karti-bloklari.svg)

MicroPython'da aynı fikir şöyle yazılır:

```python
from microbit import *

display.scroll("Merhaba")
display.show(Image.HAPPY)

while True:
    display.scroll("ELIF")
    display.show(Image("09090:99999:99999:09990:00900"))
    sleep(500)
    display.clear()
    sleep(500)
```

`Image("09090:...")` içindeki her rakam bir LED'in parlaklığıdır: 0 sönük, 9 en parlak. İki nokta üst üste (:) yeni satıra geçer.

---

## Kendini dene

1. Kendi baş harfini **LED'leri göster** ile çiz ve 1 saniye göster.
2. 3 karelik bir animasyon yap: örneğin küçük kare → büyük kare → boş ekran.
3. Bugünün tarihini **sayı göster** ile göster.
4. Koordinat bloğuyla ekranın dört köşesindeki LED'leri sırayla yak.

---

## Mini quiz

1. micro:bit ekranında kaç satır ve kaç sütun vardır?
   a) 4 satır, 4 sütun  b) 5 satır, 5 sütun  c) 6 satır, 6 sütun
2. Sol üst köşedeki LED'in koordinatı nedir?
   a) x = 1, y = 1  b) x = 0, y = 0  c) x = 5, y = 5
3. Kendi resmimizi çizmek için hangi bloğu kullanırız?
   a) LED'leri göster  b) yazı göster  c) sayı göster
4. 1000 ms kaç saniyedir?
   a) 10 saniye  b) 1 saniye  c) 100 saniye
5. Art arda gösterilen resimlerle oluşturulan harekete ne denir?
   a) Koordinat  b) Animasyon  c) Değişken

<details>
<summary>Cevap anahtarı</summary>

1-b · 2-b · 3-a · 4-b · 5-b

</details>

---

## Öğretmen notu

- **1. ders saati:** LED ekran ve koordinatlar (10 dk), piksel oyunu (15 dk), hazır simgeler ve LED'leri göster (15 dk).
- **2. ders saati:** Yazı ve sayı gösterme (10 dk), animasyon (10 dk), isim kartı projesi (15 dk), mini quiz (5 dk).
- Piksel oyunu için 5x5 kareli çalışma kâğıdı hazırlamak tasarım aşamasını hızlandırır; öğrenciler önce kâğıtta çizip sonra koda aktarır.
- Yazı kaydırma yavaştır. Öğrencilere kısa yazılar (3–5 harf) kullanmalarını önerin, yoksa test etmek uzun sürer.
- Blok ve simge adları MakeCode sürümüne göre biraz farklı görünebilir; dersten önce kendi ekranınızda kontrol edin.
