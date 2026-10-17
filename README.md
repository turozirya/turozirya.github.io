# kod_turozirya

Ortaokul robotik kodlama kulübü için micro:bit ders sitesi (Astro + Starlight).

## Siteyi bu bilgisayarda açmak

```
npx astro dev --background --host --port 8090
```

Tarayıcıda `http://localhost:8090` adresini aç. Durdurmak için: `npx astro dev stop`

Raspberry Pi'de derlemek için `npm run build:pi` kullan (arama özelliği Pi'de çalışmadığı için kapalı derler).

## Konu yazmak

Konular `src/content/docs/dersler/microbit/<hafta-klasörü>/` içindedir. Bir dosyayı açıp
"Hazırlanıyor" notunu silip yerine içeriği yaz. Dosyanın başındaki bilgiler:

```yaml
---
title: "Konu başlığı"
hafta: 5
seviye: Blok + Python
sure: 1 ders saati
kazanimlar:
  - Birinci kazanım.
  - İkinci kazanım.
makecode: https://makecode.microbit.org/_xxxx   # isteğe bağlı
video: https://www.youtube.com/watch?v=xxxx      # isteğe bağlı
---
```

Örnek olarak tamamlanmış sayfalar: `01-robot-nedir.md`, `22-kart-haritasi.md`, `25-led-ekran.md`.

Önerilen bölümler: Amaç → Malzemeler → Adım adım etkinlik → Kendini dene → Mini test → Öğretmen notu.
Cevapları ve öğretmen notunu gizlemek için:

```html
<details>
<summary>Öğretmen notu</summary>

Not buraya.

</details>
```

## Görsel eklemek

Görselleri haftanın dosyasının yanındaki `gorseller` klasörüne koy, adının başına hafta
numarasını yaz (Türkçe karakter ve boşluk kullanma):

```
dersler/microbit/blok/gorseller/02-makecode-arayuzu.png
dersler/microbit/metin/gorseller/19-python-editor.png
```

Ders dosyasında şöyle göster (köşeli parantez içi, görseli göremeyenler için açıklamadır):

```md
![MakeCode editörünün ana ekranı](./gorseller/02-makecode-arayuzu.png)
```

Site görselleri derlerken otomatik küçültür ve WebP biçimine çevirir; büyük fotoğraf koymak sorun değildir.
MakeCode'da blokların resmini almak için kod alanına sağ tıklayıp "Ekran görüntüsü" seçilebilir.

## Yeni ünite veya ders eklemek

Yeni ünite: `dersler/microbit/` altına yeni bir klasör aç ve `astro.config.mjs` içindeki
kenar menüye ekle (menü `src/kenar-menu-microbit.json` dosyasından gelir).
