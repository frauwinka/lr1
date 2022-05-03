# Лабораторная работа №1
## Постановка задачи:
1) Создать новый проект в PyCharm
2) Сервер на FLASK
3) Написать роут /, который редиректнет на роут /users
4) роут /users Выведет всех юзеров из словаря users
- в виде clickable ссылок
- <url>/users/<username или id>
5) Роут /users/<username или id> проверит
   пользователя в словаре users, и если нет, то вернет 404
###### Пример словаря:
  ```
 a = [{'name': 'Alex', 'id': 1, 'surname': 'Turner', 'age': 36}
       {'name': 'Thom', 'id': 2, 'surname': 'Yorke', 'age': 53}]
  ```
## Результат работы написанной программы:
  При открытии http://127.0.0.1:5000/ происходит переход на http://127.0.0.1:5000/users и отображается список всех пользователей:  
  ![](/images/Screenshot_2.png)  
При клике на любого из них отобразится страница с информацией из словаря о пользователе:  
  ![](/images/Screenshot_1.png)  
Если вручную вбить несуществующий id в строку запроса отобразится ошибка 404:  
  ![](/images/Screenshot_3.png)  
