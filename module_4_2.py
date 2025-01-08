import re


def send_mail(message, recipient, sender='Kazakovmvmvm@gmail.com'):
    def is_valid_email(email):
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[com, ru, net]+$'
        return re.match(email_regex, email)

    if not is_valid_email(sender):
        print('Ошибка: Некорректный email адрес отправителя')
        return

    if not is_valid_email(recipient):
        print('Ошибка: Некорректный email адрес получателя')
        return

    if sender == recipient:
        print('Ошибка: вы пытаетесь отправить сообщение себе')
        return

    if sender == 'Kazakovmvmvm@gmail.com':
        print(f'Внимание: Этот: {sender} адрес используется по умолчанию')

    if sender != 'Kazakovmvmvm@gmail.com':
        print(f'Внимание: Этот: {sender} НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ ')


    print(f'Письмо отправляет: {sender}, Получатель: {recipient}: {message}')

send_mail('День добрый', 'poluchatrl@mail.net', 'otpravitrl@mail.ru')