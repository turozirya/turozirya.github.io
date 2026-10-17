---
title: "1. Hafta – Temeller"
description: Robot, algoritma, akış şeması, hata ayıklama ve kodlama türleriyle tanışıyoruz.
sidebar:
  order: 1
hafta: 1
seviye: Hazırlık (bilgisayarsız)
sure: 2 ders saati
kazanimlar:
  - Robotun sensör, işlemci ve eylemci parçalarını örneklerle açıklar.
  - Günlük hayattan bir işi sıralı adımlarla algoritma olarak yazar.
  - Temel akış şeması sembollerini tanır ve basit bir akış şeması çizer.
  - Bir algoritmadaki hatayı bulup düzeltir.
  - Blok tabanlı ve metin tabanlı kodlamayı karşılaştırır.
makecode: ""
video: ""
---

## Bu hafta ne öğreneceğiz?

Bu hafta micro:bit'e dokunmadan önce, bütün yıl işimize yarayacak temel kavramları öğreneceğiz: robot nedir, bilgisayara nasıl "ne yapacağını" söyleriz ve bir şey ters gidince ne yaparız?

**Malzemeler:** Kâğıt, kalem, renkli kalemler. Bilgisayar gerekmez.

---

## 1. Robot nedir?

Robot; çevresini algılayan, algıladığına göre karar veren ve bu karara göre hareket eden bir makinedir. Her robotun üç temel parçası vardır:

| Parça | Görevi | İnsandaki karşılığı | Örnek |
| --- | --- | --- | --- |
| **Sensör** (algılayıcı) | Çevreden bilgi toplar | Göz, kulak, deri | Işık sensörü, sıcaklık sensörü, buton |
| **İşlemci** (beyin) | Bilgiyi değerlendirir, karar verir | Beyin | micro:bit'in içindeki çip |
| **Eylemci** (hareket eden parça) | Kararı uygular | Kaslar, ses telleri | Motor, LED, hoparlör |

**Örnek – Otomatik kapı:**
Kapının üstündeki sensör birinin yaklaştığını algılar → işlemci "kapıyı aç" kararı verir → motor (eylemci) kapıyı açar.

:::tip[Biliyor muydun?]
micro:bit'in üzerinde hem sensörler (butonlar, ışık, sıcaklık, hareket sensörü) hem işlemci hem de eylemciler (25 LED, hoparlör) bulunur. Yani küçük bir robot beyni gibidir!
:::

**Düşün:** Robot süpürge, akıllı saat ve trafik ışığı – her birinin sensörü, işlemcisi ve eylemcisi ne olabilir?

---

## 2. Algoritma nedir?

**Algoritma**, bir işi yapmak veya bir problemi çözmek için izlenen, sırası belli adımlardır. Bilgisayarlar kendi kendine düşünemez; onlara her adımı açıkça söylememiz gerekir.

**Günlük hayattan örnek – Diş fırçalama algoritması:**

1. Diş fırçasını al.
2. Fırçayı ıslat.
3. Fırçaya diş macunu sür.
4. Dişlerini 2 dakika fırçala.
5. Ağzını çalkala.
6. Fırçayı yıka ve yerine koy.

Başka örnekler: kek tarifi, okula gidiş yolu, çay demleme, bir oyunun kuralları.

---

## 3. Akış şeması sembolleri

**Akış şeması**, bir algoritmayı şekillerle gösterir. Her şeklin bir anlamı vardır:

| Sembol | Adı | Ne zaman kullanılır? |
| --- | --- | --- |
| ⬭ Oval | Başla / Bitir | Algoritmanın başı ve sonu |
| ▭ Dikdörtgen | İşlem | Yapılacak bir iş: "Fırçayı ıslat" |
| ▱ Paralelkenar | Giriş / Çıkış | Bilgi almak veya göstermek: "Sayıyı oku", "Ekrana yaz" |
| ◇ Eşkenar dörtgen | Karar | Evet/Hayır sorusu: "Yağmur yağıyor mu?" |
| → Ok | Akış yönü | Adımların hangi sırayla ilerlediği |

**Örnek – Dışarı çıkarken şemsiye almalı mıyım?**

```
   ( Başla )
       ↓
 [ Hava durumuna bak ]
       ↓
 < Yağmur yağıyor mu? >
   Evet ↓        ↘ Hayır
 [ Şemsiye al ]    ↓
       ↓          ↓
   ( Dışarı çık – Bitir )
```

**Etkinlik:** "Sabah okula hazırlanma" algoritmanın akış şemasını çiz. En az bir karar (◇) kullan. Örneğin: "Hava soğuk mu?"

---

## 4. Sıralı adımlar: Neden sıra önemli?

Bilgisayar komutları **yazıldığı sırayla** çalıştırır. Sıra değişirse sonuç da değişir.

**Hangisi doğru?**

| A | B |
| --- | --- |
| 1. Çorabı giy | 1. Ayakkabıyı giy |
| 2. Ayakkabıyı giy | 2. Çorabı giy |

B'de çorap ayakkabının üstüne giyilir. Adımların hepsi doğru, ama **sıra yanlış** olduğu için sonuç yanlış!

:::note[Robota komut verme oyunu]
Bir öğrenci "robot", bir öğrenci "programcı" olur. Programcı yalnızca şu komutları kullanabilir: **ileri git (1 adım)**, **sağa dön**, **sola dön**, **al**. Robot, sınıftaki bir kalemi alıp masaya bırakmalıdır. Robot yalnızca söyleneni yapar, tahmin yürütmez!
:::

---

## 5. Hata ayıklama (debug) nedir?

Algoritmada ya da kodda yapılan yanlışa **hata (bug)**, bu hatayı bulup düzeltmeye **hata ayıklama (debug)** denir. Hata yapmak kodlamanın normal bir parçasıdır; iyi programcılar hatayı hızlı bulanlardır.

**Hatayı bul – Çay demleme algoritması:**

1. Demliğe çay koy.
2. Çaydanlığı ocağa koy.
3. Kaynamış suyu demliğe dök.
4. Çaydanlığa su doldur.
5. 15 dakika demlenmesini bekle.

<details>
<summary>Cevabı gör</summary>

4. adım yanlış yerde! Su doldurulmadan çaydanlık ocağa konmuş ve kaynamamış su dökülmüş. Doğru sıra: 4 → 2 → 1 → 3 → 5 (ya da 1'i en başa alabilirsin).

</details>

**Hata ayıklama adımları:**

1. Sonucu beklenenle karşılaştır: Ne olmalıydı, ne oldu?
2. Adımları tek tek takip et.
3. Hatanın olduğu adımı bul.
4. Düzelt ve tekrar dene.

---

## 6. Blok tabanlı ve metin tabanlı kodlama

Bilgisayara komut vermenin iki yaygın yolu vardır:

| | Blok tabanlı | Metin tabanlı |
| --- | --- | --- |
| Nasıl yazılır? | Renkli blokları sürükleyip birleştirerek | Komutları klavyeyle yazarak |
| Örnek araç | MakeCode, Scratch | Python, MicroPython |
| Yazım hatası | Olmaz, bloklar birbirine uymazsa birleşmez | Olabilir: tek harf hatası kodu durdurur |
| Kimler için? | Başlangıç için çok uygun | Daha ileri seviye, profesyonel kullanım |

**Aynı komut, iki farklı yazım (micro:bit ekranında kalp göstermek):**

- Blok: **[ simge göster ❤ ]**
- MicroPython:

```python
from microbit import *
display.show(Image.HEART)
```

:::tip[Yol haritamız]
Bu yıl önce MakeCode bloklarıyla başlayacağız, sonra aynı işleri MicroPython ile yazmayı öğreneceğiz.
:::

---

## Kendini dene

1. Evindeki bir cihazı seç (çamaşır makinesi, buzdolabı, klima…). Sensörünü, işlemcisini ve eylemcisini yaz.
2. "Sandviç yapma" algoritmasını en az 6 adımla yaz.
3. Bu algoritmanın akış şemasını çiz ve bir karar adımı ekle ("Peynir var mı?").
4. Algoritmana bilerek bir hata koy, arkadaşın bulmaya çalışsın.

---

## Mini quiz

1. Robotun çevreden bilgi toplayan parçası hangisidir?
   a) Eylemci  b) Sensör  c) İşlemci
2. Akış şemasında karar adımı hangi şekille gösterilir?
   a) Oval  b) Dikdörtgen  c) Eşkenar dörtgen
3. Bir işi yapmak için izlenen sıralı adımlara ne denir?
   a) Algoritma  b) Sensör  c) Debug
4. Koddaki hatayı bulup düzeltme işine ne denir?
   a) Derleme  b) Hata ayıklama (debug)  c) Kaydetme
5. Aşağıdakilerden hangisi metin tabanlı bir dildir?
   a) Scratch  b) MakeCode blokları  c) Python

<details>
<summary>Cevap anahtarı</summary>

1-b · 2-c · 3-a · 4-b · 5-c

</details>

---

## Öğretmen notu

- **1. ders saati:** Robot ve 3 parçası (10 dk), algoritma ve diş fırçalama örneği (10 dk), robota komut verme oyunu (20 dk).
- **2. ders saati:** Akış şeması sembolleri ve şemsiye örneği (15 dk), çay demleme hata ayıklama etkinliği (10 dk), blok/metin karşılaştırması (5 dk), mini quiz (10 dk).
- Robota komut verme oyununda "robot" öğrencinin komutları birebir uygulaması, belirsiz komutların neden işe yaramadığını göstermek için en etkili andır.
- Haftanın sonunda micro:bit kartını yalnızca gösterin; sensör, işlemci ve eylemcilerini birlikte bulmak 2. haftaya merak bırakır.
