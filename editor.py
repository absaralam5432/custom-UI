

from customtkinter import *
from tkinter import *
from tkinter import ttk
from screeninfo import get_monitors
import ctypes
import re
import os
import pyperclip


class Editor():

    def __init__(self,window) :
        self.window=window
        self.window.state('zoomed') 

        # assing variables 
        self.previousText = ''

        self.BG_GRAY = "#ABB2B9"
        self.BG_COLOR = "#17202A"
        self.BG_COLOR='#36342f'
        self.TEXT_COLOR = "#EAECEE"
        self.FONT = "Helvetica 14"
        self.FONT_BOLD = "Helvetica 13 bold"
        self.current_directory = os.getcwd()
        self.tab_folder={}
        self.active_tab=[]
        self.chat_tab_folder={}

        # Define colors for the variouse types of tokens
        self.normal = self.rgb((234, 234, 234))
        self.keywords = self.rgb((234, 95, 95))
        self.comments = self.rgb((95, 234, 165))
        self.string = self.rgb((234, 162, 95))
        self.function = self.rgb((95, 211, 234))
        self.background = self.rgb((42, 42, 42))
        self.font = 'Consolas 15'


        # Define a list of Regex Pattern that should be colored in a certain way
        self.repl = [
            ['(^| )(False|None|True|and|as|assert|async|await|break|class|continue|def|del|elif|else|except|finally|for|from|global|if|import|in|is|lambda|nonlocal|not|or|pass|raise|return|try|while|with|yield)($| )', self.keywords],
            ['".*?"', self.string],
            ['\'.*?\'', self.string],
            ['#.*?$', self.comments],
        ]

    def init_ui(self):
        
        primary_monitor = get_monitors()[0]
        screen_width, screen_height = primary_monitor.width, primary_monitor.height
        #print(screen_height,screen_width)
        #self.window.geometry((str(screen_width-10))+'x'+(str(screen_height-19)))
        
        self.frm=Frame(self.window,bg='#044447')
        self.frm.pack(expand=1,fill="both")
        # Get the screen resolution of the primary monitor

        # Navigation bar
        menu_bar = Menu(self.frm)
        # files menu bar
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Open Folder",command=self.browse_directory)
        file_menu.add_command(label="Save")
        menu_bar.add_cascade(label="File", menu=file_menu)
        #   edit menu bar
        self.edit_menu = Menu(menu_bar, tearoff=0)
        self.edit_menu.add_command(label="show files",command=self.hide_files)
        self.edit_menu.add_command(label="show chat area",command=self.show_chat)
        menu_bar.add_cascade(label="Edit",menu=self.edit_menu)        

        menu_bar.add_command(label="About")
        self.window.config(menu=menu_bar)

        self.editor_frm=Frame(self.frm,bg='white')
        self.editor_frm.pack(expand=1,fill=BOTH)

        # Create frames for file manager , code area and chat area
        self.files_frame = Frame(self.editor_frm, background="#b3b0a8", width=(screen_width/100)*15)

        self.right_frm = Frame(self.editor_frm, background="white")

        # Pack frames to position them
        self.files_frame.pack(side=LEFT,fill="y")
        self.right_frm.pack(side='right',fill='both',expand=1)
        
        self.upper_frm=Frame(self.right_frm, background="white")
        self.upper_frm.pack(fill='x')
        self.inner_frm=Frame(self.right_frm, background="white")
        self.inner_frm.pack(fill='x')
        
        self.code_frame = Frame(self.inner_frm, background="white")
        self.chat_frame = Frame(self.inner_frm, background="white")

        self.code_frame.pack(side='left',fill='x',expand=1)  # You can also use 'side=RIGHT' for right alignment
        self.chat_frame.pack(side=RIGHT,fill='y')        


        #  ---------------------------------- file manager ---------------------------------

        # Treeview to display files and directories
        file_head_frm=Frame(self.files_frame)
        file_head_frm.pack(fill="x")
        self.copy_btn=CTkButton(file_head_frm,text='copy',width=20,height=20,command=self.copy_text)
        self.browse_btn=CTkButton(file_head_frm,text='Browse',width=20,height=20,command=self.browse_directory)

        #new_file_btn=CTkButton(file_head_frm,text='add',width=20,height=20)
        #self.copy_btn=CTkButton(file_head_frm,text='copy')
        self.copy_btn.pack(side='right',pady=(10,0),padx=(2,20))
        self.browse_btn.pack(side='right',pady=(10,0),padx=(2,2))


        

             # self.tree is show the  folder files 
        self.tree = ttk.Treeview(self.files_frame)
        self.tree.pack(side=LEFT, fill=Y)
        # Scrollbar for the self.tree
        scrollbar = ttk.Scrollbar(self.files_frame, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Bind double-click edit file
        self.tree.bind("<Double-1>", self.on_treeview_select)

        # Update treeview to display files of the current directory
        


        #                           ---------------------------------



        #  ------------------  code editor ---------------------
        header_frm=CTkFrame(self.upper_frm)
        header_frm.pack(fill='x',side='top')

        run_frm=Frame(header_frm,bg='red')
        run_frm.pack(side='right',pady=10,padx=20)
        run_btn=CTkButton(run_frm,text='run',width=50)
        run_btn.pack()

        side_frm=Frame(header_frm)
        side_frm.pack(side='left',fill="both",expand=1)
        Label(side_frm,text="Code Area",font=('helvica',20)).pack(anchor='center',pady=7)
        # ------  create tab frame -------------
        self.tab_frm=Frame(self.code_frame,bg='black')
        self.tab_frm.pack(side='top',fill='x')
        # ---------------------------------------

        self.editor=Text(self.code_frame,
                         background=self.background,
                            foreground=self.normal,
                            insertbackground=self.normal,
                            width=68,
                            relief=FLAT,
                            borderwidth=20,
                            font=self.font
                            
                            )
        self.editor.pack(fill='x')

        
        # Bind the KeyRelase to the Changes Function
        self.editor.bind('<KeyRelease>', self.changes)

        # Bind Control + R to the exec function
        self.window.bind('<Control-r>', self.execute)

        self.changes()
        # -------------------------------



            #  ------------------------------------------  chat area    --------------------------------------------------

                # --------- create tab -----------------
        self.chat_tab_frm=Frame(self.chat_frame,bg='white')
        self.chat_tab_frm.pack(fill='x')
        #self.chat_tab_folder["chat_1"]=[]
        self.chat_tab_folder["chat_1"]=CTkFrame(self.chat_tab_frm,height=10,)
        self.chat_tab_folder["chat_1"].pack(side='left',padx=(2,2))

        lbl=Button(self.chat_tab_folder["chat_1"],text="chat_1",bd=0,borderwidth=0,padx=6,
                   command=lambda _=None: self.swip_tab("chat_1"))
        lbl.pack(side='left',pady=(2,0))
        btn=Button(self.chat_tab_folder["chat_1"],text='x',bd=0,borderwidth=0,
                   command=lambda _=None: self.close_tab("chat_1"))
        btn.pack(side='right',pady=(2,0))
        
        self.chat_add_btn=CTkButton(self.chat_tab_frm,text='+',border_spacing=0,bg_color='yellow',width=10,
                   command=lambda _=None: self.add_chat_tab())
        self.chat_add_btn.pack(side='left',pady=(4,3))

        # -----------------------------------------
        message_frm=Frame(self.chat_frame,bg='red')
        message_frm.pack(fill=BOTH)
        self.text = Text(message_frm,
                         font=self.FONT,height=20)
        self.text.pack(fill=BOTH,expand=1)

        chat_sender_frm=CTkFrame(self.chat_frame,bg_color='#e1e5f0',height=200)
        chat_sender_frm.pack(padx=(10,3),pady=(0,4),fill='both',expand=1)

        Frame(chat_sender_frm,bg='skyblue',height=24,borderwidth=0).pack(fill='x')

        self.sender_message = Text(chat_sender_frm,background='#e1e5f0',height=3,font=self.FONT)
        self.sender_message.pack()

        send_btn_frm=Frame(chat_sender_frm,bg='#e1e5f0',borderwidth=0)
        send_btn_frm.pack(fill=X)

        send_btn=CTkButton(send_btn_frm,text='send',width=10
                           ,corner_radius=10)
        send_btn.pack(padx=10,side='right',pady=(0,4))
        #self.hide_chat()


    def hide_files(self):
        self.files_frame.pack_forget()
        
        self.edit_menu.entryconfigure(0,label='Show files Manager',command=self.show_files)
    def hide_chat(self):
        self.chat_frame.pack_forget()
        self.edit_menu.entryconfigure(1,label='Show CHat',command=self.show_chat)
        

    def show_chat(self):
        self.chat_frame.pack(side=RIGHT,fill="y")
        self.edit_menu.entryconfigure(1,label='Hide CHat',command=self.hide_chat)


    def show_files(self):
        self.code_frame.pack_forget()
        self.files_frame.pack(side=LEFT,fill="y")
        self.code_frame.pack(side=LEFT,expand=1,fill=BOTH)  # You can also use 'side=RIGHT' for right alignment
        self.edit_menu.entryconfigure(0,label='Hide files Manager',command=self.hide_files)

    def delete_frame(self):
        self.frm.forget()


    
    def copy_text(self):
        item = self.tree.selection()[0]  # Get the selected item from the self.treeview
        if item:
            file_path = self.tree.item(item, "text")
            file_path = os.path.join(self.current_directory, file_path)
            pyperclip.copy(file_path)
            
            self.copy_btn.configure(text='copied')
            self.window.after(1000,lambda _='': self.copy_btn.configure(text='copy'))

    # Send function
    def send(self):
        send = "You -> " + self.sender_message.get()
        self.text.insert(END, "\n" + send)
     #   get user input/message
        user = self.sender_message.get().lower()
        # tempory chat conditions ---------
        if (user == "hello"):
            self.text.insert(END, "\n" + "Bot -> Hi there, how can I help?")
    
    def add_chat_tab(self):
        chat_counter='chat_'+str(len(self.chat_tab_folder)+1)
        self.chat_add_btn.pack_forget()
        self.chat_tab_folder[chat_counter]=Frame(self.chat_tab_frm,height=10,bg='black')
        self.chat_tab_folder[chat_counter].pack(side='left',padx=(0,2))

        lbl=Button(self.chat_tab_folder[chat_counter],text=chat_counter,bd=0,borderwidth=0,padx=6,
                   command=lambda _=None: self.swip_tab(chat_counter))
        lbl.pack(side='left',pady=(2,0))
        btn=Button(self.chat_tab_folder[chat_counter],text='x',bd=0,borderwidth=0,
                   command=lambda _=None: self.close_tab(chat_counter))
        btn.pack(side='right',pady=(2,0))
        
        self.chat_add_btn.pack(side='left',pady=(2,0))
        
    def add_tab(self,tab):
        self.active_tab.append(tab)
        self.tab_folder[tab]=Frame(self.tab_frm,height=10,bg='black')
        self.tab_folder[tab].pack(side='left',padx=(0,2))

        lbl=Button(self.tab_folder[tab],text=tab,bd=0,borderwidth=0,padx=6,
                   command=lambda _=None: self.swip_tab(tab))
        lbl.pack(side='left',pady=(2,0))
        btn=Button(self.tab_folder[tab],text='x',bd=0,borderwidth=0,
                   command=lambda _=None: self.close_tab(tab))
        btn.pack(side='right',pady=(2,0))
    
    def swip_tab(self,tab):
        if tab!=self.active_tab[-1]:
            self.active_tab.remove(tab)
            self.active_tab.append(tab)
            self.edit_file(path=tab)

    def close_tab(self,frm):
        self.tab_folder[frm].destroy()
        #print(self.prev_tab,self.current_tab)
#        self.current_tab=self.prev_tab
        self.active_tab.remove(frm)
        if len(self.active_tab)>0:
            self.edit_file(path= self.active_tab[-1])
        else:
            self.editor.delete(1.0,END)

        

        
    # Function to open and edit a file
    def edit_file(self,event=None,path=None):
        item = self.tree.selection()[0]  # Get the selected item from the self.treeview
        print('1 ',item,'2 ',path,'3 ', self.active_tab)
        
        if path!=None :
            print(path)
            file_path=path
            print('condtion 2')

        elif item:
            file_path = self.tree.item(item, "text")
            self.add_tab(file_path)
            print('condtion 3')
        
        print(self.tab_folder,file_path)
        if len(self.active_tab)>0:
            self.tab_folder[file_path].configure(bg='skyblue')
        if len(self.active_tab)>1:
            self.tab_folder[self.active_tab[-2]].configure(bg='gray')

        file_path = os.path.join(self.current_directory, file_path)
        print(file_path)
        if file_path=='----':
            self.update_treeview('/..')
            return
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                self.editor.delete(1.0, END)  # Clear previous content
                self.editor.insert(END, content)
        except Exception as e:
            self.editor.delete(1.0, END)  # Clear self.editor if there's an error
            self.editor.insert(END, str(e))
        self.changes()

        # Function to update the treeview
    def update_treeview(self,directory):

        self.current_directory = directory
        self.tree.delete(*self.tree.get_children())
        self.tree.insert("", "end", text='------')

        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isdir(item_path):
                self.tree.insert("", "end", text=item, open=False)
            else:
                self.tree.insert("", "end", text=item)
    # Function to browse for a directory
    def browse_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.update_treeview(directory)
    # Function to handle directory selection in the treeview
    def on_treeview_select(self,event=None):
        item = self.tree.selection()[0]
        if item:
            directory_path = self.tree.item(item, "text")
        if os.path.isdir(os.path.join(self.current_directory, directory_path)):
            self.update_treeview(os.path.join(self.current_directory, directory_path))
        elif directory_path=='------':
            self.navigate_back()
        else:
            self.edit_file()

        
    # Function to navigate back to the parent directory
    def navigate_back(self):
        parent_directory = os.path.dirname(self.current_directory)
        self.update_treeview(parent_directory)



    # code editor ---------------------
    
        # Execute the Programm
    def execute(self,event=None):
    

        # Write the Content to the Temporary File
        with open('run.py', 'w', encoding='utf-8') as f:
            f.write(self.editor.get('1.0', END))

        # Start the File in a new CMD Window
        os.system('start cmd /K "python run.py"')


    # Register Changes made to the Editor Content
    def changes(self,event=None,stat=True):
        

        # If actually no changes have been made stop / return the function
        #if self.editor.get('1.0', END) == self.previousText and stat:
        #    return

        # Remove all tags so they can be redrawn
        for tag in self.editor.tag_names():
            self.editor.tag_remove(tag, "1.0", "end")

        # Add tags where the search_re function found the pattern
        i = 0
        for pattern, color in self.repl:
            for start, end in self.search_re(pattern, self.editor.get('1.0', END)):
                self.editor.tag_add(f'{i}', start, end)
                self.editor.tag_config(f'{i}', foreground=color)

                i+=1

        self.previousText = self.editor.get('1.0', END) 

    def search_re(self,pattern, text, groupid=0):
        matches = []

        text = text.splitlines()
        for i, line in enumerate(text):
            for match in re.finditer(pattern, line):

                matches.append(
                    (f"{i + 1}.{match.start()}", f"{i + 1}.{match.end()}")
                )

        return matches


    def rgb(self,rgb):
        return "#%02x%02x%02x" % rgb

win=CTk()
win.state('zoomed')
win.config(bg='#044447')

page=Editor(win)
page.init_ui()

win.geometry("700x500")


win.mainloop()