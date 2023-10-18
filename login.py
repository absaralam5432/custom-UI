import customtkinter as ctk 
import tkinter.messagebox as tkmb 
from start_page import Start_Page
from customtkinter import *
from tkinter import *


class Login_Page():
    def __init__(self,window) -> None:
        self.window=window
    # ------------------------------   UI Login page --------------------------------------
    def init_ui(self):
        # create a login page on main frame
        self.login_frm=Frame(self.window,bg='white')
        self.login_frm.pack(expand=1)
        
        # set text and desing
        title=CTkLabel(self.login_frm,text="Gitturbo.com",font=('Britannic Bold',40),fg_color='white',bg_color='white',text_color='black',width=100)
        title.pack(anchor='center',pady=(0,20))

        heading=CTkLabel(self.login_frm,text="   AI Coding Agents At Your Finger",font=('Britannic Bold',20),fg_color='white',bg_color='white',text_color='black',width=100)
        heading.pack(anchor='center',pady=0)
        border_line=Frame(self.login_frm,border=4,bg='black')
        border_line.pack(fill=X,padx=50,pady=(30,10))

        login_lbl=CTkLabel(self.login_frm,text="Login",font=('Britannic Bold',20),fg_color='white',bg_color='white',text_color='black',width=100)
        login_lbl.pack(anchor='center',pady=0)

        
        
        user_entry_frm=Frame(self.login_frm,bg='white')
        user_entry_frm.pack(anchor='center',pady=20)

        key_lbl=CTkLabel(user_entry_frm,text="User :",font=('Britannic Bold',20),fg_color='white',bg_color='white',text_color='black')
        key_lbl.pack(side='left',padx=20)
        # get the user name 
        self.user_entry=CTkEntry(user_entry_frm,width=250,placeholder_text='User')
        self.user_entry.pack()

        password_frm=Frame(self.login_frm,bg='white')
        password_frm.pack(anchor='center',pady=0)

        password_lbl=CTkLabel(password_frm,text="Password:",font=('Britannic Bold',20),fg_color='white',bg_color='white',text_color='black')
        password_lbl.pack(side='left',padx=20)
        # get the password
        self.password_entry=CTkEntry(password_frm,width=240,placeholder_text='Password',show='*')
        self.password_entry.pack()

        login_frm=Frame(self.login_frm,bg='white')
        login_frm.pack(fill='x')

        # login button to verify account        
        login_btn=CTkButton(login_frm,text="Login",text_color='black',fg_color='#34e1eb',
                           corner_radius=10,width=70,command=self.verification)
        login_btn.pack(side='right',pady=7,padx=10)
         
        # sing up button to redirect the signup page
        sign_btn=CTkButton(login_frm,text="Sign Up",text_color='black',fg_color='#34e1eb',
                           corner_radius=10,width=70,command=self.signup)
        sign_btn.pack(side='right',pady=7)


        # bind the "enter" key to call the verification 
        self.password_entry.bind('<Return>',self.verification)
        #  set/focus  the cursor on text box
        self.user_entry.focus_set()


    #  -------------------------------- UI sign up page --------------------------------------    
    def signup_ui(self):

        # frame of signup page 
        self.signup_frm=Frame(self.window,bg='white')
        self.signup_frm.pack(expand=1)
        
        title=CTkLabel(self.signup_frm,text="Gitturbo.com",font=('Britannic Bold',40),fg_color='white',bg_color='white',text_color='black',width=100)
        title.pack(anchor='center',pady=(0,20))

        heading=CTkLabel(self.signup_frm,text="   AI Coding Agents At Your Finger",font=('Britannic Bold',20),fg_color='white',bg_color='white',text_color='black',width=100)
        heading.pack(anchor='center',pady=0)

        border_line=Frame(self.signup_frm,border=4,bg='black')
        border_line.pack(fill=X,padx=50,pady=(30,10))

        singup_lbl=CTkLabel(self.signup_frm,text="sing Up",font=('Britannic Bold',20),fg_color='white',bg_color='white',text_color='black',width=100)
        singup_lbl.pack(anchor='center',pady=0)

        
                    #    frame of  user entry with label       
        user_entry_frm=Frame(self.signup_frm,bg='white')
        user_entry_frm.pack(anchor='center',pady=20)
        user_lbl=CTkLabel(user_entry_frm,text="User :",font=('Britannic Bold',20),fg_color='white',bg_color='white',text_color='black')
        user_lbl.pack(side='left',padx=20)
         # text box for get input name from user 
        self.sign_user_entry=CTkEntry(user_entry_frm,width=250,placeholder_text='User')
        self.sign_user_entry.pack()


        sign_password_frm=Frame(self.signup_frm,bg='white')
        sign_password_frm.pack(anchor='center',pady=0)
        password_lbl=CTkLabel(sign_password_frm,text="Password:",font=('Britannic Bold',20),fg_color='white',bg_color='white',text_color='black')
        password_lbl.pack(side='left',padx=20)
            # get password from user
        self.sign_password_entry=CTkEntry(sign_password_frm,width=240,placeholder_text='Password',show='*')
        self.sign_password_entry.pack()

        confirm_password_frm=Frame(self.signup_frm,bg='white')
        confirm_password_frm.pack(anchor='center',pady=10)

        confirm_lbl=CTkLabel(confirm_password_frm,text="Confirm: ",font=('Britannic Bold',20),fg_color='white',bg_color='white',text_color='black')
        confirm_lbl.pack(side='left',padx=20)
        # get confirm password from user ---
        self.sign_confirm_entry=CTkEntry(confirm_password_frm,width=240,placeholder_text='confirm Password',show='*')
        self.sign_confirm_entry.pack()

        login_frm=Frame(self.signup_frm,bg='white')
        login_frm.pack(fill='x')
        # button for register the user account
        signup_btn=CTkButton(login_frm,text="Register",text_color='black',fg_color='#34e1eb',
                           corner_radius=10,width=70,command=self.register)
        signup_btn.pack(side='right',pady=7,padx=10)
    
    def register(self):
        # register account
        self.sign_user_entry.get()#user name
        self.sign_password_entry.get() # get password
        self.sign_confirm_entry.get() # get confirm password
        # you can apply condition ......... 
        # and it true so call this funtion to redirect login page
        self.signup_frm.pack_forget()
        self.show_login_page()


    # redirect signup page
    def signup(self):
        # delete login page 
        self.delete_frame()
        # make sing up page
        self.signup_ui()
    
    # show the login page 
    def show_login_page(self):
        self.login_frm.pack(expand=1)
    
    # hide the login page 
    def delete_frame(self):
        self.login_frm.forget()

    # veify the user account
    def verification(self,e=None):
        username = "hello"
        password='12345'

        if self.user_entry.get()==username and self.password_entry.get()==password:
            # if account is verfy so 
            #create object for start page 
            start_p=Start_Page(self.window)
            # now remove the login page
            self.delete_frame()
            # now show the start page
            start_p.init_ui()


        elif self.user_entry.get()==username and self.password_entry.get()!=password:
            tkmb.showwarning(title='Wrong password',message='Please check your password')
        elif self.user_entry.get()!=username and self.password_entry.get()==password:
            tkmb.showwarning(title='Wrong Username',message='Please check your User Name')
        else:tkmb.showerror(title="Login Failed",message="Invalid Username and password")

        
        


win=CTk()
win.config(bg='white')

page=Login_Page(win)
page.init_ui()

win.geometry("700x500")


win.mainloop()

