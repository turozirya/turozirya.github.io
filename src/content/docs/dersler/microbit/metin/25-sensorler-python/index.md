---
# Yayına hazır olunca bu satırı sil:
draft: true
title: "25. Hafta – Sensörler Python ile"
description: 10. ve 11. haftadaki hareket, ışık ve sıcaklık sensörlerini bu kez MicroPython fonksiyonlarıyla okuyoruz.
sidebar:
  order: 25
hafta: 25
seviye: Python
sure: 2 ders saati
kazanimlar:
  - accelerometer, temperature ve light_level fonksiyonlarını kullanır.
  - was_gesture() ile hareket algılar.
  - Sensör verisiyle su terazisi ve gece lambası programı yazar.
makecode: ""
video: ""
---

## Bu hafta ne öğreneceğiz?

10. ve 11. haftalarda **ivme (mg)**, **ışık seviyesi**, **sıcaklık (°C)** bloklarını kullanmıştık. Bu hafta aynı sensörleri MicroPython fonksiyonlarıyla okuyup, su terazisi ve gece lambasını yazıyla yeniden yapacağız.

**Malzemeler:** micro:bit v2, USB kablo, bilgisayar.

---

## 1. İvmeölçer: accelerometer

| Blok | MicroPython |
| --- | --- |
| ivme (mg) x | `accelerometer.get_x()` |
| ivme (mg) y | `accelerometer.get_y()` |
| ivme (mg) z | `accelerometer.get_z()` |
| salla ise | `accelerometer.was_gesture("shake")` |

```python
from microbit import *

while True:
    x = accelerometer.get_x()
    if x > 300:
        display.show(Image.ARROW_E)
    elif x < -300:
        display.show(Image.ARROW_W)
    else:
        display.show(Image.ARROW_N)
```

Bu, 10. haftadaki su terazisinin birebir Python sürümü.

---

## 2. Işık ve sıcaklık

| Blok | MicroPython |
| --- | --- |
| ışık seviyesi | `display.read_light_level()` |
| sıcaklık (°C) | `temperature()` |

```python
from microbit import *

while True:
    if display.read_light_level() < 30:
        display.show(Image.ARROW_N)   # gerçek projede özel bir ampul deseni çizilebilir
    else:
        display.clear()

    if button_a.was_pressed():
        display.scroll(temperature())
```

Bu da 11. haftadaki gece lambası + termometrenin Python sürümü — mantık birebir aynı, sadece yazım değişti.

---

## 3. Hareket adları (gesture)

`was_gesture()` fonksiyonu içine yazılan metin, hangi hareketi aradığımızı belirtir. En sık kullanılanlar:

| Metin | Hareket |
| --- | --- |
| `"shake"` | Sallama |
| `"up"` / `"down"` | Ekran yukarı / aşağı bakıyor |
| `"left"` / `"right"` | Sola / sağa yatırma |
| `"face up"` / `"face down"` | Ekran yukarı / aşağı dönük duruyor |

```python
if accelerometer.was_gesture("left"):
    display.show(Image.ARROW_W)
```

:::note[Blok tarafında emin olmadığımız kısım]
12-17. haftalardaki blok derslerinde bu hareket adlarının Türkçe karşılıklarını canlı editörden doğrulayamadık; bu yüzden blok derslerinde eşik değer (ivme x/y sayısı) yöntemini kullandık. MicroPython'da ise bu İngilizce metin anahtarları resmî belgelerde net olarak tanımlı.
:::

---

## Kendini dene

1. Gece lambasına sıcaklık kontrolü de ekle: karanlıksa VE sıcaksa (`and`) farklı bir simge göster.
2. `was_gesture("left")` ve `was_gesture("right")` ile 4 yönlü bir "yön bulucu" yap.
3. Su terazisini y eksenini de kullanarak 4 yönlü hâle getir (ileri/arkaya eğim dahil).
4. Işık seviyesini her saniye `display.scroll()` ile sayı olarak göster, odanın farklı yerlerinde değerin nasıl değiştiğini gözlemle.

---

## Mini quiz

1. `accelerometer.get_x()` neyi döndürür?
   a) Sıcaklık  b) x eksenindeki eğim/ivme değeri  c) Işık seviyesi
2. Işık seviyesini okuyan fonksiyon hangisidir?
   a) `temperature()`  b) `display.read_light_level()`  c) `accelerometer.get_x()`
3. `was_gesture("shake")` hangi bloğa karşılık gelir?
   a) A tuşuna basıldığında  b) salla ise  c) pusulayı kalibre et
4. `temperature()` fonksiyonu neyi döndürür?
   a) Oda nemini  b) Çipin sıcaklığını (°C)  c) Pil seviyesini
5. Bu derste neden bazı hareket isimleri (gesture) İngilizce bırakıldı?
   a) Türkçesi yok çünkü bunlar kod içindeki sabit anahtar kelimeler  b) Unutulmuş  c) Çevrilemez bir teknik sebep var

<details>
<summary>Cevap anahtarı</summary>

1-b · 2-b · 3-b · 4-b · 5-a

</details>

---

## Öğretmen notu

- **1. ders saati:** Blok-Python fonksiyon eşleştirme tablolarını birlikte okuma (10 dk), su terazisini birlikte yazma (20 dk).
- **2. ders saati:** Gece lambası + termometre (15 dk), hareket adları tablosu ve kendini dene (20 dk).
- Bu hafta öğrencilerin çoğu "bunu zaten blok dönemimde yapmıştım" diyecek — bu iyi bir işarettir, amaç zaten aynı mantığı farklı bir dille tekrar görmek.
- `was_gesture()` içindeki metin anahtar kelimeleri (`"shake"`, `"left"` vb.) tam olarak yazılmalı; büyük/küçük harf ve yazım hatası sessizce çalışmaz (hata vermez, sadece hareketi hiç yakalamaz) — bu da iyi bir hata ayıklama örneğidir.
- 26. haftada ses ve müziğe, 27. haftada fonksiyon/liste/radyoya geçerek Python dönemini tamamlayacağız.
