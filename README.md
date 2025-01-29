# AI Network Security Gateway

Этот проект — **интеллектуальный шлюз безопасности**, который анализирует сетевой трафик с помощью ИИ и предотвращает атаки в режиме реального времени.

## Возможности:
Мониторинг сетевого трафика  
Обнаружение аномалий (DDoS, сканирование, брутфорс и т. д.)  
Автоматическое блокирование IP-адресов злоумышленников  
Веб-интерфейс для мониторинга  

## Установка и запуск
### 1. Установите зависимости:
    pip install -r requirements.txt

## Структура проекта

    ai_network_security/
    │── core/                 # Основная логика работы шлюза
    │   ├── packet_sniffer.py # Захват трафика
    │   ├── preprocess.py     # Предобработка данных
    │   ├── anomaly_detection.py # Анализ ИИ
    │   ├── mitigation.py     # Устранение угроз
    |   ├── firewall.py       # Управление iptables 
    │── web/                  # Веб-интерфейс
    │   ├── routes.py         # API эндпоинты
    │   ├── templates/        # HTML-страницы
    │   ├── static/           # CSS, JS
    │── config.py             # Конфигурация
    │── start.py              # Точка входа
    │── requirements.txt      # Зависимости
    │── README.md             # Документация



## Как работает?
 
    1.Захват трафика: packet_sniffer.py собирает пакеты с сетевого интерфейса.
    2.Анализ: anomaly_detection.py использует обученную модель ИИ для выявления атак.
    3.Защита: mitigation.py блокирует IP-адреса злоумышленников через iptables.



## Настройки
### Измените config.py, если нужно настроить:
    Мониторинг сетевого интерфейса (eth0)
    Количество анализируемых пакетов
    Порт веб-интерфейса (8000)



## Запустите сервис:
    python start.py



## API эндпоинты:
    GET -	/monitor -	Запуск анализа сети и блокировка угроз
    GET -	/status -	Проверка состояния системы
    GET	- /blocklist -	Список заблокированных IP



## Разработчик
👨‍💻 Автор: lightnnx
✉️ Контакты: bigbobodikc@bk.ru

