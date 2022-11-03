import pyperclip
import keyboard
import os

if not os.path.exists("text.txt"):
    with open("text.txt", mode="w", encoding="utf-8") as file:
        file.write("Пример вставки")
key = input("Введите англ клавишу для вставки:")
os.system('cls' if os.name=='nt' else 'clear')

with open("text.txt", mode="r", encoding="utf-8") as file:
    strings = file.readlines()
    text = "\n".join(strings)
    print(f"\"{text}\" сейчас на бинде\nКлавиша {key} для вставки\nДля изменения поменяйте текст в text.txt в папке проги")

while True:
    if keyboard.is_pressed(key):
        with open("text.txt", mode="r", encoding="utf-8") as file:
            strings = file.readlines()
            text = "\n".join(strings)
            pyperclip.copy(text)
            pyperclip.paste()
        