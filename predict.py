import os
from ultralytics import YOLO

# Kendi eğittiğiniz modeli yükleyin
model = YOLO('C:\\Users\\Hatice\\Downloads\\kayisi.v1i.yolov8 (1)\\runs\\detect\\train3\\weights\\best.pt')

# Test klasörünün yolunu belirleyin
test_images_folder = "test\images"
results_folder = "results"
os.makedirs(results_folder, exist_ok=True)

# Test klasöründeki her bir görüntüde tahmin yap ve kaydet
for idx, image_file in enumerate(os.listdir(test_images_folder), start=1):
    image_path = os.path.join(test_images_folder, image_file)

    # Tahminleri yap
    results = model.predict(source=image_path, conf=0.45, iou=0.45)

    # Tahmin edilen görüntüyü kaydet
    results[0].save(os.path.join(results_folder, f"prediction_{idx}.jpg"))
    print(f"Processed {image_file} - Results saved as prediction_{idx}.jpg in 'results' folder")

