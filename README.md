# LiveStream_with_Socket
Teknofest 2023 Savaşan İHA Yarışması Canlı Yayın Aktarımı ve Video Kaydı
## Proje Teknofest Savasan İHA Yarısması kapsamında canlı yayın haberlesmesini gerceklestirmek üzere hazırlanmıştır. Kodlar, Teknofest 2023 Savaşan İHA Finalisti olan VEGA Havacılık ve Uzay Takımı tarafından kullanılmıştır.

Sistemin çalışma prensibi, IP eşitlemesinin ardından socket kütüphanesi ile görüntü haberleşmesinin gerçekleştirilmesidir. VEGA takımı sistemi, WiFi haberleşmesi ile kullanmıştır.
<br/>
 Kaydedilen video Teknofest Sunucu heyetine FileZilla Client ile aktarılmaktadır. Projeyi kullanacak olan takımların, kayıt işlemi sonrası IP adresleri ile birlikte FileZilla Client üzerinden oturum açmaları gerekmektedir.
<br/>

# Videonun Anlık Olarak Sunucuya Basılması İşlemi
Videounun anlık olarak sunucuya basılması işlemini terminal üzerinden aşağıdaki kod ile gerçekleştirebilirsiniz.
```
“ffmpeg.exe –i udp://@127.0.0.1:1111 –c:v h264 –b:v 2M –g 12 –c:a aac –b:a
128k –f mpegts udp://@235.10.10.10:1001” 
```
Bu kodu çalıştırabilmek için açık kaynak kütüphaneli ffmpeg uygulamasını indirmiş olmanız gerekmektedir
## YAZARLAR:
[@ofarukusta](https://github.com/ofarukusta) <br/>
[@eceilk](https://github.com/eceilk) <br/>
[@esmanurcigdem](https://github.com/esma4)
