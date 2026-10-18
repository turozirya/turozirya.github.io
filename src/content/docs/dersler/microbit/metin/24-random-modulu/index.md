---
# Yayına hazır olunca bu satırı sil:
draft: true
title: "24. Hafta – random modülü"
description: Python'da rastgelelik için ayrı bir modül içe aktarılır; bununla 7. haftadaki zar ve taş-kâğıt-makası yeniden yazıyoruz.
sidebar:
  order: 24
hafta: 24
seviye: Python
sure: 2 ders saati
kazanimlar:
  - Bir modülü import ile programa eklediğini açıklar.
  - randint() ile belirli aralıkta rastgele sayı üretir.
  - choice() ile bir listeden rastgele eleman seçer.
makecode: ""
video: ""
---

## Bu hafta ne öğreneceğiz?

7. haftada **rastgele değer seçimi** bloğunu kullanmıştık. MicroPython'da rastgelelik, `from microbit import *` içinde hazır gelmez — ayrı bir **modül** (araç kutusu) içe aktarmamız gerekir: `random`.

**Malzemeler:** micro:bit v2, USB kablo, bilgisayar.

---

## 1. Modül (import) nedir?

Bir **modül**, belirli bir işe yarayan hazır fonksiyonlar kümesidir. `from microbit import *` ekranı, düğmeleri, sesi getirir; rastgelelik için `random` modülünü de eklememiz gerekir:

```python
from microbit import *
import random
```

:::tip[Neden her şey otomatik gelmiyor?]
Her modülü otomatik yüklemek, kullanmayacağımız araçları da hafızaya almak demektir — küçük bir kartta yer kaplar. İhtiyacımız olan modülü kendimiz seçeriz.
:::

---

## 2. randint(): belirli aralıkta rastgele sayı

```python
from microbit import *
import random

while True:
    if accelerometer.was_gesture("shake"):
        zar = random.randint(1, 6)
        display.show(zar)
```

`random.randint(1, 6)` → 1 ile 6 arasında (1 ve 6 dahil) rastgele bir tam sayı — bloktaki **rastgele değer seçimi 1 ila 6** ile aynı iş.

`accelerometer.was_gesture("shake")` → "salla ise" bloğunun MicroPython karşılığı; 25. haftada hareket sensörlerini ayrıntılı göreceğiz, burada sadece zar örneği için önizliyoruz.

---

## 3. choice(): listeden rastgele seçim

Taş-kâğıt-makas gibi "birkaç seçenekten biri" durumlarında bir **liste** yapıp `random.choice()` ile seçeriz — 16. haftadaki liste bilgisi burada işimize yarıyor:

```python
from microbit import *
import random

secenekler = ["taş", "kâğıt", "makas"]

while True:
    if accelerometer.was_gesture("shake"):
        secim = random.choice(secenekler)
        display.scroll(secim)
```

| Fonksiyon | Ne yapar | Blok karşılığı |
| --- | --- | --- |
| `random.randint(a, b)` | a-b arasında rastgele tam sayı | rastgele değer seçimi |
| `random.choice(liste)` | Listeden rastgele bir eleman | rastgele değerini al |

---

## Kendini dene

1. Zar aralığını 1-6'dan 1-20'ye çıkar (çok yüzlü zar).
2. Taş-kâğıt-makas listesine görsel ekleme yerine, her seçime özel bir `Image` simgesi atayan bir sözlük/eşleştirme dene (ileri seviye — yardım isteyebilirsin).
3. Bir "kahin" yap: `secenekler = ["Evet", "Hayır", "Belki"]` listesinden A tuşuna basınca rastgele cevap versin.
4. `import random` satırını bilerek sil, ne tür hata aldığını oku (`NameError`), sonra geri ekle.

---

## Mini quiz

1. Rastgele sayı üretmek için hangi modül içe aktarılır?
   a) microbit  b) random  c) music
2. `random.randint(1, 6)` ifadesi ne üretir?
   a) Her zaman 6  b) 1 ile 6 arasında rastgele tam sayı  c) 0 ile 1 arasında ondalık sayı
3. `random.choice(secenekler)` ne yapar?
   a) Listeyi sıralar  b) Listeden rastgele bir eleman seçer  c) Listeyi siler
4. `import random` satırını silersek ne olur?
   a) Hiçbir şey değişmez  b) random fonksiyonları tanınmaz, hata verir  c) Kart yeniden başlar
5. Taş-kâğıt-makas projesinde seçenekler nerede tutulur?
   a) Bir listede  b) Bir sayıda  c) Bir metinde (tek kelime)

<details>
<summary>Cevap anahtarı</summary>

1-b · 2-b · 3-b · 4-b · 5-a

</details>

---

## Öğretmen notu

- **1. ders saati:** Modül/import kavramı (10 dk), randint ile zar oyunu (15 dk), simülatörde/kartta salla hareketini deneme (15 dk).
- **2. ders saati:** Liste + choice ile taş-kâğıt-makas (15 dk), kendini dene (20 dk), import'u silme deneyi (5 dk).
- "Modül" kavramını somutlaştırmak için gerçek bir araç kutusu benzetmesi iyi işler: "Her işin için ayrı bir kutuyu masana açarsın, kullanmayacağını açmazsın."
- `accelerometer.was_gesture("shake")` bu hafta sadece örnek olarak kullanıldı; 25. haftada bu fonksiyonu ve diğer hareket fonksiyonlarını ayrıntılı işleyeceğiz, şimdi her ayrıntısını sormayın.
- 25. haftada tüm sensörleri (hareket, ışık, sıcaklık) MicroPython ile toplu olarak göreceğiz — bu hafta kısaca gördüğümüz `accelerometer` orada derinleşecek.
