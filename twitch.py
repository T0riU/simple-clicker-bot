import pyautogui
import time
import keyboard
from PIL import ImageGrab

def get_hex_color(x, y):
    # Захват экрана всех мониторов
    screen = ImageGrab.grab(all_screens=True)
    # Получение цвета пикселя в указанных координатах
    r, g, b = screen.getpixel((x, y))
    # Конвертация цвета в формат HEX
    return f'#{r:02x}{g:02x}{b:02x}'


message = "!"+"hitsquad"
click_x, click_y = 3244, 745  # Укажите координаты для клика
timeQ = 180

def perform_action():
    # Переместить мышь к указанным координатам и кликнуть
    pyautogui.moveTo(click_x, click_y)
    pyautogui.click()
    
    # Вставить сообщение
    pyautogui.typewrite(message)
    
    # Нажать Enter
    pyautogui.press('enter')

print("Программа начата. Нажмите 'q' для выхода.")

last_action_time = time.time()
change_print = False

try:
    while True:
        # Проверка, если 'q' была нажата
        if keyboard.is_pressed('q'):
            print("Программа остановлена пользователем.")
            break
        if keyboard.is_pressed('u'):
            change_print = not(change_print)
            
        if change_print:  
            x, y = pyautogui.position()
            hex_color = get_hex_color(x, y)
            print(f"Текущие координаты мыши: X={x}, Y={y} | Цвет пикселя: {hex_color}")
        
        if time.time() - last_action_time >= timeQ:
            perform_action()
            last_action_time = time.time()
        
        # Пауза на 1 секунду перед следующей итерацией
        time.sleep(1)
except KeyboardInterrupt:
    print("Программа остановлена пользователем.")