---
# Yayına hazır olunca bu satırı sil:
draft: true
title: "19. Hafta – Bloktan metne geçiş"
description: Blokları bir kenara bırakıp gerçek bir programlama dili olan MicroPython ile yazmaya başlıyoruz.
sidebar:
  order: 19
hafta: 19
seviye: Python
sure: 2 ders saati
kazanimlar:
  - MicroPython'ın blok kodun yazıya dökülmüş hâli olduğunu açıklar.
  - python.microbit.org editörünü açıp kod yazabilir.
  - İlk MicroPython programını yazıp karta yükler.
makecode: ""
video: ""
---

## Bu hafta ne öğreneceğiz?

1–18. haftalarda blokları birbirine bağlayarak program yazdık. Bugün itibarıyla aynı mantığı kullanıp **yazarak** (metin tabanlı) kod yazmaya geçiyoruz. Kullanacağımız dil **MicroPython**: normal Python dilinin, micro:bit gibi küçük kartlara sığacak kadar küçültülmüş hâli. Korkma — blok dönemindeki tüm mantık (koşul, döngü, değişken) aynen geçerli; sadece bloklar yerine satırlar yazacağız.

**Malzemeler:** micro:bit v2, USB kablo, bilgisayar (internet tarayıcısı).

---

## 1. Blok ile yazı aslında aynı şeyi söylüyor

MakeCode'un sağ üstünde **Bloklar** / **JavaScript** geçiş düğmesi var. "JavaScript" görünümü, bloklarının bir benzerinin nasıl yazıyla ifade edildiğini gösterir. Bu bize fikir verir ama kullanacağımız dil JavaScript değil, **Python**'dır. Mantığı karşılaştıralım:

| Blok (MakeCode) | Yazı (MicroPython) |
| --- | --- |
| program başladığında | (dosyanın en üstü, otomatik çalışır) |
| her zaman | `while True:` |
| simgeyi göster | `display.show(Image.HAPPY)` |
| duraklat (ms) | `sleep(500)` |
| A tuşuna basıldığında | `if button_a.was_pressed():` |

:::tip[Hiçbir şey kaybolmadı]
"Her zaman" döngüsü, "eğer-ise" koşulu, değişkenler — hepsi MicroPython'da da var, sadece görünümleri değişti. 1–18. haftalarda öğrendiklerin boşa gitmedi.
:::

---

## 2. Gerçek araç: python.microbit.org

MicroPython yazmak için **python.microbit.org** adresindeki resmî çevrimiçi editörü kullanacağız. MakeCode'daki simülatör burada yok; kodu doğrudan karta yükleyip denersin.

**Kodu karta yükleme (iki yol):**

1. **Sürükle-bırak (her bilgisayarda çalışır):** Editördeki "İndir" düğmesiyle bir `.hex` dosyası indirilir, bu dosya micro:bit'in göründüğü USB sürücüsüne sürüklenir.
2. **Doğrudan bağlan (WebUSB, sadece Chrome/Edge):** "Bağlan" düğmesiyle tarayıcı karta doğrudan yükleme yapar; ilk bağlantıda tarayıcı izin ister.

:::note[Okulda hangisi?]
Okul bilgisayarlarında tarayıcı izinleri kısıtlıysa sürükle-bırak yöntemi her zaman çalışır. WebUSB daha hızlıdır ama her ortamda açık olmayabilir.
:::

---

## 3. İlk MicroPython kodun

Her MicroPython programı aynı satırla başlar — bu satır karttaki tüm hazır araçları (ekran, düğmeler, bekleme) kullanıma açar:

```python
from microbit import *

display.scroll("Merhaba")
display.show(Image.HAPPY)
```

- `from microbit import *` → "micro:bit'in bütün araçlarını kullanacağım" demektir, her programın ilk satırıdır.
- `display.scroll("...")` → yazıyı kaydırarak gösterir (bloktaki **dizgi göster**).
- `display.show(Image.HAPPY)` → hazır bir simge gösterir (bloktaki **simgeyi göster**).

Dikkat: Python'da metinler tırnak içinde (`"Merhaba"`), parantezler ve büyük/küçük harfler **tam doğru** yazılmalı; bir harf yanlışsa kod çalışmaz.

---

## Kendini dene

1. Kendi adını `display.scroll(...)` ile kaydır.
2. Art arda iki simge göster (aralarına `sleep(500)` ekleyerek — 20. haftada ayrıntılı göreceğiz, şimdilik dene).
3. MakeCode'da 3. haftadaki isim kartı kodunu aç, **JavaScript** görünümüne geç, hangi kelimelerin tanıdık geldiğini bul.
4. `display.scroll("Merhaba")` satırındaki bir tırnak işaretini sil, kodu yüklemeye çalış, ne olduğunu gözlemle, sonra düzelt.

---

## Mini quiz

1. MicroPython nedir?
   a) Yeni bir blok kategorisi  b) Python dilinin küçük kartlar için hâli  c) Bir simülatör
2. Her MicroPython programının ilk satırı nedir?
   a) `display.show()`  b) `from microbit import *`  c) `while True:`
3. Kodu karta yüklemenin her bilgisayarda çalışan yolu hangisidir?
   a) WebUSB ile bağlan  b) Sürükle-bırak (.hex dosyası)  c) Bluetooth
4. MakeCode'daki "JavaScript" görünümü hangi dili gösterir?
   a) Python  b) JavaScript  c) MicroPython
5. `display.scroll("Merhaba")` satırı bloktaki hangi bloğa benzer?
   a) simgeyi göster  b) dizgi göster  c) duraklat (ms)

<details>
<summary>Cevap anahtarı</summary>

1-b · 2-b · 3-b · 4-b · 5-b

</details>

---

## Öğretmen notu

- **1. ders saati:** Blok-yazı karşılaştırma tablosunu birlikte okuma (10 dk), MakeCode'da JavaScript görünümünü gösterme (10 dk), python.microbit.org'u tanıtma (10 dk), ilk kodu birlikte yazma (10 dk).
- **2. ders saati:** Karta yükleme (her iki yöntemi deneme, 15 dk), kendini dene 1-2 (15 dk), kasıtlı hata deneyi ve mini quiz (10 dk).
- Okul ağında WebUSB engellenmiş olabilir; ders öncesi bir bilgisayarda test edin, sürükle-bırak yöntemini her zaman yedek olarak gösterin.
- Bu hafta kod yazma hızını değil, "blok ile yazı aynı mantık" farkındalığını hedefleyin; hız sonraki haftalarda gelecek.
- 20. haftada girinti ve hata mesajı okumaya ayrıntılı gireceğiz; bu hafta öğrenciler hata görürse paniklemesinler, "normal" olduğunu söyleyin.
