# kod_turozirya

Ortaokul robotik kodlama kulübü için micro:bit ders sitesi (Astro + Starlight).

## Siteyi bu bilgisayarda açmak

```
npx astro dev --background --host --port 8090
```

Tarayıcıda `http://localhost:8090` adresini aç. Durdurmak için: `npx astro dev stop`

Raspberry Pi'de derlemek için `npm run build:pi` kullan (arama özelliği Pi'de çalışmadığı için kapalı derler).

## Konu yazmak

Haftalar `src/content/docs/dersler/microbit/blok/` (1–18) ve `metin/` (19–28) içindedir. Bir dosyayı açıp
"Hazırlanıyor" notunu silip yerine içeriği yaz. Dosyanın başındaki bilgiler:

```yaml
---
title: "5. Hafta – Değişkenler"
hafta: 5
seviye: Blok (MakeCode)
sure: 2 ders saati
kazanimlar:
  - Birinci kazanım.
  - İkinci kazanım.
makecode: https://makecode.microbit.org/_xxxx   # isteğe bağlı
video: https://www.youtube.com/watch?v=xxxx      # isteğe bağlı
---
```

Örnek olarak tamamlanmış hafta: `blok/01-temeller.md`.

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

Yeni hafta: `blok/` veya `metin/` klasörüne `NN-konu-adi.md` dosyası ekle; menüde kendiliğinden görünür.

Yeni ders (örn. Scratch): `dersler/` altına yeni bir klasör aç ve `astro.config.mjs` içindeki
`sidebar` listesine bir grup olarak ekle.
