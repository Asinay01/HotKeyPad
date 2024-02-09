import serial
import time
import os
import sys
import traceback
import serial.tools.list_ports
import serial.serialutil
import json
import keyboard as kb
import inspect

parser = {
    'a': '1',
    'b': '2',
    'c': '3',
    'd': '4',
    'e': '5',
    'f': '6',
    'g': '7',
    'h': '8',
    'i': '9',
    'j': '10',
    'k': '11',
    'l': '12',
    'm': '13',
    'n': '14',
    'o': '15',
    'p': '16'
}


def get_script_dir(follow_symlinks=True):
    if getattr(sys, 'frozen', False):
        path = os.path.abspath(sys.executable)
    else:
        path = inspect.getabsfile(get_script_dir)
    if follow_symlinks:
        path = os.path.realpath(path)
    return os.path.dirname(path)


def load_config():
    script_dir = get_script_dir()
    if not os.path.isfile(f"{script_dir}/config.json"):
        print("config.json не найден. Поместите его в папку с программой")
        input('Press Enter to exit')
        sys.exit()
    else:
        with open(f"{script_dir}/config.json") as file:
            return json.load(file)


def find_port():
    print('Поиск устройства')
    try:
        ports = list(serial.tools.list_ports.comports())
        if len(ports) != 0:
            for port in ports:
                if "CH340" in str(port.description):
                    print('Попытка подключения через порт '
                          f'{port.description}')
                    return str(port.description).strip(')').split('(')[-1]
        print('Устройство не найдено')
        input('Нажмите Enter для повторной попытки\n')
        return None
    except Exception:
        return None


def run_hotkey(*args):
    for arg in args:
        kb.press(arg)
        time.sleep(0.07)
    for arg in args:
        kb.release(arg)
        time.sleep(0.07)


def main():
    try:
        config = load_config()
        while True:
            port = find_port()
            if port:
                break
        ser = serial.Serial(port, 9600)
        time.sleep(2)
        ser.reset_input_buffer()
        print('Соединение установлено. Можно тыкать\n')
        while True:
            try:
                response = ser.readline()
                parsed = parser[response.decode('utf-8')[0]]
                if parsed in config:
                    print(f'Кнопка {parsed}')
                    if type(config[parsed]) is list:
                        if len(config[parsed]) == 2:
                            print(config[parsed])
                            keydata = config[parsed][0]
                            if config[parsed][1] == 'hotkey':
                                run_hotkey(*keydata)
                            elif config[parsed][1] == 'text':
                                kb.write(keydata)
                            else:
                                print('Неизвестный тип бинда. '
                                      'Проверьте конфиг')
                        else:
                            print(f'Проверь кнопку {parsed}, там что-то '
                                  'лишнее, или чего-то не хватает')
                    else:
                        print('Ошибка в конфиге')
                else:
                    print(f'Кнопки {parsed} нет в конфиге')
            except serial.serialutil.SerialException:
                print('\nСоединение с устройством прервано')
                input('Нажмите Enter для попытки переподключения\n')
                break
        ser.close()
    except Exception:
        print('Ошибка:\n', traceback.format_exc())
        print('Критическая ошибка\n')
        input('Press Enter to exit')
        sys.exit()


print('Asinay software turboproductions ©\n')
while True:
    main()
