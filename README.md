# kod_turozirya

Ortaokul robotik kodlama kulübü için micro:bit ders sitesi (Astro + Starlight).

## Siteyi bu bilgisayarda açmak

```
npx astro dev --background --host --port 8090
```

Tarayıcıda `http://localhost:8090` adresini aç. Durdurmak için: `npx astro dev stop`

Raspberry Pi'de derlemek için `npm run build:pi` kullan (arama özelliği Pi'de çalışmadığı için kapalı derler).

## Hafta yazmak

Her hafta kendi klasöründedir; haftanın metni `index.md`, görselleri aynı klasörde durur:

```
src/content/docs/dersler/microbit/
  blok/                       1–18. haftalar (MakeCode)
    01-temeller/
      index.md
      robot-parcalari.svg
      semsiye-akis-semasi.svg
    02-microbit-ile-tanisma/
      index.md
  metin/                      19–28. haftalar (MicroPython)
```

Haftanın `index.md` dosyasını açıp "Hazırlanıyor" notunu silip yerine içeriği yaz.
Tamamlanmış örnek: `blok/01-temeller/index.md`. Dosyanın başındaki bilgiler:

```yaml
---
title: "5. Hafta – Değişkenler"
sidebar:
  order: 5
hafta: 5
seviye: Blok (MakeCode)
sure: 2 ders saati
kazanimlar:
  - Birinci kazanım.
  - İkinci kazanım.
makecode: ""   # MakeCode paylaşım bağlantısı (isteğe bağlı)
video: ""      # YouTube bağlantısı (isteğe bağlı)
---
```

Önerilen bölümler: Amaç → Malzemeler → Adım adım etkinlik → Kendini dene → Mini quiz → Öğretmen notu.
Cevapları gizlemek için:

```html
<details>
<summary>Cevap anahtarı</summary>

Cevaplar buraya.

</details>
```

## Görsel eklemek

Görseli haftanın klasörüne koy (Türkçe karakter ve boşluk kullanma) ve `index.md` içinde göster.
Köşeli parantez içi, görseli göremeyenler için açıklamadır:

```md
![Robotun 3 parçası: sensör, işlemci, eylemci](./robot-parcalari.svg)
```

PNG, JPG ve SVG kullanılabilir. Site fotoğrafları derlerken otomatik küçültür ve WebP biçimine çevirir.
MakeCode'da blokların resmini almak için kod alanına sağ tıklayıp "Ekran görüntüsü" seçilebilir.

## Yeni ünite veya ders eklemek

Yeni hafta: `blok/` veya `metin/` içine `NN-konu-adi/index.md` klasörü ekle; menüde kendiliğinden görünür.

Yeni ders (örn. Scratch): `dersler/` altına yeni bir klasör aç ve `astro.config.mjs` içindeki
`sidebar` listesine bir grup olarak ekle.
