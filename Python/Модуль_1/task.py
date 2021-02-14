'''
Створити клас BlablacarBooking, який містить такі поля
 1. DriverName (Тільки літери)
 2. NoOfPeople (1-4)
 3. StartTime (Клас Time, що містить 2 поля: hour (00 - 23), minute (00 - 59)).
 4. EndTime (Клас Time, що містить 2 поля: hour (00 - 23), minute (00 - 59)). Min: StartTime.
 5. StartPlace (Тільки літери)
 6. EndPlace (Тільки літери)
Створити такі методи:
 1. Зчитати масив (клас для роботи з масивом екземплярів класу BlablacarBooking) BlablacarBooking з файла (1)
 2. Додати новий BlablacarBooking. На одну і ту саму годину і з одним і тим самим водієм може бути заброньовано
 одночасно не більше 4 місць. Наприклад, #1: John Doe, 2, 10:00 - 11:00, …, #2:John Doe, 3, 10:00 - 11:00,
 … забронювати неможливо, оскільки на 10:00 забронювати можна лише 4 людини.
 Ну і звісно, що один і той самий водій не може везти машину в двох місцях одночасно (вважається, що ім’я унікальне).
 Наприклад, #1: John Doe, 2, 10:00 - 11:00 зі Львова в Київ та #2: John Doe, 2, 10:30 - 17:00 з Харкова в Київ (3)
 3. Додати валідацію на поля DriverName, NoOfPeople, StartTime, EndTime, StartPlace, EndPlace. (2)
 4. Визначити годину, на яку є найбільше замовлень. Якщо таких декілька - вивести всі години. (2)
 5. Водія з найбільшою кількістю поїздок записати в інший файл: John Doe, 5 (1.5)
 6. Вивести всі BlablacarBooking на екран (0.5)
'''

from Colection import Composition

mas = Composition()
file_name = "Information"
mas.read_txt(file_name)
for i in mas:
    print(i)
mas.add_element()
for i in mas:
    print(i)
mas.search_driver()
mas.search_hour()
