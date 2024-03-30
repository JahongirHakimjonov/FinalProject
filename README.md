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