from ultralytics import YOLO
import os

if __name__ == '__main__':

    os.chdir("C:/Users/balci/OneDrive/Desktop/deneme_projesi")


    model_yolu = "runs/detect/train12/weights/best.pt"
    if os.path.exists(model_yolu):
        print("train12 üzerinden devam ediliyor...")
        model = YOLO(model_yolu)
    else:
        model = YOLO("yolov8n.pt")


    model.train(
        data="data.yaml",
        epochs=100,          
        imgsz=640,
        device=0,            
        batch=16,            
        name="train13_final", # Sonuçlar bu klasöre kaydedilecek
        augment=True         # Tabelaları farklı açılardan tanıması için
    ) 