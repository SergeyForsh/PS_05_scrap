# PS_05_scrap
##PS05. Введение в Scrapy. Web Scraping
--
#Устанавливаем нужную библиотеку через терминал:

Заходим в терминал в PyCharm.
Пишем команду
pip install scrapy
Нажимаем на клавишу Enter.
#
Используем команду:

Открываем терминал.
Пишем команду:
scrapy startproject divanpars
Нажимаем на клавишу Enter.
Видим, что создалась папка. В папке есть пакеты (иконка папки с кругляшочком).
Модуль — один пайтоновский файл.

Пакет — набор модулей.
Создаём файл внутри пакета spiders:
Пишем команду:
cd 
Нажимаем правой кнопкой мыши на пакет и выбираем Copy Path/Reference — Absolute Path. Так мы скопируем абсолютный путь к пакету.
Вставляем путь в терминал, после команды cd.
Продолжаем команду: cd [путь] scrapy genspider divannewpars divan.ru
Нажимаем на клавишу Enter.
Заходим в создавшийся файл и видим автоматически создавшийся код:

import scrapy
class DivannewparsSpider(scrapy.Spider):
name = "divannewpars"
allowed_domains = ["divan.ru"]
start_urls = ["https://www.divan.ru/category/svet"]
def parse(self, response):
pass

Поправляем ссылки:
import scrapy
class DivannewparsSpider(scrapy.Spider):
name = "divannewpars"
allowed_domains = [https://www.divan.ru/sankt-peterburg/]
start_urls = ["https://www.divan.ru/sankt-peterburg/category/svet"]
# start_urls - это та ссылка, от которой начинается парсинг
def parse(self, response):
pass - это заглушка потом ее удаляем!!!
Визуально упрощаем работу с терминалом (необязательно): Пишем команду: pip install ipython
Нажимаем на клавишу Enter.

Заходим в файл scrapy.cfg.
Дописываем код: # Это было, это не прописываем
 [settings]
 default = divanpars.settings
# Это новое, это прописываем
shell == ipython
# То есть мы "заменяем" стандартный терминал только что установленным.
##Отправляем в терминале команду:   scrapy shell
Видим список команд, в котором команды отделены значком [s].
--
## Базовые функции и команды в терминале
Мы работаем в терминале, чтобы перед работой в коде найти то, что нам нужно будет делать...
### Чтобы увидеть теги, названия классов и т.д., нажимаем на элемент правой кнопкой мыши и выбираем Просмотреть код.!!!

Команды в терминале:
- Чтобы найти информацию по конкретному элементу, при открытой консоли нажимаем на инструмент в левом верхнем углу (стрелочка в пунктирном прямоугольнике):
fetch(’ссылка’) — используется, чтобы загрузить веб-страницу. После использования покажется статус-код;
response.css(’h2’) — поиск всех элементов с тегом h2;
response.css(’h2.vFBoK’) — поиск элементов по названию класса. Указываем тег, ставим точку, указываем название класса;
response.css(’div.LlPhw’) — поиск по тегу. Будет создан целый список;
response.css(’div.LlPhw’).get() — выбор только первого элемента из списка;
divan = response.css(’div.LlPhw’) — создаём переменную, в которую сохранится список из поиска по тегу;
len(divan) — считаем, сколько диванов было найдено по тегу;
divan1 = divan[0] — выбираем элемент из списка по его индексу (индексы начинаются с 0);
divan1.css(’div’) — получаем все теги div от этого элемента.

Теперь мы поработаем не в терминале, а в коде.
Мы соберём информацию обо всех диванах с сайта. Мы возьмём названия, цены и ссылки.
Заходим на сайт и изучаем, какие у карточек одинаковые блоки.
Открываем файл divannewpars.py.
Удаляем pass.
# start_urls - это та ссылка, от которой начинается парсинг.
---
Для запуска программы можно использовать основной терминал или создать новый.

Текущий терминал переименовываем: кликаем по нему правой кнопкой мыши, выбираем Rename Session, вводим название scrapy shell и нажимаем на клавишу Enter.

Переходим в новый терминал Local(2). Нажимаем правой кнопкой мыши на пакет spiders и выбираем Copy Path/Reference — Absolute Path.

Пишем команду:

cd [путь] scrapy crawl divannewpars

Нажимаем на клавишу Enter.

Выводятся отдельно имя, цена и дополнение к ссылке. Выводится также запрос и его статус (200 — без ошибок).
--
### Дополнительные материалы:

1. Веб-скрапинг

https://tproger.ru/translations/skraping-sajta-s-pomoshhju-python-gajd-dlja-novichkov

https://priceva.ru/blog/article/v-chem-raznitsa-mezhdu-parsingom-i-skrejpingom

2. Scrapy

https://habr.com/ru/companies/otus/articles/812035/

https://habr.com/ru/companies/sberbank/articles/748406/

https://digitology.tech/docs/scrapy/index.html

3. Итераторы и генераторы

https://sky.pro/media/ispolzovanie-klyuchevogo-slova-yield-v-python/

https://proglib.io/p/chto-takoe-yield-v-python-samyy-populyarnyy-vopros-na-stakoverflou-po-pitonu-2022-03-21

https://habr.com/ru/articles/337314/

https://sky.pro/media/raznicza-mezhdu-generatorami-i-iteratorami-v-python/

--
Web scraping (веб-скрапинг) — это процесс автоматического извлечения данных из интернета, обычно из веб-страниц. Этот процесс включает в себя загрузку веб-страницы и извлечение нужной информации из неё, что часто делается с помощью ботов или скриптов. Обычно веб-скрапинг используется для сбора больших объёмов данных, которые затем могут быть использованы в различных аналитических целях для мониторинга цен, сбора контактной информации, исследования рынка и т.д.
--
Знаем основы программирования на Python

✅Умеем работать с базами данных и SQL

✅Умеем работать с виртуальными машинами

✅Знаем основные концепции извлечения данных из веб-страниц

✅Умеем отправлять HTTP-запросы

✅ Умеем извлекать данные из HTML-кода веб-страниц

✅ Умеем обрабатывать динамические элементы страницы
