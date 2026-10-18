---
title: "18. Hafta – Proje haftası 2"
description: Blok döneminin tamamını (1–17. haftalar) bir araya getirip kendi projemizi tasarlıyor ve sunuyoruz.
sidebar:
  order: 18
hafta: 18
seviye: Blok
sure: 2 ders saati
kazanimlar:
  - Blok döneminde öğrendiği sensör ve yapıları bir arada kullanır.
  - Kendi fikrine uygun bir proje planlar ve uygular.
  - Yaptığı projeyi sınıfa kısaca sunar.
makecode: ""
video: ""
---

## Bu hafta ne yapacağız?

1–17. haftalarda LED ekrandan radyoya, sensörlerden listelere kadar çok şey öğrendik. Bu, **blok döneminin kapanış haftası**: öğrendiklerimizin tamamından seçerek kendi projemizi tasarlayıp sunacağız. 19. haftadan itibaren aynı mantığı MicroPython ile yazmaya başlayacağız.

**Malzemeler:** micro:bit v2, USB kablo, bilgisayar.

---

## 1. Neler öğrendik? Hızlı tur

| Hafta | Konu | Elimizdeki araç |
| --- | --- | --- |
| 2–3 | Tanışma, LED ekran | simge/dizgi/sayı göster |
| 4–8 | Butonlar, değişkenler, koşullar, rastgele, döngüler | eğer-ise, her zaman, tekrarla |
| 10–12 | Hareket, ışık/sıcaklık, pusula | ivme, ışık seviyesi, sıcaklık, pusula yönü |
| 13 | Ses | ton çal, melodi çal, sound level |
| 14–15 | Radyo | radyo gönder/al, sinyal gücü |
| 16–17 | Fonksiyonlar, listeler, dokunmatik pinler | fonksiyon yarat, liste, pin basıldığında |

Bu tablo, proje seçerken "hangi araçları kullanabilirim?" sorusuna hızlı bir bakış sağlar.

---

## 2. Örnek proje: Adım sayar

**Fikir:** Kartı cebinde/elinde taşırken her sarsıntıyı (adımı) sayıp ekranda göstermek.

**Plan:**
1. `adim` değişkenini 0 yap.
2. **salla ise** olayında `adim` değişkenini 1 artır.
3. A tuşuna basılınca toplam adım sayısını göster.
4. B tuşuna basılınca sayaç sıfırlansın.

Bu proje 5. hafta (değişkenler), 7. hafta (salla ise) ve 4. hafta (butonlar) bilgisini birleştiriyor — yeni blok öğrenmeden, bildiklerimizle gerçek bir alet yaptık.

---

## 3. Kendi projeni seç

Aşağıdakilerden birini seç ya da kendi fikrini öner:

- **Hava durumu istasyonu:** sıcaklık + ışık seviyesini birlikte gösteren bir ekran.
- **Gizli şifre kilidi:** belirli bir pin dokunma sırasını doğru yapınca kilit açılan bir kod (17. hafta).
- **Sınıf trafik ışığı:** radyo ile uzaktan kumanda edilen bir trafik ışığı simülasyonu (14-15. hafta).
- **Müzik aleti:** üç pine farklı nota atanmış, pusula yönüne göre oktav değişen bir alet (12-13-17. haftalar).

:::tip[Önce plan]
9. haftada öğrendiğimiz gibi: önce adımları yaz, sonra kodla. "Hangi sensörü, hangi koşulu, hangi değişkeni kullanacağım?" sorularını kağıda dök.
:::

---

## Kendini dene

1. Projeni üç cümleyle tanımla: "Ne yapıyor, nasıl çalışıyor, hangi blokları kullanıyor?"
2. Projende en az iki farklı kategoriden (örnek: Girdi + Radyo) blok kullanmaya çalış.
3. Projeni bir arkadaşına göster, o denesin; senin görmediğin bir hatayı o bulabilir.
4. Sınıfa 1 dakikalık kısa bir sunum hazırla: ne yaptın, en çok neyde zorlandın?

---

## Mini quiz

1. Bu hafta neden yeni blok öğretilmiyor?  
   a) Bloklar tükendi  
   b) Blok dönemini öğrendiklerimizi kullanarak kapatıyoruz  
   c) Zaman kalmadı
2. Adım sayar projesinde adımı saymak için hangi olay kullanılır?  
   a) A tuşuna basıldığında  
   b) salla ise  
   c) radyo ile sayı alındığında
3. Bir projeye başlamadan önce önerilen ilk adım nedir?  
   a) Hemen kod yazmaya başlamak  
   b) Planı yazmak  
   c) Kartı sıfırlamak
4. "Farklı kategorilerden blok kullanmayı dene" önerisi neden verilir?  
   a) Zorunlu kural olduğu için  
   b) Öğrendiklerini birleştirme pratiği için  
   c) Hiçbir sebep yok
5. 19. haftadan itibaren ne değişecek?  
   a) Yeni bir kart kullanılacak  
   b) Aynı mantık MicroPython ile (yazarak) uygulanacak  
   c) Dersler bitecek

<details>
<summary>Cevap anahtarı</summary>

1-b · 2-b · 3-b · 4-b · 5-b

</details>

---

## Öğretmen notu

- **1. ders saati:** Hızlı tur tablosunu birlikte okuma (10 dk), proje seçimi ve planlama (20 dk), kodlamaya başlama (10 dk).
- **2. ders saati:** Kodlamayı tamamlama ve test etme (25 dk), kısa sunumlar (15 dk — her öğrenci/ikili 1 dakika).
- Bu hafta değerlendirme amaçlı kullanılabilir: öğrencinin hangi blokları doğru yerde kullandığına bakarak 1-17. haftalardaki eksik konular belirlenebilir.
- Zayıf kalan öğrenciler için "Adım sayar" örneği hazır bir şablon olarak sunulabilir; güçlü öğrenciler serbest proje fikirlerine yönlendirilebilir.
- Sunumlar kısa tutulmalı (1 dakika) — amaç jüri gibi değerlendirmek değil, "söz söyleme" ve "projesini özetleme" pratiği yaptırmaktır. 28. hafta final projesinde bu beceri daha kapsamlı kullanılacak.
