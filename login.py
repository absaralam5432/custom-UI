import customtkinter as ctk 
import tkinter.messagebox as tkmb 
from start_page import Start_Page




from customtkinter import *
from tkinter import *

class Login_Page():
    def __init__(self,window) -> None:
        self.window=window

    def init_ui(self):

        self.frm=Frame(self.window,bg='white')
        self.frm.pack(expand=1)

        title=CTkLabel(self.frm,text="Gitturbo.com",font=('Britannic Bold',40),fg_color='white',bg_color='white',text_color='black',width=100)
        title.pack(anchor='center',pady=(0,20))

        heading=CTkLabel(self.frm,text="   AI Coding Agents At Your Finger",font=('Britannic Bold',20),fg_color='white',bg_color='white',text_color='black',width=100)
        heading.pack(anchor='center',pady=0)
        border_line=Frame(self.frm,border=4,bg='black')
        border_line.pack(fill=X,padx=50,pady=(30,10))

        login_lbl=CTkLabel(self.frm,text="Login",font=('Britannic Bold',20),fg_color='white',bg_color='white',text_color='black',width=100)
        login_lbl.pack(anchor='center',pady=0)

        
        
        key_entry_frm=Frame(self.frm,bg='white')
        key_entry_frm.pack(anchor='center',pady=20)

        key_lbl=CTkLabel(key_entry_frm,text="User :",font=('Britannic Bold',20),fg_color='white',bg_color='white',text_color='black')
        key_lbl.pack(side='left',padx=20)
        self.user_entry=CTkEntry(key_entry_frm,width=250,placeholder_text='User')
        self.user_entry.pack()

        password_frm=Frame(self.frm,bg='white')
        password_frm.pack(anchor='center',pady=0)

        password_lbl=CTkLabel(password_frm,text="Password:",font=('Britannic Bold',20),fg_color='white',bg_color='white',text_color='black')
        password_lbl.pack(side='left',padx=20)
        self.password_entry=CTkEntry(password_frm,width=240,placeholder_text='Password',show='*')
        self.password_entry.pack()

        save_frm=Frame(self.frm,bg='white')
        save_frm.pack(fill='x')
        save_btn=CTkButton(save_frm,text="Login",text_color='black',fg_color='#34e1eb',corner_radius=10,width=70)
        save_btn.pack(side='right',pady=7)
        self.password_entry.bind('<Return>',self.verification)
        self.user_entry.focus_set()
    def delete_frame(self):
        self.frm.forget()
    def verification(self,e=None):
        username = "geeks"
        password='12345'

        if self.user_entry.get()==username and self.password_entry.get()==password:
            start_p=Start_Page(self.window)
            self.delete_frame()
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


# Selecting GUI theme - dark, light , system (for system default) 
#ctk.set_appearance_mode("dark") 

# Selecting color theme - blue, green, dark-blue 
#ctk.set_default_color_theme("blue") 

#app = ctk.CTk() 
#app.geometry("400x400") 
#app.title("Modern Login UI using Customtkinter") 


#def login(): 
#
#	username = "Geeks"
#	password = "12345"
#	new_window = ctk.CTkToplevel(app) 
#
#	new_window.title("New Window") 
#
#	new_window.geometry("350x150") 

	#if user_entry.get() == username and user_pass.get() == password: 
	#	tkmb.showinfo(title="Login Successful",message="You have logged in Successfully") 
	#	ctk.CTkLabel(new_window,text="GeeksforGeeks is best for learning ANYTHING !!").pack() 
	#elif user_entry.get() == username and user_pass.get() != password: 
	#	tkmb.showwarning(title='Wrong password',message='Please check your password') 
	#elif user_entry.get() != username and user_pass.get() == password: 
	#	tkmb.showwarning(title='Wrong username',message='Please check your username') 
	#else: 
	#	tkmb.showerror(title="Login Failed",message="Invalid Username and password") 



#label = ctk.CTkLabel(app,text="This is the main UI page") 
#
#label.pack(pady=20) 


#frame = ctk.CTkFrame(master=app) 
#frame.pack(pady=20,padx=40,fill='both',expand=True) 
#
#label = ctk.CTkLabel(master=frame,text='Modern Login System UI') 
#label.pack(pady=12,padx=10) 
#
#
#user_entry= ctk.CTkEntry(master=frame,placeholder_text="Username") 
#user_entry.pack(pady=12,padx=10) 
#
#user_pass= ctk.CTkEntry(master=frame,placeholder_text="Password",show="*") 
#user_pass.pack(pady=12,padx=10) 
#
#
#button = ctk.CTkButton(master=frame,text='Login',command=login) 
#button.pack(pady=12,padx=10) 
#
#checkbox = ctk.CTkCheckBox(master=frame,text='Remember Me') 
#checkbox.pack(pady=12,padx=10) 
#

