def send_email (massage, recipient, sender = 'university.help@gmail.com'):
    ending = ('.com', '.ru', '.net')
    if ((recipient.find('@') and sender.find('@')  != -1) and (recipient.endswith(ending) and sender.endswith(ending))) != True :
        answer = f'Не возможно отправить c адреса {sender} на адрес {recipient}'
    elif sender == recipient:
        answer = f'Нельзя отправисть письмо самому себе!'
    elif sender == 'university.help@gmail.com':
        answer = f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}'
    else:
        answer = f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса{sender} на адрес {recipient}'
    return answer

qwe = send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
print(qwe)
qwe = send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
print(qwe)
qwe = send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
print(qwe)
qwe = send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
print(qwe)


