### Task1

Register qilish uchun link:
```
http://127.0.0.1:8000/api/v1/register/
```

Login qilish uchun link:
```
http://127.0.0.1:8000/api/v1/login/
```

Delete qilish uchun link:
```
http://127.0.0.1:8000/api/v1/delete/<int:pk>/
```

### Task2

Vakansilarni filter qilish uchun link: <br>
```
http://127.0.0.1:8000/api/v2/vacancies?salary_from=6000&salary_to=7000
```
yoki<br>
```
http://127.0.0.1:8000/api/v2/vacancies?salary=5000
```

### Task3

Product yaratish uchun ushbu linkga POST request yuboring:
```
http://127.0.0.1:8000/api/v3/products/
```

```
{
    "price": 11.8,
    "marja": 14.7,
    "package_code": "Code1",
}
```

### Task4
Sport musobaqalari uchun quyidagi modellar yaratilgan:
1. Sport
2. Team
3. Player
4. Match
5. Goal
6. Card

### Task5
LeetCode misollari leetcode1.py va leetcode2.py fayllarida yechilgan.
Kodni leetcodeni ozida run qilish tavsiya etiladi.


### CleanCode
Iloji boricha clean kod yozishga harkat qildim.


-------------------------------------------------------------------------------------

Backend Python Django yakuniy imtihoni
1-topshiriq (5 ball)

Soft Delete:
User modelini “soft delete” qilib o’chiring. User modelida bitta unique field bo’lsin. Delete qilingan user login qila olmasin lekin qaytib Register qila olsin.


2-topshiriq (10 ball)

Vacancy Model:
“Vacancy” modelini yarating va “salary” uchun filter yozing. Fields: salary_from, salary_to, salary. Masalan: $5000lik vacancylarni chiqarib bersin.

3-topshiriq (10 ball)

AES Cipher:
“Product” modelini yarating va barcha fieldlarni responseda AES algorithmidan foydalanib shifrlang. Fields: price(decimalfield), marja(decimalfield), package_code(charfield).

4-topshiriq (15 ball)

Modellarni tuzing:
Futbol chempionatiga oid barcha ma’lumotlarni saqlash uchun modellarni tuzing. Masalan: O’yinlar ro’yhati, o’yindagi statistika va boshqa chempionat haqida barcha ma’lumotlar. Ushbu sourcedan foydalaning qancha ko’p ma’lumot saqlasangiz to’liq ball beriladi.

5-topshiriq (5 ball)

LeetCode Problems:
Ikkita masalani yeching:<br>
https://leetcode.com/problems/length-of-last-word/<br>
https://leetcode.com/problems/plus-one/<br>

Clean Code (5 ball)

Arxitektura to’g’ri tuzilgan, katta xatolar qilinmagan va “best practice”lardan foydalanilgan.
