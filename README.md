Nesne Yönelimli Programlama (OOP) – Python Projesi
Özet

Bu proje, Nesne Yönelimli Programlama (Object-Oriented Programming - OOP) prensiplerinin Python dili kullanılarak uygulanmasını göstermektedir. Çalışma kapsamında Encapsulation, Inheritance, Polymorphism ve Abstraction kavramları basitleştirilmiş örnekler ile ele alınmıştır. Amaç, bu temel OOP prensiplerinin yazılım tasarımındaki kullanımını anlaşılır bir şekilde ortaya koymaktır.

1. Giriş

Nesne Yönelimli Programlama, yazılım geliştirmede “nesne” kavramına dayanan bir programlama paradigmıdır. Nesneler; veri (attributes) ve davranış (methods) içeren yapılardır.

OOP yaklaşımı, yazılım sistemlerini daha modüler, yeniden kullanılabilir ve bakımı kolay hale getirir.

Bu proje kapsamında OOP’nin temel prensipleri Python üzerinde örneklenmiştir.

2. Kullanılan OOP Prensipleri
   
2.1 Encapsulation (Kapsülleme)

Encapsulation, verilerin ve bu verilere ait metotların tek bir sınıf içinde toplanması ve dış erişime kontrollü şekilde kapatılmasıdır. Amaç, veri bütünlüğünü korumak ve yetkisiz erişimi engellemektir.

Bu projede:

Private değişkenler (__salary)
Getter ve setter metotları
kullanılarak veri kontrolü sağlanmıştır.

Temel kazanım:

Veri güvenliği
Kontrollü erişim
Hata riskinin azaltılması

2.2 Inheritance (Kalıtım)

Inheritance, bir sınıfın başka bir sınıfın özelliklerini ve metotlarını devralmasını sağlar. Bu sayede kod tekrarının önüne geçilir ve hiyerarşik yapı oluşturulur.

Bu projede:

Animal temel sınıf
Dog ve Cat türetilmiş sınıflar olarak kullanılmıştır.

Temel kazanım:

Kod tekrarının azaltılması
Genişletilebilir yapı
Mantıksal sınıf hiyerarşisi

2.3 Polymorphism (Çok Biçimlilik)

Polymorphism, aynı metot isminin farklı sınıflarda farklı davranışlar göstermesidir. Bu sayede ortak bir arayüz üzerinden farklı nesneler kullanılabilir.

Bu projede speak() ve eat() metotları farklı sınıflarda farklı çıktılar üretmektedir.

Temel kazanım:

Esnek yapı
Runtime davranış değişimi
Ortak arayüz kullanımı

2.4 Abstraction (Soyutlama)

Abstraction, bir sistemin yalnızca gerekli özelliklerini gösterip detaylarını gizleme prensibidir. Kullanıcıya “ne yapıldığı” bilgisi sunulur, “nasıl yapıldığı” bilgisi gizlenir.

Python’da abstraction, abstract class ve abstract method kullanılarak uygulanır.

Bu projede Payment adlı soyut sınıf, farklı ödeme yöntemleri için ortak bir yapı tanımlamaktadır.

Temel kazanım:

Standart arayüz oluşturma
Karmaşıklığın azaltılması
Zorunlu metot tanımlama
3. Ödeme Sistemi Örneği (Abstraction + Polymorphism)

Proje içerisinde gerçek bir kullanım senaryosu olarak ödeme sistemi modellenmiştir.

Ortak metot:

pay(amount)

Somut sınıflar:

Credit Card ödeme yöntemi
PayPal ödeme yöntemi

Bu yapı sayesinde farklı ödeme yöntemleri aynı arayüz üzerinden kullanılabilmektedir.

4. Proje Yapısı
OOP-Projesi/
│
├── Encapsulation/
├── Inheritance/
├── Polymorphism/
├── Abstraction/


Her klasör ilgili OOP prensibini açıklayan örnek kodları içermektedir.

5. Sonuç

Bu çalışma kapsamında OOP prensiplerinin Python üzerinde nasıl uygulanabileceği gösterilmiştir. Her bir prensip basitleştirilmiş örneklerle açıklanmıştır.

6. Geliştirici

Bu proje, Nesne Yönelimli Programlama kavramlarını öğrenmek ve uygulamak amacıyla hazırlanmıştır.
