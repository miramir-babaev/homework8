from data_create import*
import os

def input_data():
    name = input_name()
    surname = input_surname()
    patronymic =  input_patronymic()
    phone = input_phone()
    address = input_address()
    with open("phone_book.txt", "a",encoding="utf-8") as data:
        data.write(f"{name} {surname} {patronymic}\n{phone}\n{address}\n\n")

def input_data_to_replace () :
    name = input_name ()
    surname = input_surname ()
    patronymic = input_patronymic ()
    phone = input_phone ()
    address = input_address ()
    replace = (f" {name} {surname} {patronymic}\n{phone}\n{address }\n") 
    return replace

def print_data():
    os.system("cls")
    with open("phone_book.txt", "r",encoding="utf-8") as data:
        print(data.read())

def search_line():
    search = input("Введите значение поиска: ")
    with open("phone_book.txt", "r",encoding="utf-8") as data:
        text = data.read().split("\n\n")[:-1]
        
        # data.seek(0)
        # list_data = data.readlines()
        for line in text:
            # print(line)
            # print()
            # time.sleep(1)
            if search in line:
                print(line)
                print()
def delite_line():
    delite = str(input("Введите любой атрибут удаляемого объекта => "))
    with open("phone book.txt"
        "p+", encoding="utf-8") as data:
        text = data.read()
        text_lines = text.strip().split("\n\n")
        for i, line in enumerate (text_lines) :
            if delite in line:
                del_phone_book_lines = text_lines[i]
                text_lines.__delattr__(i)
                print (f'Удалена запись: {del_phone_book_lines}\n')
    with open ("phone_book. txt",'w', newline='',encoding="utf-g") as data:
        data.write('\n\n'.join(text_lines))

def replace_line():
    rep_lace = str (input ("Введите любой атрибут изменяегого объекта => "))
    with open ("phone_book.txt","r+", encoding="utf-g") as data:
        text = data.read ()
        text_lines = text.strip().split("\n\n")
        for i, line in enumerate (text_lines):
            if rep_lace in line:
                rep_phone_book_lines = line
                print (f'Вы хотите изменить: {rep_phone_book_lines}')
                text_lines[i] = input_data_to_replace()
    with open("phone_book. txt" ,'w' ,newline='' ,encoding="utf-8") as data:
        data.write("\n\n". join(text_lines))

def search_line():
    print("Выберите вариант действия: \n"\
            "1.Поиск по имени\n"\
            "2.Поиск по фамилии\n"\
            "3.Поиск по отчеству\n"\
            "4.Поиск по номеру\n"\
            "5.Поиск по адресу"  )
    cmd = input("Введите номер операции: ")
    while cmd not in ("1", "2", "3", "4", "5"):
        print("Ввод неверный")
        cmd = input("Введите номер операции: ")
    search = input("Введите значение поиска: ").title()
    with open("phone_book.txt", "r",encoding="utf-8") as data:
        text = data.read().strip().split("\n\n")
        for line in text:
            new_line = line.replace(" ","\n").strip().split("\n")
            if search in new_line[int(cmd)-1]:
                print(line)
                print()
            

            # if search in line:
            #     print(line)
            #     print()

