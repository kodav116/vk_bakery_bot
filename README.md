# vk_bakery_bot
Простой бот на vk-api и python, отправляет сообщения вашего сообщества с товарами/новостями/чем-угодно через меню. У меня отправляет выпечку.

## Установка

При помощи [pip](https://pip.pypa.io/en/stable/) устанавливаем vk и vk-api.

```bash
pip install vk
pip install vk-api
```
В вашем сообществе в ВК заходите в Управление -> Работа с API. Следуем инструкции, включаем Longpoll и получаем наш уникальный Access Token.
## Использование
Добавляете свой Access Token в env и бот в реальном времени будет реагировать на сообщения пользователей. Бот отвечает на 'Привет' и открывает меню:
![bak_1](https://user-images.githubusercontent.com/101284782/225134747-5c2612bf-bc9b-4f44-b98f-e6a6ab028c10.png)
В меню есть 3 раздела: Выпечка, Десерты, Пироги. В кадом разделе есть несколько товаров. При выборе товара бот отправляет название, описание и фото. Меню работает
через inline: кнопки будут в самом диалоге и ниже поля для ввода сообщения, если открыть этот раздел
![bak_2](https://user-images.githubusercontent.com/101284782/225135529-b8467ae4-d3f2-47be-b4fc-68a12954c9f4.png)
![bak_3](https://user-images.githubusercontent.com/101284782/225135557-fabd9287-20f4-446d-9be7-818584af9af3.png)
Из раздела в меню можно выйти нажав кнопку Назад или введя Назад в сообщения.
![bak_4](https://user-images.githubusercontent.com/101284782/225135912-2660b49f-8d98-4b69-904f-97434d36cea6.png)
При написании использованы только vk, vk-api и python.
![bak_5](https://user-images.githubusercontent.com/101284782/225136141-19cf7f5c-d8c0-49fc-a500-9c5a0e6c4a3b.png)

