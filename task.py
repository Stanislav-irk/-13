price = 0
while True:
    try:
        ticket = input('Сколько билетов вы хотите приобрести на мероприятие? ')
        ticket = int(ticket)
        if type(ticket) == int:
            break
    except ValueError:
        print('Введите целое число')
for i in range(ticket):
    i += 1
    while True:
        try:
            visitor_for_age = input(f'Возраст посетителя? {i} ')
            visitor_for_age = int(visitor_for_age)
            if visitor_for_age < 18:
                print('Билет бесплатный')
            elif 25 > visitor_for_age >+ 18:
                 price += 990
                 print('Стоимость билета: 990 рублей ')
            else:
                 price += 1390
                 print('Стоимость билета: 1390 рублей ')
            if type(visitor_for_age) == int:
                break
        except ValueError:
            print('Введите целое число')
if ticket > 3:
    print(f'Сумма к оплате {price} рублей. ')
    price = price - ((price / 100) * 10)
    print(f'Сумма к оплате {price} рублей с учетом скидки 10%, за полную стоимость заказа от 3-х человек')





