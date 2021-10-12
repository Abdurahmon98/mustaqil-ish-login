#login
#parol
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
        #self.logins_passwords ()

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
            print("To'g'ri kiriting")
            name = input("Ismingizni kiriting: ").strip()



        surname = input("Familiyangizni kiriting: ")
        while not surname.isalpha() or len(name) < 4:
            print("To'g'ri kiriting")
            surname = input("Ismingizni kiriting: ")



        age = input("Yoshingizni kiriting ").strip()
        while not age.isnumeric():
            print("To'g'ri kiriting")
            age = input("Yoshingizni kiriting ").strip()


        login = input("Login kiriting: ").strip()
        while not login.isalnum():
            print("Boshqatdan kiriting")
            login = input("Login kiriting: ").strip()


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
        print("men loginman")


    def chang_login(self):
        print("men change loginman")


    def log_out(self):
        print("logoutman")

    def delete_account(self):
        print("deleete")

























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
    def matn_bosh(str):
        return not bool(str)



user1 = User()
user1.enter_the_system()