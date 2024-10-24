import zipfile
import os
from colorama import init, Fore
import time

init()

#задержка перед запуском
time.sleep(1)

#пайчекер реди еу
print(f"{Fore.GREEN}PyChecker ready!!!!{Fore.RESET}")

# Запрос пути к директории для извлечения файлов
def get_true_directory():
    while True:
        extract_dir = input(f"{Fore.GREEN}Enter the path to the directory where you want to extract files (for example, C:/Users/YourUsername/Downloads/extracted_program/):{Fore.RESET} ")
        if os.path.isdir(extract_dir):
            print(f"{Fore.GREEN}Yup! That's the correct way!: {extract_dir}{Fore.RESET}")
            return extract_dir
        else: 
            print(f"{Fore.RED}Incorrect path, please, try again.{Fore.RESET}")

#Получение корректного пути для извлечения файлов
extract_dir = get_true_directory()

# Запрос пути к исполняемому файлу
def get_exe_file_path():
    while True: 
        exe_file_path = input(f"{Fore.GREEN}Enter the path to the executable file that needs to be checked (for example, C:/Users/YourUsername/Downloads/program.exe):{Fore.RESET} ")
        if os.path.isfile(exe_file_path):  # Проверяем, что это файл
            print(f"{Fore.GREEN}Yup! That's the correct way!: {exe_file_path}{Fore.RESET}")
            return exe_file_path
        else:
            print(f"{Fore.RED}Incorrect path, please, try again.{Fore.RESET}")

#Получение корректного пути к исполняемому файлу
exe_file_path = get_exe_file_path()

#Проверка, является ли файл zip-архивом
try:
    if zipfile.is_zipfile(exe_file_path):
        with zipfile.ZipFile(exe_file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)
        print(f"{Fore.GREEN}Files have been successfully extracted to {extract_dir}{Fore.RESET}")  
    else:
        print(f"{Fore.RED}The file is not a zip archive or was not created using PyInstaller.{Fore.RESET}")  
except Exception as e:
    print(f"{Fore.RED}fail: {e}{Fore.RESET}")

#Ожидание ввода перед закрытием программы
input(f"{Fore.YELLOW}Press Enter to leave...{Fore.RESET}")  
