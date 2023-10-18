from customtkinter import *
from tkinter import *
from editor import Editor
class Start_Page():
    def __init__(self,window) :
        self.window=window

    def init_ui(self):
        self.window.config(bg='#43b3cc')
        self.frm=Frame(self.window,bg='#43b3cc')
        self.frm.pack(expand=1)

        title=CTkLabel(self.frm,text="Gitturbo.com",font=('Britannic Bold',40),
                       fg_color='#43b3cc',bg_color='#43b3cc',text_color='black',width=100)
        title.pack(anchor='center',pady=(0,20))

        heading=CTkLabel(self.frm,text="   AI Coding Agents At Your Finger",font=('Britannic Bold',20),fg_color='#43b3cc',bg_color='#43b3cc',text_color='black',width=100)
        heading.pack(anchor='center',pady=0)

        btn_frm=Frame(self.frm,bg='#43b3cc')
        btn_frm.pack(anchor='center',pady=20)

        load_btn=CTkButton(btn_frm,text="Load Project",text_color='black',fg_color='#34e1eb',
                           corner_radius=10,command=self.create_project)
        load_btn.pack(side='left',padx=30,pady=10,anchor='center')

        new_project_btn=CTkButton(btn_frm,text="Create A New Project",text_color='black',
                                  corner_radius=10,fg_color='#34e1eb',command=self.create_project)
        new_project_btn.pack(side='left',padx=30,pady=10,anchor='center')
        
        key_entry_frm=Frame(self.frm,bg='#43b3cc')
        key_entry_frm.pack(anchor='center',pady=20)

        key_lbl=CTkLabel(key_entry_frm,text="Open AI Api Key:",font=('Britannic Bold',20),fg_color='#43b3cc',bg_color='#43b3cc',text_color='black')
        key_lbl.pack(side='left',padx=20)
        key_entry=Entry(key_entry_frm,width=50)
        key_entry.pack()
        key_entry.focus_set()

        proxy_frm=Frame(self.frm,bg='#43b3cc')
        proxy_frm.pack(anchor='center',pady=0)

        proxy_lbl=CTkLabel(proxy_frm,text="Proxy Address(Optional):",font=('Britannic Bold',20),fg_color='#43b3cc',bg_color='#43b3cc',text_color='black')
        proxy_lbl.pack(side='left',padx=20)
        proxy_entry=Entry(proxy_frm,width=40)
        proxy_entry.pack()

        save_frm=Frame(self.frm,bg='#43b3cc')
        save_frm.pack(fill='x')
        save_btn=CTkButton(save_frm,text="Save",text_color='black',fg_color='#34e1eb',
                           corner_radius=10,width=70,command=self.create_project)
        save_btn.pack(side='right',pady=7)

    def delete_frame(self):
        self.frm.forget()

    def create_project(self):

        self.frm.forget()
        editor=Editor(self.window)
        editor.init_ui()
        


#win=CTk()
#win.config(bg='#43b3cc')
#
#page=Start_Page(win)
#page.init_ui()
#
#win.geometry("700x500")
#
#
#win.mainloop()