import os
import time

TARGET_IP = "192.168.8.102"
LOG_FILE = "father_presence.log"

print(f"\033[94m[INFO] Радар запущен. Цель: {TARGET_IP}\033[0m")
print(f"\033[94m[INFO] Логи сохраняются в {LOG_FILE}\033[0m")

last_state = None

try:
    while True:
        # Проверка связи
        status = os.system(f"ping -c 1 -W 1 {TARGET_IP} > /dev/null 2>&1")
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        
        if status == 0:
            state = "В СЕТИ"
            color = "\033[92m" # Зеленый
        else:
            state = "ОФФЛАЙН"
            color = "\033[91m" # Красный

        # Вывод в терминал
        print(f"[{current_time}] {color}{state}\033[0m")

        # Если статус изменился, записываем в файл
        if state != last_state:
            with open(LOG_FILE, "a") as f:
                f.write(f"{current_time} - Объект {state}\n")
            last_state = state
        
        time.sleep(5)
except KeyboardInterrupt:
    print("\n\033[93m[STOP] Наблюдение прекращено.\033[0m")
