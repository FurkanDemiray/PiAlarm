# PiAlarm
PiAlarm temel olarak güvenlik kameralarının görüntüyü analiz edebilecek seviyeye gelmesi için yapılmış bir çalışmadır. 
Bu çalışma içerisinde görüntü işleme, yapay zekâ, nesnelerin interneti gibi teknolojiler kullanılmıştır.
İlk aşama olarak hareket algılayıcı sensor ile bir tetiklenme beklenmekte. Daha sonra ise bu tetikleyici kamera modülünü açarak analize başlamakta. Önce bir fotoğraf alıyor sonrasında 15 saniye analiz yaparak görülen tüm nesneleri analiz ederek mail modülüne bir string olarak gönderiyor. Mail modülü fotoğraf ve nesne isimlerini maile ekleyerek söz konusu maile gönderiyor.
Proje Raspberry Pi adlı mikroişlemci ile gerçekleştirilmiştir. İşletim sistemi olarak ise debian tabanlı Raspbian OS kullanılmıştır.

*Uygulamanın çalışması için OpenCV yüklü olması gerekiyor.
*Çalışmada, CSI arayüzü ile bağlanılan PiCam ve PIR sensörü kullanılmıştır.
*Bu çalışmada PIR sensörü 23 numaralı pine bağlanmıştır.

![](https://github.com/FurkanDemiray/PiAlarm/blob/master/picam.png)
![](https://github.com/FurkanDemiray/PiAlarm/blob/master/pir.jpg)

### Run

Uygulamanın bulunduuğu dizine gidiyoruz.

`$ cd [klasör_Adi]`

Öncelikle env aktif hale getiriyoruz.

`$ source tflite1-env/bin/activate`

Daha sonra `<starter.py>` çalıştırıyoruz.

`$ python3 starter.py`

### Ekran Görüntüleri

> 15 sn. boyunca süren analiz.

![](https://github.com/FurkanDemiray/PiAlarm/blob/master/screenshot.png)

> Her karede tespit edilmiş tüm nesneler ve tahmini doğruluk oranları.

![](https://github.com/FurkanDemiray/PiAlarm/blob/master/obj_exam1.png)

> Nesnelerin benzersiz ve doğruluk ortalaması alınmış hali.

![](https://github.com/FurkanDemiray/PiAlarm/blob/master/obj_exam2.png)
