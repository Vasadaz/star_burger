# Сайт доставки еды Star Burger

Это сайт сети ресторанов Star Burger. Здесь можно заказать превосходные бургеры 
с доставкой на дом.

![скриншот сайта](https://dvmn.org/filer/canonical/1594651635/686/)


Сеть Star Burger объединяет несколько ресторанов, действующих под единой франшизой. 
У всех ресторанов одинаковое меню и одинаковые цены. Просто выберите блюдо из меню 
на сайте и укажите место доставки. Мы сами найдём ближайший к вам ресторан, 
всё приготовим и привезём.

На сайте есть три независимых интерфейса. Первый — это публичная часть, где можно 
выбрать блюда из меню, и быстро оформить заказ без регистрации и SMS.

Второй интерфейс предназначен для менеджера. Здесь происходит обработка заказов. 
Менеджер видит поступившие новые заказы и первым делом созванивается с клиентом, 
чтобы подтвердить заказ. После оператор выбирает ближайший ресторан и передаёт 
туда заказ на исполнение. Там всё приготовят и сами доставят еду клиенту.

Третий интерфейс — это админка. Преимущественно им пользуются программисты при 
разработке сайта. Также сюда заходит менеджер, чтобы обновить меню 
ресторанов Star Burger.

[Пример сайта.](https://vasadaz.ru)

## Как запустить dev-версию сайта

Для запуска сайта нужно запустить **одновременно** бэкенд и 
фронтенд, в двух терминалах.

### Как собрать бэкенд

Скачайте код:
```shell
git clone https://github.com/Vasadaz/star_burger.git
```

Перейдите в каталог проекта:
```shell
cd star_burger/backend/
```

[Установите Python](https://www.python.org/), если этого ещё не сделали.

Проверьте, что `python` установлен и корректно настроен. 
Запустите его в командной строке:
```shell
python --version
```
**Важно!** Версия Python должна быть не ниже 3.6.

Возможно, вместо команды `python` здесь и в остальных инструкциях этого README 
придётся использовать `python3`. Зависит это от операционной системы и от того, 
установлен ли у вас Python старой второй версии.

В каталоге проекта создайте виртуальное окружение:
```shell
python -m venv .venv
```
Активируйте его. На разных операционных системах это делается разными командами:

- Windows: `.\.venv\Scripts\activate`
- MacOS/Linux: `source .venv/bin/activate`


Установите зависимости в виртуальное окружение:
```shell
pip install -r requirements.txt
```

Получить токен [геокодера Яндекса](https://developer.tech.yandex.ru/services/3).
Определите переменную окружения `SECRET_KEY` и `YANDEX_GEO_API`. 
Создать файл `.env/django/.env` в каталоге `star_burger/` и положите туда такой код:
```shell
SECRET_KEY=django-insecure-0if40nf4nf93n4
YANDEX_GEO_API=ed562gf-b95a-8563-a7c6-fa6891033e38c8ba0
```

Создайте файл базы данных SQLite и отмигрируйте её следующей командой:

```shell
python manage.py migrate
```

Запустите сервер:

```shell
python manage.py runserver
```

Откройте сайт в браузере по адресу [http://127.0.0.1:8000/](http://127.0.0.1:8000/). 
Если вы увидели пустую белую страницу, то не пугайтесь, выдохните. 
Просто фронтенд пока ещё не собран. Переходите к следующему разделу README.

### Собрать фронтенд


**Откройте новый терминал**. Для работы сайта в dev-режиме необходима одновременная 
работа сразу двух программ `runserver` и `parcel`. Каждая требует себе отдельного 
терминала. Чтобы не выключать `runserver` откройте для фронтенда новый терминал и 
все нижеследующие инструкции выполняйте там.

[Установите Node.js](https://nodejs.org/en/), если у вас его ещё нет.

Проверьте, что Node.js и его пакетный менеджер корректно установлены. Если всё исправно,
то терминал выведет их версии:
###### Все версии устанавливаемых пакетов указанные в примерах являются минимальными для запуска проекта!

```shell
nodejs --version
# v18.17.1
# Если ошибка, попробуйте node:
node --version
# v18.17.1

npm --version
# 10.2.4
```

Версия `nodejs` должна быть не младше 10.0. Версия `npm` не важна. 
Как обновить Node.js читайте в статье: [How to Update Node.js](https://phoenixnap.com/kb/update-node-js-version).

Перейдите в каталог проекта и установите пакеты Node.js:
```shell
cd star_burger/frontend
npm ci --include=dev
```

Команда `npm ci` создаст каталог `node_modules` и установит туда пакеты Node.js. 
Получится аналог виртуального окружения как для Python, но для Node.js.

Помимо прочего будет установлен [Parcel](https://parceljs.org/) — это упаковщик веб-приложений, 
похожий на [Webpack](https://webpack.js.org/). В отличие от Webpack он прост в использовании и совсем 
не требует настроек. Проверяем успешную установку `parcel`:
```shell
cd star_burger
./node_modules/.bin/parcel --version
# 2.4.0
```

Теперь запустите сборку фронтенда и не выключайте. Parcel будет работать в фоне и 
следить за изменениями в JS-коде:
```shell
./node_modules/.bin/parcel watch bundles-src/index.js --dist-dir bundles --public-url="./"
```

Если вы на Windows, то вам нужна та же команда, только с другими слешами в путях:
```shell
.\node_modules\.bin\parcel watch bundles-src/index.js --dist-dir bundles --public-url="./"
```

Дождитесь завершения первичной сборки. Это вполне может занять 10 и более секунд. 
О готовности вы узнаете по сообщению в консоли:

```
✨  Built in 10.89s
```

Parcel будет следить за файлами в каталоге `bundles-src`. Сначала он прочитает 
содержимое `index.js` и узнает какие другие файлы он импортирует. Затем Parcel 
перейдёт в каждый из этих подключенных файлов и узнает что импортируют они. 
И так далее, пока не закончатся файлы. В итоге Parcel получит полный список 
зависимостей. Дальше он соберёт все эти сотни мелких файлов в большие 
бандлы `bundles/index.js` и `bundles/index.css`. Они полностью самодостаточно и 
потому пригодны для запуска в браузере. Именно эти бандлы сервер отправит клиенту.

Теперь если зайти на страницу [http://127.0.0.1:8000/](http://127.0.0.1:8000/), 
то вместо пустой страницы вы увидите:
![](https://dvmn.org/filer/canonical/1594651900/687/)

Каталог `bundles` в репозитории особенный — туда Parcel складывает результаты своей 
работы. Эта директория предназначена исключительно для результатов сборки фронтенда и 
потому исключёна из репозитория с помощью `.gitignore`.

**Сбросьте кэш браузера <kbd>Ctrl-F5</kbd>.** Браузер при любой возможности старается 
кэшировать файлы статики: CSS, картинки и js-код. Порой это приводит к странному 
поведению сайта, когда код уже давно изменился, но браузер этого не замечает и 
продолжает использовать старую закэшированную версию. В норме Parcel решает эту 
проблему самостоятельно. Он следит за пересборкой фронтенда и предупреждает JS-код 
в браузере о необходимости подтянуть свежий код. Но если вдруг что-то у вас идёт не так,
то начните ремонт со сброса браузерного кэша, жмите <kbd>Ctrl-F5</kbd>.


## Как запустить prod-версию сайта

#### 1. Собрать фронтенд.
```shell
# Если при сборке будет ошибка - Error: You must provide the URL of lib/mappings.wasm...
# то раскомментировать экспорт переменной:
# export NODE_OPTIONS=--no-experimental-fetch
./node_modules/.bin/parcel build bundles-src/index.js --dist-dir bundles --public-url="./"
```

#### 2. Настроить бэкенд.

Создать файл `.env/django/.env` в каталоге `star_burger/` со следующими параметрами:

- `ALLOWED_HOSTS` — [см. документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts)
- `DB_URL` - URL для подключения к БД, пример: `postgres://user:paSsw0rd@localhost:5432/star_burger`
- `SECRET_KEY` — секретный ключ проекта. Он отвечает за шифрование на сайте. 
  Например, им зашифрованы все пароли на вашем сайте.
- `YANDEX_GEO_API` - токен [геокодера Яндекса](https://developer.tech.yandex.ru/services/3);

Необязательные настройки `.env/django/.env`:
- `DEBUG` — дебаг-режим, по-умолчанию `False`.
- `ROLLBAR_ACCESS_TOKEN` - токен [Rollbar](https://rollbar.com) для мониторинга ошибок
- `ROLLBAR_ENVIRONMENT` - [Rollbar](https://rollbar.com) ветка мониторинга `production` или `development`.


## Деплой проекта BASH

В файл [`run_deploy.sh`](./run_deploy.sh) прописаны команды для обновления проекта 
на сервере. Перед запуском файл необходимо сделать исполняемым:
```shell
# Даём права
sudo chmod 744 run_deploy.sh

# Запускаем скрипт деплоя
./run_depoy.sh
```

## Деплой проекта DOCKER-COMPOSE

1. Добавить дополнительные параметры в уже существующий файл `.env/django/.env`:
   - `DJANGO_SUPERUSER_EMAIL` — email администратора Django
   - `DJANGO_SUPERUSER_PASSWORD` — пароль администратора Django
   - `DJANGO_SUPERUSER_USERNAME` — логин администратора Django

   А также необходимо добавить или заменить параметр:
    - `DB_URL` - URL для подключения к БД со значением `postgres://user:paSsw0rd@pgdb:5432/star_burger`.
   Если у вас уже было указано похожее значение, то здесь меняется адрес с `localhost`
   на `pgdb`.

2.  В корне проекта создать две директории для будущих томов Docker:
    ```shell
    mkdir db_data # Здесь будут храниться данные БД PostgreSQL
    mkdir fontend/media # Здесь будут храниться медиа данные для Django
    mkdir fontend/static # Здесь будут храниться статические(collectstatic) данные для Django
    ```

3. Установить Docker и Docker-Compose.

4. Находясь в корне проекта выполнить команду по сборке и запуску контейнеров:
   ```shell
    docker-compose up -d
    ```
   
5. После завершения предыдущей команды необходимо проверить состояние контейнеров:
    ```shell
    docker-compose ps
    ```
    Информация об успешном запуске всех контейнеров будет выглядеть примерно так:
    ```shell
    NAME            IMAGE                       COMMAND                  SERVICE         STATUS   PORTS
    django          star_burger-django          "/bin/sh -c 'sleep 2…"   django          Up       0.0.0.0:8080->8080/tcp, :::8080->8080/tcp
    nodejs-parcel   star_burger-nodejs-parcel   "docker-entrypoint.s…"   nodejs-parcel   Up
    postgres        postgres:15.0-alpine        "docker-entrypoint.s…"   pgdb            Up       0.0.0.0:5432->5432/tcp, :::5432->5432/tcp
    ```
    Важно, что у всех контейнеров `STATUS` указан `Up`. 
    Также, здесь видно, что Django работает на порту `8080`.

6. Осталось создать администратора Django c теми данными,
   что были указаны в шаге №1 - выполните следующую команду:
   ```shell
   docker exec -t django sh ./initadmin.sh
   ```

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и 
веб-разработке на сайте [Devman](https://dvmn.org). За основу был взят код проекта [FoodCart](https://github.com/Saibharath79/FoodCart).

Где используется репозиторий:
- Второй и третий урок [учебного курса Django](https://dvmn.org/modules/django/)
