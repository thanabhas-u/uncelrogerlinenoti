import requests

# Uncle Roger Notification Bot


token = 'YOUR_LINE_NOTI_TOKEN'


def create_headers(token):
    headers = {'Authorization': f'Bearer {token}'}
    return headers


def send_noti(message, mood):
    fuiyoh = 'https://upload.wikimedia.org/wikipedia/commons/4/4f/Nigel_Ng%2C_2020-11-14_A_%28crop%29.jpg'
    haiya = 'https://www.hitc.com/static/uploads/2020/07/Screenshot-2020-07-24-at-10.03.41-AM.png'
    if mood == 'happy':
        url = fuiyoh
    else:
        url = haiya
    payload = {'message': f'{message}', 'imageThumbnail': f"{url}",
               'imageFullsize': f"{url}"}

    return payload


def send_message(headers, payload):
    r = requests.post('https://notify-api.line.me/api/notify', headers=headers, data=payload)
    if r.status_code == 200:
        print("Successful.")
        print(r.text)
    else:
        raise Exception(r.text)


def noti_pipeline(message, mood):
    send_message(create_headers(token), send_noti(message, mood))


