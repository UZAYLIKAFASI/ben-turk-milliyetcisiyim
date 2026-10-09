# Ben Türk Milliyetçisiyim
Ekranı tam ekran açıp turtle ile Türk bayrağı çizen, arkada müzik çalan küçük bir Python programı.

## Özellikler
- Kırmızı zemin üzerine ay ve yıldız çizimi (turtle)
- Açılışta müzik çalar (pygame)
- Tam ekran açılır, pencereye tıklayınca kapanır

## Teknolojiler
- Python 3, turtle (tkinter), pygame

## Kurulum
```
pip install -r requirements.txt
```

## Yapılandırma
Gerekmiyor.

## Kullanım
```
python bayrak.py
```
Kapatmak için ekrana tıkla.

## Klasör yapısı
```
bayrak.py                       # program
BENTURKMILLEYETCISIYIMLAN.mp3   # çalınan müzik
requirements.txt
```

## Durum
Arşiv (eski proje). Son yedek: 2025-02-15.

## Değişiklik notları
- Drive yedeğinden GitHub'a taşındı (2026-10-09).
- Derlenmiş `.exe` ve kısayol dosyası repoya eklenmedi.
- Müzik dosyası, program hangi klasörden çalıştırılırsa çalıştırılsın bulunacak şekilde script'in yanındaki konumdan yükleniyor.
