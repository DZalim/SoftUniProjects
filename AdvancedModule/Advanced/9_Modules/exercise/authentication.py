from canvas import root, frame
from helpers import clean_screen, get_password_hash
from tkinter import Button, Entry
import os
from json import dump, loads
from buying_page import display_products

file_name_users = 'users_information.txt'
file_path = os.path.join('db', file_name_users)


def get_users_data():
    info_data = []

    with open(file_path, 'r') as users_file:
        for line in users_file:
            info_data.append(loads(line))

    return info_data


def render_entry():
    register_button = Button(
        root,
        text='Register',
        bg='green',
        fg='white',
        bd=0,
        width=10,
        height=2,
        command=register
    )

    login_button = Button(
        root,
        text='Login',
        bg='blue',
        fg='white',
        bd=0,
        width=10,
        height=2,
        command=login
    )

    frame.create_window(350, 260, window=register_button)
    frame.create_window(350, 310, window=login_button)


def register():
    clean_screen()

    frame.create_text(100, 50, text='First Name:')
    frame.create_text(100, 100, text='Last Name:')
    frame.create_text(100, 150, text='Username:')
    frame.create_text(100, 200, text='Password:')

    frame.create_window(200, 50, window=first_name_box)
    frame.create_window(200, 100, window=last_name_box)
    frame.create_window(200, 150, window=username_box)
    frame.create_window(200, 200, window=password_box)

    register_button = Button(
        root,
        text='Register',
        bg='green',
        fg='white',
        bd=0,
        width=10,
        height=1,
        command=registration
    )

    frame.create_window(225, 240, window=register_button)


def registration():
    info_dict = {
        'First name': first_name_box.get(),
        'Last name': last_name_box.get(),
        'Username': username_box.get(),
        'Password': password_box.get()
    }


    if check_registration(info_dict):
        with open(file_path, 'a') as users_file:
            info_dict['Password'] = get_password_hash(info_dict['Password'])
            dump(info_dict, users_file)
            users_file.write('\n')
            display_products()



def check_registration(info_dict):
    frame.delete('error')

    for key, value in info_dict.items():
        if not value.strip():
            frame.create_text(
                190,
                280,
                text=f'{key} cannot be empty!',
                fill='red',
                tags='error',
            )

            return False

    users_data = get_users_data()

    for user in users_data:
        if user['Username'] == info_dict['Username']:
            frame.create_text(
                190,
                280,
                text='Username is already taken!',
                fill='red',
                tags='error',
            )

            return False

    return True

def login():
    clean_screen()

    frame.create_text(100, 50, text='Username:')
    frame.create_text(100, 100, text='Password:')

    frame.create_window(200, 50, window=username_box)
    frame.create_window(200, 100, window=password_box)

    frame.create_window(220, 150, window=login_button)

def logging():
    if check_login():
        display_products()
    else:
        frame.create_text(180,
                          180,
                          text='Invalid username or password!',
                          fill='red',
                          tags='error',
                          )


def check_login():
    users_data = get_users_data()

    user_username = username_box.get()
    user_password = get_password_hash(password_box.get())

    for user in users_data:
        current_user_username = user['Username']
        current_user_password = user['Password']
        if current_user_username == user_username and current_user_password == user_password:
            return True

    return False


def change_login_button_status(event):
    info = [
        username_box.get(),
        password_box.get(),
    ]

    for el in info:
        if not el.strip():
            login_button['state'] = 'disabled'
            break
    else:
        login_button['state'] = 'normal'


first_name_box = Entry(root, bd=0)
last_name_box = Entry(root, bd=0)
username_box = Entry(root, bd=0)
password_box = Entry(root, bd=0, show='*')


login_button = Button(
    root,
    text='Login',
    bg='blue',
    fg='white',
    width=10,
    height=1,
    bd=0,
    command=logging,
)

login_button['state'] = 'disabled'

root.bind('<KeyRelease>', change_login_button_status)
