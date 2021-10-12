#login
#parol
import os

import mysql.connector
import getpass


class User:
    def __init__(self):
        self.Name = None
        self.Surname = None
        self.Age = None
        self.Log_in = None
        self.Password = None
        self.passwords = []
        self.logins = []
        self.logins_and_passwords = []
        self.logins_passwords ()

    def enter_the_system(self):
        pass
        self.frontend()
        user_choice = ['1','2','3','4','5']
        user_input = input("Nima qilmoqchisiz: ")
        while user_input not in user_choice:
            print("Boshqatdan kiriting:")
            user_input = input("Nima qilmoqchisiz: ")
        if user_input == user_choice [0]:
            self.registr()
        elif user_input == user_choice [1]:
            self.login_enter()
        elif user_input == user_choice[2]:
            self.chang_login()
        elif user_input == user_choice[3]:
            self.log_out()
        elif user_input == user_choice[4]:
            self.delete_account()




    def registr(self):
        name = input("Ismingizni kiriting: ").strip()
        while not name.isalpha() or len(name) < 3:
            self.clear_str()
            print("To'g'ri kiriting")
            name = input("Ismingizni kiriting: ").strip()

        self.clear_str()
        surname = input("Familiyangizni kiriting: ")
        while not surname.isalpha() or len(name) < 4:
            self.clear_str()
            print("To'g'ri kiriting")
            surname = input("Ismingizni kiriting: ")

        self.clear_str()
        age = input("Yoshingizni kiriting ").strip()
        while not age.isnumeric():
            self.clear_str()
            print("To'g'ri kiriting")
            age = input("Yoshingizni kiriting ").strip()

        self.clear_str()
        login = input("Login kiriting: ").strip()
        while not login.isalnum():
            self.clear_str()
            print("Boshqatdan kiriting")
            login = input("Login kiriting: ").strip()

        self.clear_str()
        password = getpass.getpass("Parol kiriting: ko'rinmaydi").strip()
        password1 = getpass.getpass("Parolni tasdiqlang: ko'rinmaydi").strip()
        while self.matn_bosh(password) or password1 != password:
            password = getpass.getpass("Xato: Qaytadan: ko'rinmaydi").strip()
            password1 = getpass.getpass("Xato: Qaytadan: ko'rinmaydi").strip()

        self.Name = name
        self.Surname = surname
        self.Age = age
        self.Log_in = login
        self.Password = password
        my_data = self.database()
        mycursor = my_data.cursor()
        mycursor.execute(f"insert into info (Name, Surname, Age, Login, Password) values ('{self.Name}','{self.Surname}','{self.Age}','{self.Log_in}','{self.Password}')")
        my_data.commit()
        print("Muvaffaqiyatli ro'yxatdan o'tdingiz")


    def login_enter(self):
        print("Tizimga kirish uchun Login va Parolingizni kiriting:")
        login_user = input("Login: ").strip()
        self.clear_str()
        while not login_user.isalnum() not in self.logins:
            self.clear_str()
            print("Qaytadan kiriting:")
            login_user = input("Login: ").strip()
        my_data = self.database()
        mycursor = my_data.cursor()
        mycursor.execute(f"select password from info where login = '{login_user}'")
        logi = None
        for i in mycursor:
            logi = i[0]
        self.clear_str()
        password = getpass.getpass("Parol: ")
        while password != logi:
            self.clear_str()
            print("Xato qaytadan kiriting: ")
            password = getpass.getpass("Parol: ")
        self.clear_str()
        print("Tizimga xush kelibsiz")



    def chang_login(self):
        self.clear_str()
        login_user = input("Login: ").strip()
        self.clear_str()
        while not login_user.isalnum() not in self.logins:
            self.clear_str()
            print("Qaytadan kiriting:")
            login_user = input("Login: ").strip()
        my_data = self.database()
        mycursor = my_data.cursor()
        mycursor.execute(f"select password from info where login = '{login_user}'")
        logi = None
        for i in mycursor:
            logi = i[0]
        self.clear_str()
        password = getpass.getpass("Parol: ")
        while password != logi:
            self.clear_str()
            print("Xato qaytadan kiriting: ")
            password = getpass.getpass("Parol: ")
        self.clear_str()
        insert_new_login = input("Yangi login:").strip()
        while not insert_new_login.isalnum() or insert_new_login in self.logins:
            self.clear_str()
            print("Error: Qaytadan kiriting:")
            insert_new_login = input("Yangi login:").strip()


        self.clear_str()
        insert_new_password = input("Yangi parol:").strip()
        while not insert_new_password.isnumeric() or insert_new_password in self.passwords:
            self.clear_str()
            print("Error: Qaytadan kiriting:")
            insert_new_password = input("Yangi parol:").strip()
        my_data = self.database()
        mycursor = my_data.cursor()
        mycursor.execute(f"update info set login = '{insert_new_login}', password = '{insert_new_password}'")
        my_data.commit()

    def log_out(self):
        print("Tizmdan chiqdindiz")
        exit()


    def delete_account(self):
        self.clear_str()
        login_user = input("Login: ").strip()
        self.clear_str()

        while not login_user.isalnum() not in self.logins:
            self.clear_str()
            print("Qaytadan kiriting:")
            login_user = input("Login: ").strip()

        my_data = self.database()
        mycursor = my_data.cursor()
        mycursor.execute(f"select Password from info where login = '{login_user}'")
        logi = None

        for i in mycursor:
            logi = i[0]
        self.clear_str()
        password_user = input("Parol:")

        while password_user != logi:
            print("Xato qaytdan kiriting")
            password_user = input("Parol:")
        self.clear_str()
        input("Enterni bossangiz kettiz")

        my_data = self.database()
        mycursor = my_data.cursor()
        mycursor.execute(f"delete from info where Login = '{login_user}'")
        my_data.commit()
        print("Delete account")


     def logins_passwords (self):
        my_dbasa = self.database()
        mycursor = my_dbasa.cursor()
        mycursor.execute("select Login, Password from info")
        for i in mycursor:
            self.logins_and_passwords.append(i)
            for j in self.logins_and_passwords:
                self.logins.append(j[0])
                self.passwords.append(j[1])

    def frontend(self):
        print("""Assalomu alaykum 
                Ro'yxatdan o'tish       [1]
                Login                   [2]
                Loginni o'zgartirish    [3]
                Dasturdan chiqib ketish [4]
                Delete account          [5]            

                                    """)

    @staticmethod
    def database():
        return mysql.connector.connect(
        host="localhost",
        user="admin",
        password="123456789",
        database="userinfo"
            )

    @staticmethod
    def clear_str():
        os.system("clear")

    @staticmethod
    def matn_bosh(str):
        return not bool(str)



user1 = User()
user1.enter_the_system()