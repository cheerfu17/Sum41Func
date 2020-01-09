def sum41(user_id, message, random_id):
    without_point = message.replace('.','')
    i = 0
    b = ''
    a = ''
    simbol = ''
    result = 0
    while i < len(without_point):
        if without_point[i].isdigit():
            a += without_point[i]
        else:
            simbol = without_point[i]
            i += 1
            break
        i += 1

    while i < len(without_point):
        b += without_point[i]
        i+=1

    if simbol == '^':
        message = message.replace('^', '**')

    if a != '' and b.isdigit():
        try:
            result = round(eval(message), 5)
        except:
            vk.messages.send(user_id=user_id, message='ERROR!!! DIVIDION BY ZERO', random_id=random_id)
        result = 'Ответ: ' + str(result)
        time.sleep(1)
        vk.messages.send(user_id=user_id, message=result, random_id=random_id)