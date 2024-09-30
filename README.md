# Задание
Разработать эмулятор для языка оболочки ОС. Необходимо сделать работу
эмулятора как можно более похожей на сеанс shell в UNIX-подобной ОС.
Эмулятор должен запускаться из реальной командной строки, а файл с
виртуальной файловой системой не нужно распаковывать у пользователя.
Эмулятор принимает образ виртуальной файловой системы в виде файла формата
zip. Эмулятор должен работать в режиме CLI.

Ключами командной строки задаются:
* Имя пользователя для показа в приглашении к вводу.
* Путь к архиву виртуальной файловой системы.
* Путь к лог-файлу.
* Путь к стартовому скрипту.

Лог-файл имеет формат json и содержит все действия во время последнего
сеанса работы с эмулятором. Для каждого действия указан пользователь.
Стартовый скрипт служит для начального выполнения заданного списка
команд из файла.

Необходимо поддержать в эмуляторе команды ls, cd и exit, а также
следующие команды:
1. mv.
2. whoami.
3. pwd.

Все функции эмулятора должны быть покрыты тестами, а для каждой из
поддерживаемых команд необходимо написать 2 теста.

# Запуск
Запуск эмулятора происходит из командной строки путём ввода:
```
python [path]/main.py [username] [[path]/filesystem.zip] [[path]/logfile.json] [[path]/startscript.txt]
```
Где
* path - путь до файла
* username - имя пользователя
* filesystem.zip - zip-архив, предназначенный для хранения файлов для эмуляции
* logfile.json - файл в формате json, содержащий сведения о пользователе, осуществившим команду, самой команде, успешности выполнения команды и дате выполнения
* startscript.txt - стартовый скрипт - тестовый файл, содержащий команды, которые выполнятся при запуске файла

  После ввода команд пользователю выведется сообщение об ошибке или предложится запустить выполнение команд из стартового скрипта
