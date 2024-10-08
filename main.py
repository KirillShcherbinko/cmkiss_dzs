from functions import username_correctness
from functions import file_path_correctness
from terminal import Terminal
from sys import argv


def main():
    if len(argv) == 5:
        if (username_correctness(argv[1]) and
                file_path_correctness(argv[2], ".zip") and
                file_path_correctness(argv[3], ".json") and
                file_path_correctness(argv[4], ".txt")):
            username = argv[1]
            vfs_path = argv[2]
            logfile_path = argv[3]
            start_script_path = argv[4]
            terminal = Terminal(username, vfs_path, logfile_path, start_script_path)
            start_script_launch = input("Нажмите y, чтобы начать исполнение стартового скрипта ")
            if start_script_launch == "y":
                terminal.start_script_exec()
            terminal.start_work_process()
    elif len(argv) < 5:
        print("Введено недостаточное количество аргументов")
    else:
        print("Введено слишком много аргументов")


if __name__ == '__main__':
    main()
