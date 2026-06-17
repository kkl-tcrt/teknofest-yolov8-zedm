import cv2
import os
from ultralytics import YOLO

# 1. MODEL VE SINIF AYARLARI
model_dosyasi = r"C:/Proje/best.pt" 

#  data.yaml dosyasındaki sıra ile birebir aynı olmalı
ozel_isimler = {
    0: 'Stage_1', 1: 'Stage_2', 2: 'Stage_3', 3: 'Stage_4', 
    4: 'Stage_5', 5: 'Stage_6', 6: 'Stage_7', 7: 'Stage_8', 
    8: 'Stage_9', 9: 'Stage_10', 10: 'Stage_11', 
    11: 'Stage_11_cross', 12: 'Stop_Sign'
}

print("Sistem başlatılıyor")

if not os.path.exists(model_dosyasi):
    print(f"HATA: Model dosyası '{model_dosyasi}' adresinde bulunamadı!")
else:
    # 2. MODELİ YÜKLE
    model = YOLO(model_dosyasi)
    
    
    try:
        model.model.names = ozel_isimler
        print(" Model isimleri başarıyla senkronize edildi.")
    except Exception as e:
        print(f"İsimler güncellenirken bir sorun çıktı ama devam ediliyor: {e}")


    # 0 genellikle laptop kamerasıdır. ZED-M takarsan bu rakamı değiştirebiliriz.
    cap = cv2.VideoCapture(0) 

    print("\n--- TEST BAŞLADI ---")
    print(f"Aktif Sınıf Listesi: {model.model.names}")
    print("Çıkmak için 'q' tuşuna bas.\n")

    while True:
        ret, frame = cap.read()
        if not ret:
            print(" Kameradan görüntü alınamıyor!")
            break

        results = model.predict(frame, conf=0.45, imgsz=640, verbose=False)

        # 6. GÖRSELLEŞTİRME
        # results[0].plot() otomatik olarak kutuları ve senin YENİ isimlerini çizer
        annotated_frame = results[0].plot()
        
        # Ekranda göster
        cv2.imshow("Zehra Tabela Denetim Masasi", annotated_frame)

        # 7. ÇIKIŞ KONTROLÜ
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Kaynakları serbest bırak
    cap.release()
    cv2.destroyAllWindows()
    print(" Sistem kapatıldı.")