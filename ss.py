import os
from ultralytics import YOLO

# Bu blok Windows'ta multiprocessing hatalarını engellemek için ŞARTTIR
if __name__ == '__main__':
    
    # 1. Yolları tanımla
    proje_yolu = "C:/Users/balci/OneDrive/Desktop/deneme_projesi"
    model_yolu = f"{proje_yolu}/runs/detect/train13_final/weights/best.pt"
    yaml_yolu = f"{proje_yolu}/data.yaml"

    # 2. Modeli yükle
    if os.path.exists(model_yolu):
        model = YOLO(model_yolu)
        
        print("Doğrulama (Validation) başlatılıyor...")
        
        # 3. Doğrulamayı çalıştır
        # workers=0 parametresini ekleyerek işlemci yükünü manuel de kontrol edebiliriz
        results = model.val(
            data=yaml_yolu,
            project=f"{proje_yolu}/runs/detect",
            name="val_final_v2",
            save=True,
            device=0, # RTX 3060'ı kullan
            workers=4 # Hata devam ederse burayı 0 yapabilirsin
        )
        
        print("İşlem tamamlandı! Sonuçlar val_final_v2 klasöründe.")
    else:
        print("HATA: Model dosyası bulunamadı!")