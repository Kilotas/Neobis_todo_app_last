Клонируйте репозиторий:

git clone https://github.com/Kilotas/Neobis_todo_app_last.git
cd todo
Создайте и активируйте виртуальное окружение:

python -m venv venv
source venv/bin/activate  # для Unix/MacOS
venv\Scripts\activate  # для Windows
Установите зависимости:

pip install -r requirements.txt
Примените миграции:

python manage.py migrate
Запустите сервер:

python manage.py runserver
Использование
После успешного запуска сервера, вы сможете взаимодействовать с веб-приложением. Откройте браузер и перейдите по адресу http://localhost:8000/.
