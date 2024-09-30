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

# Примеры использования

В данном разделе приводятся примеры использования эмулируемых команд. Также рассмотрены примеры записи данных о работе эмулятора в файл формата json и выполнения команд из стратового скрипта 

## Пример записи в файл формата json

![image](https://github.com/user-attachments/assets/f7e694c5-26c1-4fff-9a14-468aa80282b3)

## Пример выполнения стартового скрипта 

![image](https://github.com/user-attachments/assets/9536610b-61d6-4bd8-8b7d-e9489a5f193b)

## Функция ls

Выводит содержимое директории (directory)

```
ls [directory]
```

![image](https://github.com/user-attachments/assets/313a69ec-44da-448a-acc9-a745698051e9)

## Функция cd

Осуществляет переход в новую директорию (new directory)

```
cd [new directory]
```

![image](https://github.com/user-attachments/assets/672b9e2e-1e6d-4786-9535-4482f49cf981)

## Функция exit

Осуществляет выход из программы

```
exit
```

![image](https://github.com/user-attachments/assets/cf8e9e41-29da-4379-ac2f-c9cc655f0ef3)

## Функция pwd

Выводит название текущей директории

```
pwd
```

![image](https://github.com/user-attachments/assets/1cdf24aa-b6b5-41cc-a82b-04b9dc1007fa)

## Функция whoami

Выводит имя пользователя

```
whoami
```

![image](https://github.com/user-attachments/assets/28f45ad2-b014-4949-8f6a-67b538d679a8)

## Функция mv

Осуществляет перемещение файла из данной директории (old file path) в другую (new file path) с возможностью переименования этого файла

```
mv [old file path] [new file path]
```

![Uploading image.png…]()


# Тестирование
В ходе тестирования удалось добиться покрытия 83%

![image](https://github.com/user-attachments/assets/279cdaec-b536-4db5-bb7a-32e52783cdef)

