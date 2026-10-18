---
# Yayına hazır olunca bu satırı sil:
draft: true
title: "20. Hafta – MicroPython yazım kuralları"
description: Girinti, yorum satırı ve hata mesajı okumayı öğreniyoruz — Python'un "noktalama kuralları" bunlar.
sidebar:
  order: 20
hafta: 20
seviye: Python
sure: 2 ders saati
kazanimlar:
  - Girintinin (satır başı boşluğunun) Python'da neden önemli olduğunu açıklar.
  - sleep() ile bekleme süresi ayarlar.
  - Basit bir hata mesajını okuyup hangi satırda sorun olduğunu bulur.
makecode: ""
video: ""
---

## Bu hafta ne öğreneceğiz?

Her dilin yazım kuralları (noktalama, büyük harf) vardır; Python'un en önemli kuralı **girinti**dir. Bu hafta girintiyi, yorum satırlarını ve bir hata mesajını nasıl okuyacağımızı öğreneceğiz. Bu beceri bütün MicroPython derslerinde işimize yarayacak.

**Malzemeler:** micro:bit v2, USB kablo, bilgisayar.

---

## 1. Girinti: "bu satır onun içinde mi?"

Bloklarda bir bloğu başka bir bloğun **içine** sürüklüyorduk (örn. **her zaman** bloğunun içine **simgeyi göster**). MicroPython'da "içine koymak", satırın başına **boşluk** (girinti) koymak demektir:

```python
from microbit import *

while True:
    display.show(Image.HAPPY)
    sleep(500)
    display.clear()
    sleep(500)
```

`while True:` satırından sonraki 4 satır, **4 boşlukla** içeri kaydırılmış — bunlar döngünün *içindedir*. Girinti olmasaydı Python hangi satırların döngüye ait olduğunu bilemezdi.

:::caution[En sık hata: girinti kayması]
Aynı blok içindeki tüm satırlar **aynı miktarda** girintili olmalı. Bir satır biraz fazla veya az kaymışsa Python `IndentationError` (girinti hatası) verir. Editörler genelde `:` sonrası otomatik girinti yapar — elle boşluk eklerken dikkatli ol.
:::

---

## 2. Yorum satırı

`#` ile başlayan satırlar Python tarafından **çalıştırılmaz**; sadece insanlar için açıklamadır:

```python
# Bu satır kalp gösterir
display.show(Image.HEART)
```

Yorumlar koda not bırakmak için kullanılır — "neden böyle yazdım?" sorusuna cevap olur.

---

## 3. display ve sleep ile zamanlama

`sleep(ms)` programı belirtilen milisaniye kadar durdurur (bloktaki **duraklat (ms)** ile aynı):

```python
from microbit import *

display.show(Image.YES)
sleep(1000)   # 1000 ms = 1 saniye
display.clear()
```

| Süre | Milisaniye |
| --- | --- |
| Yarım saniye | 500 |
| 1 saniye | 1000 |
| 2,5 saniye | 2500 |

---

## 4. Hata mesajını okumak

MicroPython bir hata bulduğunda ekranda kırmızı bir **traceback** (hata izi) gösterir. Korkutucu görünür ama genelde en alttaki satır, hatayı özetler:

```
Traceback (most recent call last):
  File "main.py", line 4
IndentationError: unexpected indent
```

**Okuma sırası:** 1) `line 4` → hatanın olduğu satır numarası. 2) Son satır (`IndentationError: ...`) → hatanın türü ve açıklaması.

| Hata türü | Anlamı | Genelde sebebi |
| --- | --- | --- |
| IndentationError | Girinti yanlış | Boşluk sayısı tutmuyor |
| SyntaxError | Yazım hatası | Eksik `:`, parantez veya tırnak |
| NameError | Tanınmayan isim | Yazım hatası (örn. `Diplay` yerine `Display`) |

---

## Kendini dene

1. "İsim kaydırma" kodunu yaz: kendi adını kaydır, sonra bir simge göster, sonra ekranı temizle; her adımın arasına uygun bir `sleep()` koy.
2. Koduna kısa bir yorum satırı ekle: "Bu program adımı gösterir ve bekler" gibi.
3. **Hata avı:** Öğretmeninin verdiği (veya 3. bölümdeki) kodda bilerek bir satırın girintisini kaydır, hatayı oku, satır numarasını bul, düzelt.
4. `sleep(500)` yerine yanlışlıkla `Sleep(500)` yaz (büyük S), ne tür bir hata aldığını not et.

---

## Mini quiz

1. Python'da bir satırın bir bloğun "içinde" olduğunu ne gösterir?
   a) Büyük harf  b) Girinti (boşluk)  c) Nokta
2. `#` işareti ne işe yarar?
   a) Döngü başlatır  b) Yorum satırı (açıklama) yazdırır  c) Sayı gösterir
3. `sleep(1000)` kaç saniye bekletir?
   a) 1 saniye  b) 10 saniye  c) 0,1 saniye
4. Hata mesajında en çok işimize yarayan iki bilgi nedir?
   a) Renk ve boyut  b) Satır numarası ve hata türü  c) Tarih ve saat
5. IndentationError genelde neden olur?
   a) Boşluk sayısı tutmadığında  b) İnternet koptuğunda  c) Kart şarjı azaldığında

<details>
<summary>Cevap anahtarı</summary>

1-b · 2-b · 3-a · 4-b · 5-a

</details>

---

## Öğretmen notu

- **1. ders saati:** Girinti kavramı ve blok benzetmesi (10 dk), yorum satırı (5 dk), display + sleep ile birlikte kod yazma (15 dk), sleep tablosuyla pratik (10 dk).
- **2. ders saati:** Hata mesajı okuma — projektörde canlı bir hata üretip birlikte okuma (15 dk), hata avı etkinliği (15 dk), mini quiz (10 dk).
- Girinti hatasını ilk gören öğrenciler genelde "bozuldu" der; bunun normal ve her programcının başına geldiğini, hata mesajının "düşman değil rehber" olduğunu vurgulayın.
- Editör genelde otomatik girinti yapar; elle boşluk silme/ekleme alıştırması yaptırmak hatayı daha iyi anlamalarını sağlar.
- Bu haftadan sonra 21. haftada if-elif-else ile koşulları MicroPython'da yazacağız; girinti burada da aynen geçerli olacak.
