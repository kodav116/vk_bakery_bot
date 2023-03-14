import os

import vk_api

from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor


vk_session = vk_api.VkApi(token=os.getenv("ACCESS_TOKEN"))


def send_message(user_id, message, keyboard=None, attachment = ""):
    """
    Функция получает ID юзера и отправляет ему приветствие, а затем кнопки меню.

    """
    post = {
        "user_id": user_id,
        "message": message,
        "random_id": 0,
        "attachment": attachment
    }
    if keyboard is not None:
        post["keyboard"] = keyboard.get_keyboard()
    else:
        post = post

    vk_session.method("messages.send", post)


if __name__ == '__main__':
    while True:
        for event in VkLongPoll(vk_session).listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                user_text = event.text.lower()
                user_id = event.user_id
                if user_text == "Привет".lower():
                    keyboard = VkKeyboard(inline=True)
                    keyboard.add_button("Меню", VkKeyboardColor.PRIMARY)
                    send_message(user_id, "Привет! Вот меню нашей пекарни!", keyboard)

                elif user_text == "Меню".lower() or user_text == "Назад".lower():
                    keyboard = VkKeyboard(inline=True)
                    buttons = ["Выпечка", "Десерты", "Пироги"]
                    button_colors = [VkKeyboardColor.PRIMARY, VkKeyboardColor.SECONDARY, VkKeyboardColor.NEGATIVE]
                    for btn, btn_color in zip(buttons, button_colors):
                        keyboard.add_button(btn, btn_color)
                    send_message(user_id, "Выберите раздел меню", keyboard)

                elif user_text == "Выпечка".lower() or user_text == "В раздел выпечки".lower():
                    keyboard = VkKeyboard(inline=True)
                    buttons = ["Белый хлеб", "Булка с маком", "Хлеб-Бородино", "Назад"]
                    button_colors = [VkKeyboardColor.PRIMARY, VkKeyboardColor.PRIMARY, VkKeyboardColor.PRIMARY,
                                     VkKeyboardColor.NEGATIVE]
                    for btn, btn_color in zip(buttons, button_colors):
                        keyboard.add_button(btn, btn_color)
                    send_message(user_id, "Выберите выпечку", keyboard)

                elif user_text == "Белый хлеб".lower():
                    send_message(user_id, 'БЕЛЫЙ ХЛЕБ\nЦена: 20 рублей\nВсегда свежий, всегда в наличии!',
                                          keyboard=None, attachment="photo-219295104_457239017")

                elif user_text == "Булка с маком".lower():
                    send_message(user_id, "БУЛОЧКА С МАКОМ\nЦена: 50 рублей\nВкусная, как в детстве.",
                                         keyboard=None, attachment="photo-219295104_457239020")

                elif user_text == "Хлеб-Бородино".lower():
                    send_message(user_id, "БОРОДИНСКИЙ ХЛЕБ\nЦена: 20 рублей\nОчень вкусный, по народному рецепту.",
                                 keyboard=None, attachment="photo-219295104_457239021")

                elif user_text == "Десерты".lower() or user_text == "В раздел десертов".lower():
                    keyboard = VkKeyboard(inline=True)
                    buttons = ["Торт Наполеон", "Пирожное Прага", "Желе-вишня", "Назад"]
                    button_colors = [VkKeyboardColor.PRIMARY, VkKeyboardColor.PRIMARY, VkKeyboardColor.PRIMARY,
                                     VkKeyboardColor.NEGATIVE]
                    for btn, btn_color in zip(buttons, button_colors):
                        keyboard.add_button(btn, btn_color)
                    send_message(user_id, "Выберите десерт", keyboard)

                elif user_text == "Торт Наполеон".lower():
                    send_message(user_id, "ТОРТ НАПОЛЕОН\nЦена: 500 рублей\nГде он? На поле он!",
                                 keyboard=None, attachment="photo-219295104_457239022")

                elif user_text == "Пирожное Прага".lower():
                    send_message(user_id, "ПИРОЖНОЕ ПРАГА\nЦена: 465 рублей\nВкус Праги у вас дома!",
                                 keyboard=None, attachment="photo-219295104_457239023")

                elif user_text == "Желе-вишня".lower():
                    send_message(user_id, "ЖЕЛЕ-ВИШНЯ\nЦена: 350 рублей\nЧеревишня, но с желе!",
                                 keyboard=None, attachment="photo-219295104_457239024")

                elif user_text == "Пироги".lower():
                    keyboard = VkKeyboard(inline=True)
                    buttons = ["Пирог с мясом", "Пирог с рыбой", "Назад"]
                    button_colors = [VkKeyboardColor.PRIMARY, VkKeyboardColor.PRIMARY, VkKeyboardColor.NEGATIVE]
                    for btn, btn_color in zip(buttons, button_colors):
                        keyboard.add_button(btn, btn_color)
                    send_message(user_id, "Выберите пирог", keyboard)

                elif user_text == "Пирог с мясом".lower():
                    send_message(user_id, "ПИРОГ С МЯСОМ\nЦена: 200 рублей\nСытный обед для всей семьи!",
                                 keyboard=None, attachment="photo-219295104_457239025")

                elif user_text == "Пирог с рыбой".lower():
                    send_message(user_id, "ПИРОГ С РЫБОЙ\nЦена: 300 рублей\nЛучшее завершение дня.",
                                 keyboard=None, attachment="photo-219295104_457239026")

                else:
                    send_message(user_id, f"Ещё раз. Не могу разобрать: {user_text}. Попробуйте ввести 'Привет'.")
