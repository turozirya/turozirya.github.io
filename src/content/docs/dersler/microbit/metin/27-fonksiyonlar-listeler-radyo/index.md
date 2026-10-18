---
# Yayına hazır olunca bu satırı sil:
draft: true
title: "27. Hafta – Fonksiyonlar, listeler, radyo"
description: 14-17. haftalardaki fonksiyon, liste ve radyo bloklarını def, liste ve radio modülüyle MicroPython'da yazıyoruz.
sidebar:
  order: 27
hafta: 27
seviye: Python
sure: 2 ders saati
kazanimlar:
  - def ile kendi fonksiyonunu tanımlar.
  - Python listesi oluşturup eleman ekler/okur.
  - radio modülüyle iki kart arasında mesaj gönderir.
makecode: ""
video: ""
---

## Bu hafta ne öğreneceğiz?

Python dönemini kapatmadan önce, 16. haftadaki fonksiyon/liste ve 14-15. haftadaki radyo konularını MicroPython'da topluyoruz. Bu üçü birlikte, gerçek programların nasıl düzenlendiğine dair iyi bir önizleme sunar.

**Malzemeler:** 2 adet micro:bit v2 (çift başına, radyo kısmı için), USB kablolar, bilgisayar.

---

## 1. def ile fonksiyon tanımlama

16. haftadaki **Fonksiyon Yarat...** düğmesinin MicroPython karşılığı `def` anahtar kelimesidir:

```python
from microbit import *

def selam_ver():
    display.scroll("Merhaba")
    display.show(Image.HAPPY)
    sleep(500)
    display.clear()

selam_ver()                 # programın başında bir kere çağır

while True:
    if button_a.was_pressed():
        selam_ver()          # istediğin kadar tekrar çağırabilirsin
```

`def selam_ver():` → "selam_ver adında bir fonksiyon tanımlıyorum" demektir. Fonksiyonun içindeki satırlar girintilidir (20. haftadaki kural burada da geçerli). `selam_ver()` yazarak onu **çağırırız**.

---

## 2. Python listesi

```python
gorevler = ["Zıpla", "Şarkı söyle", "Dans et"]
display.scroll(gorevler[0])     # "Zıpla" — ilk eleman, indeks 0
```

| İş | Kod | Blok karşılığı |
| --- | --- | --- |
| Liste oluşturma | `gorevler = ["a", "b", "c"]` | dizin liste değişkenini yap |
| Eleman ekleme | `gorevler.append("d")` | sonuna değer ekle |
| Uzunluk | `len(gorevler)` | liste dizisi uzunluğu |
| Rastgele seçme | `random.choice(gorevler)` | rastgele değerini al |

```python
from microbit import *
import random

gorevler = ["Zıpla", "Şarkı söyle", "Dans et"]

while True:
    if button_a.was_pressed():
        display.scroll(random.choice(gorevler))
```

---

## 3. radio modülü

```python
from microbit import *
import radio

radio.config(group=1)
radio.on()

while True:
    if button_a.was_pressed():
        radio.send("Merhaba")
    gelen = radio.receive()
    if gelen:
        display.scroll(gelen)
```

| İş | Kod | Blok karşılığı |
| --- | --- | --- |
| Grup ayarlama | `radio.config(group=1)` + `radio.on()` | radyo grubunu ayarla |
| Metin gönderme | `radio.send("...")` | radyo dizgi gönder |
| Alma | `radio.receive()` | radyo ile dizgi alındığında |

:::caution[radio.on() unutulmasın]
Bloklarda radyo otomatik açıktır; MicroPython'da `radio.on()` yazmazsan kart mesaj gönderip almaz. Bu, bu haftanın en sık unutulan satırıdır.
:::

---

## Kendini dene

1. `selam_ver()` fonksiyonuna bir parametre ekle: `def selam_ver(ad):` ve içinde `display.scroll(ad)` kullan (ileri seviye).
2. Görev listesine kendi fikrini ekle, `len(gorevler)` ile kaç görev olduğunu göster.
3. İki kartla "İki kartla mesajlaşma" projesini kur: A'ya basınca "Selam", B'ye basınca "Görüşürüz" gönder.
4. Bilerek `radio.on()` satırını silip mesajın gidip gitmediğini gözlemle, sonra geri ekle.

---

## Mini quiz

1. Kendi fonksiyonunu tanımlamak için hangi anahtar kelime kullanılır?
   a) `func`  b) `def`  c) `function`
2. Bir Python listesinin ilk elemanına nasıl ulaşılır?
   a) `liste[1]`  b) `liste[0]`  c) `liste[-0]`
3. `gorevler.append("d")` ne yapar?
   a) Listedeki ilk elemanı siler  b) Listenin sonuna yeni eleman ekler  c) Listeyi sıralar
4. Radyo ile mesaj gönderip almak için hangi satır şarttır?
   a) `radio.on()`  b) `import random`  c) `display.clear()`
5. `radio.receive()` hiçbir mesaj gelmediğinde ne döndürür?
   a) Hata verir  b) `None` (boş/hiçbir şey)  c) 0

<details>
<summary>Cevap anahtarı</summary>

1-b · 2-b · 3-b · 4-a · 5-b

</details>

---

## Öğretmen notu

- **1. ders saati:** def ile fonksiyon tanımlama (15 dk), liste oluşturma ve rastgele görev seçici (15 dk).
- **2. ders saati:** radio modülü ve iki kartla mesajlaşma (20 dk), kendini dene / radio.on() deneyi (10 dk).
- Bu hafta üç farklı konuyu (fonksiyon, liste, radyo) bir arada görmek yoğun gelebilir; hızlı gruplar üçünü de bitirebilir, yavaş gruplar için fonksiyon + liste yeterli bir hedef olarak bırakılabilir, radyo kısmı 28. hafta final projesinde isteyen gruplarca kullanılabilir.
- `radio.receive()`'in `None` döndürmesi (mesaj yoksa) yeni bir kavramdır; "boş kutu açmak gibi, hiçbir şey çıkmayabilir" benzetmesi faydalı olabilir.
- 28. hafta final projesiyle hem blok hem Python dönemini kapsayan bir sergi/sunum haftasına giriyoruz.
