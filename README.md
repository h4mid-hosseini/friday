# friday
Friday is an IoT survilance system for detecting mothion, temprature, humidity and light!

این سیستم اطلاعات سنسورهای دما، رطوبت، نور و حرکت رو میفرسته به سرور و همچنین دستور خاموش و روشن کردن دوتا وسیله برقی رو از سرور میگیره و اعمال میکنه.

بکند سرور رو با جنگو نوشتم و nodemuc رو با Arduino IDE  کد نویسی کردم.

برای نصب پیش نیازهای راه اندازی سرور فایل requirements.txt رو با دستور pip نصب کنید.



وسائل مورد نیاز این پروژه:

۱. ماژول nodemcu

۲. سنسور دما و رطوبت DHT11

۳. سنسور تشخیص حرکت PIR HC-SR501

۴. یک عدد LDR

۵. یک عدد مقاومت ۱۰ کیلو اهم

۶. دو عدد رله ۵ ولت برای کنترل وسائل برقی

۷. یه مقدار سیم جامپر :)

۸. نرم افزار آردوینو

بعد از کلون کردن پروژه با نصب نرم افزار اردوینو مراحل زیر را برای نصب کتابخانه های مورد نیاز دنبال کنید.


1.  به بخش file>preferences بروید. 

2. در بخش Additional Board Manager URLs آدرس زیر را وارد کنید. http://arduino.esp8266.com/stable/package_esp8266com_index.json

3. به بخش Tools>Boards> Boards Manager رفته و ESP8266 را جستجو کنید و آن را نصب کنید. 




اتصالات سنسور ها و رله ها به این صورت می باشد:


LRD:

A0=> LDR => 10k ohm =>3.3V



PIR:

vin => 3.3v

gnd => nodemcu gnd

out => D7 nodemcu



DHT11:

gnd => nodemcu gnd

vin => 3.3v

out => D2 nodemcu

