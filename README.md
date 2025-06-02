# 🍑 Kayısı Tespiti – YOLOv8 ile Görüntü İşleme Projesi

Bu proje, **YOLOv8** nesne tespiti modeli kullanılarak kayısı meyvesinin görüntülerde tespit edilmesini amaçlamaktadır. Proje, özel olarak oluşturulmuş bir veri kümesi üzerinde eğitilmiş olup, tespit sonuçları görselleştirilmiştir.

## 📁 Proje Yapısı

```
├── kayisi-1/             # Eğitim veri kümesi (Roboflow'dan alınmış)
├── train/                # Eğitim görüntüleri
├── valid/                # Doğrulama görüntüleri
├── test/                 # Test görüntüleri
├── runs/detect/          # YOLOv8 tespit sonuçları
├── results/              # Sonuçların görselleri
├── data.yaml             # Veri kümesi yapılandırma dosyası
├── yolov8n.pt            # YOLOv8n model ağırlıkları
├── main.py               # Eğitim ve değerlendirme betiği
├── predict.py            # Görüntü üzerinde tespit betiği
├── README.dataset.txt    # Veri kümesi açıklamaları
├── README.roboflow.txt   # Roboflow veri kümesi bilgileri
└── LICENSE.txt           # Apache 2.0 lisans dosyası
```

## ⚙️ Kurulum ve Kullanım

### 1. Gerekli Kütüphanelerin Kurulumu

Python ortamınızı hazırlayın ve gerekli kütüphaneleri yükleyin:

```bash
pip install ultralytics
```

### 2. Model Eğitimi

Eğer modeli yeniden eğitmek isterseniz, aşağıdaki komutu kullanabilirsiniz:

```bash
yolo task=detect mode=train model=yolov8n.pt data=data.yaml epochs=50 imgsz=640
```

### 3. Görüntü Üzerinde Tespit

Eğitilmiş model ile bir görüntü üzerinde tespit yapmak için:

```bash
python predict.py --source path/to/image.jpg --weights yolov8n.pt --conf 0.5
```

### 4. Sonuçların Görselleştirilmesi

Tespit sonuçları `runs/detect/` klasöründe görseller olarak kaydedilecektir.

## 📝 Notlar

- `data.yaml` dosyası, eğitim, doğrulama ve test veri yollarını ve sınıf etiketlerini içerir.
- `predict.py` betiği, tek bir görüntü veya klasör üzerinde tespit yapabilir.
- `main.py` betiği, eğitim ve değerlendirme süreçlerini otomatikleştirir.

## 📄 Lisans

Bu proje [Apache 2.0 Lisansı](LICENSE.txt) ile lisanslanmıştır.

---

👩‍💻 Geliştirici: Hatice Gazel  
📫 GitHub: [@gazellhatice](https://github.com/gazellhatice)
