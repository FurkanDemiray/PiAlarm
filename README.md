# PiAlarm
PiAlarm temel olarak güvenlik kameralarının görüntüyü analiz edebilecek seviyeye gelmesi için yapılmış bir çalışmadır. 
Bu çalışma içerisinde görüntü işleme, yapay zekâ, nesnelerin interneti gibi teknolojiler kullanılmıştır.
İlk aşama olarak hareket algılayıcı sensor ile bir tetiklenme beklenmekte. Daha sonra ise bu tetikleyici kamera modülünü açarak analize başlamakta. Önce bir fotoğraf alıyor sonrasında 15 saniye analiz yaparak görülen tüm nesneleri analiz ederek mail modülüne bir string olarak gönderiyor. Mail modülü fotoğraf ve nesne isimlerini maile ekleyerek söz konusu maile gönderiyor.
Proje Raspberry Pi adlı mikroişlemci ile gerçekleştirilmiştir. İşletim sistemi olarak ise debian tabanlı Raspbian OS kullanılmıştır.

*Uygulamanın çalışması için OpenCV yüklü olması gerekiyor.

Çalışmada, CSI arayüzü ile bağlanılan PiCam ve PIR sensörü kullanılmıştır.

![](https://github.com/FurkanDemiray/PiAlarm/blob/master/picam.png)
![](https://github.com/FurkanDemiray/PiAlarm/blob/master/pir.jpg)
