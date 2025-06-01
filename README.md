# 📦 Drone Filo Optimizasyonu: Çok Kısıtlı Ortamlarda Dinamik Teslimat Planlaması

## 🔍 Proje Amacı
Bu projede, enerji limitleri ve uçuş yasağı bölgeleri gibi dinamik kısıtlar altında çalışan drone'ların, **en verimli şekilde teslimat yapmalarını sağlayan algoritmalar** geliştirilmiştir. Hedef, **optimum rota planlaması**, **öncelik yönetimi**, **no-fly zone geçiş kontrolleri** ve **enerji tüketim analizlerinin** bir arada ele alındığı bir simülasyon ortamı sunmaktır.

## 📁 Klasör Yapısı

```
DroneFiloOptimizasyonu/
├── main.py
├── models.py
├── data_loader.py
├── data_generator.py
├── a_star.py
├── genetic_algorithm.py
├── constraints.py
├── utils.py
├── visualizer.py
├── test_performance.py
└── README.md
```

## ⚙️ Kurulum ve Çalıştırma

### 1. Gerekli kütüphaneleri yükle:
```bash
pip install matplotlib
```

### 2. Projeyi çalıştır:
```bash
python main.py
```

## 🧠 Kullanılan Algoritmalar

### ✅ A* Algoritması
- Düğümler: Teslimat noktaları
- Kenarlar: Drone hareketleri
- Heuristic: Mesafe + ceza
- No-fly zone kontrolü: Aktif zaman ve konum çakışması
- Kapasite ve enerji kısıtı: max_weight ve battery'e göre

### ✅ Genetik Algoritma (GA)
- Popülasyon: Geçerli rastgele rotalar
- Crossover: İki rotadan yeni rota
- Mutasyon: Rastgele teslimat değişimi
- Fitness: Teslimat sayısı yüksek, enerji ve ihlal düşükse iyi

## 🧪 Senaryolar ve Testler

| Senaryo | Açıklama                               |
|---------|----------------------------------------|
| 1       | 5 Drone, 20 Teslimat, 2 No-Fly Zone    |
| 2       | 10 Drone, 50 Teslimat, 5 No-Fly Zone   |

### Kullanılan Metrikler:
- ✅ Tamamlanan teslimat yüzdesi
- ⚡ Ortalama enerji tüketimi
- ⏱️  Algoritma çalışma süresi

## 📊 Örnek Konsol Çıktısı

```
📊 [GRAFİK] A* – Senaryo 1
🎨 Grafik çiziliyor: A* – Senaryo 1
📊 [GRAFİK] GA – Senaryo 1
🎨 Grafik çiziliyor: GA – Senaryo 1
📊 [TEST] Senaryo 1
🔍 Algoritma: A*
✅ Tamamlanan Teslimat: 61
⚡ Ortalama Enerji: 457.86
⏱️  Süre: 0.001 saniye
```

## 🗺️ Görselleştirme

- Matplotlib ile çizim yapılır.
- Drone rotaları renkli çizgilerle gösterilir.
- No-fly zone’lar kırmızı saydam çokgenlerle çizilir.

## 🧩 Geliştirme Notları

- Algoritmalar modüler yapıda dosyalanmıştır.
- `constraints.py` dosyası kısıtları kontrol eder.
- `run_all_once()` fonksiyonu sayesinde algoritmalar yalnızca bir kez çalışır.
- Kod IEEE raporu için uygundur.

## 🔗 GitHub Projesi

[https://github.com/EgehanSZ/DroneFiloOptimizasyonu](https://github.com/EgehanSZ/DroneFiloOptimizasyonu)

## 📃 Lisans

Bu proje eğitim amaçlı geliştirilmiştir. Herhangi bir ticari kullanımı önerilmez.