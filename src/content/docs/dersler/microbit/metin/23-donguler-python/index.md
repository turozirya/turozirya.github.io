---
# Yayına hazır olunca bu satırı sil:
draft: true
title: "23. Hafta – Döngüler"
description: while True, for ve range ile 8. haftadaki döngüleri bu kez MicroPython ile yazıyoruz.
sidebar:
  order: 23
hafta: 23
seviye: Python
sure: 2 ders saati
kazanimlar:
  - while True ve for döngülerinin farkını açıklar.
  - range() fonksiyonunu belirli sayıda tekrar için kullanır.
  - Döngülerle geri sayım ve LED tarama programı yazar.
makecode: ""
video: ""
---

## Bu hafta ne öğreneceğiz?

19-22. haftalarda `while True` döngüsünü zaten kullandık ama üzerinde durmadık. Bu hafta 8. haftadaki üç döngü türünü (her zaman, tekrarla, olduğunda) MicroPython karşılıklarıyla eşleştirip, `for` ve `range()` ile tanışacağız.

**Malzemeler:** micro:bit v2, USB kablo, bilgisayar.

---

## 1. Üç döngünün Python karşılığı

| Blok | MicroPython | Ne zaman durur? |
| --- | --- | --- |
| her zaman | `while True:` | Hiç durmaz (kart kapanana kadar) |
| … kere tekrarla | `for i in range(n):` | n kere tekrar edince |
| … olduğunda | `while kosul:` | Koşul yanlış olunca |

```python
from microbit import *

while True:                 # her zaman
    for i in range(3):      # 3 kere tekrarla
        display.show(Image.SQUARE)
        sleep(300)
        display.clear()
        sleep(300)
    sleep(2000)
```

---

## 2. range() nasıl çalışır?

`range(n)` 0'dan `n-1`'e kadar sayar — toplam `n` kere. `range(3)` → 0, 1, 2 (3 sayı).

```python
for i in range(5):
    display.scroll(str(i))
```

Bu kod sırayla 0, 1, 2, 3, 4 gösterir — 20. haftadaki sayaç mantığıyla aynı sonucu, tek satırda alırız.

:::tip[i değişkeni ne işe yarıyor?]
`i`, döngünün her turunda otomatik değişen bir sayaçtır; "şu an kaçıncı turdayız" bilgisini taşır. İstersen `display.show(i)` ile bu sayıyı da gösterebilirsin.
:::

---

## 3. while ile koşullu döngü (olduğunda)

8. haftadaki geri sayım örneğini hatırlıyoruz:

```python
from microbit import *

while True:
    if button_b.was_pressed():
        sayi = 5
        while sayi > 0:       # "olduğunda" döngüsü
            display.show(sayi)
            sleep(1000)
            sayi -= 1
        display.show(Image.YES)
```

`while sayi > 0:` tam olarak bloktaki **sayı > 0 olduğunda** ile aynı iş yapıyor: koşul doğru olduğu sürece tekrarlar.

---

## 4. LED tarama

Ekrandaki bir noktayı soldan sağa kaydırmak için `for` ve koordinatları kullanırız:

```python
from microbit import *

while True:
    for x in range(5):
        display.clear()
        display.set_pixel(x, 2, 9)   # x: sütun, 2: orta satır, 9: en parlak
        sleep(150)
```

`display.set_pixel(x, y, parlaklik)` tek bir LED'i yakar — 3. haftadaki **led yak** bloğunun MicroPython karşılığıdır.

---

## Kendini dene

1. `range(3)` yerine `range(10)` yazıp geri sayımı 10'dan başlat.
2. LED taramasını önce sağa, sonra sola gidecek şekilde genişlet (ipucu: ikinci bir `for` ile `range(4, -1, -1)` dene).
3. `for i in range(5):` döngüsünde her turda `i`'yi ekranda göster, sonsuz döngü olmadığını gözlemle.
4. Bilerek `while sayi > 0:` içinde `sayi -= 1` satırını sil, simülatörde/kartta ne olduğunu gözlemle (sonsuz döngü!), sonra düzelt.

---

## Mini quiz

1. `while True:` hangi blok döngüsüne karşılık gelir?
   a) tekrarla  b) her zaman  c) olduğunda
2. `range(4)` kaç sayı üretir?
   a) 3  b) 4  c) 5
3. `range(4)` hangi sayılarla başlar ve biter?
   a) 1,2,3,4  b) 0,1,2,3  c) 0,1,2,3,4
4. `while sayi > 0:` hangi blok döngüsüne karşılık gelir?
   a) her zaman  b) tekrarla  c) olduğunda
5. `display.set_pixel(x, y, parlaklik)` ne yapar?
   a) Ekranı temizler  b) Tek bir LED'i belirtilen parlaklıkla yakar  c) Melodi çalar

<details>
<summary>Cevap anahtarı</summary>

1-b · 2-b · 3-b · 4-c · 5-b

</details>

---

## Öğretmen notu

- **1. ders saati:** Üç döngünün blok-Python eşleştirme tablosu (10 dk), range() kavramı ve 0'dan başlama (15 dk), LED tarama örneği (15 dk).
- **2. ders saati:** while ile geri sayım (10 dk), kendini dene (20 dk), sonsuz döngü deneyi (10 dk).
- `range(n)`'in `n-1`'de bittiğini (0'dan başladığı için) göstermek için tahtada sayıları tek tek yazdırmak faydalı; 16. haftadaki liste indeksleme mantığıyla aynı "0'dan başlama" kuralı burada tekrar karşımıza çıkıyor.
- Sonsuz döngü deneyini (kendini dene 4) kesinlikle yaptırın — hata ayıklama (debug) becerisi derste en çok bu tür "bilerek bozup düzeltme" alıştırmalarıyla gelişir.
- 24. haftada random modülüyle zar ve tahmin oyunlarına geçeceğiz.
