

from customtkinter import *
from tkinter import *
from screeninfo import get_monitors
class Editor():
    def __init__(self,window) :
        self.window=window

    def init_ui(self):

        BG_GRAY = "#ABB2B9"
        BG_COLOR = "#17202A"
        BG_COLOR='#36342f'
        TEXT_COLOR = "#EAECEE"
        FONT = "Helvetica 14"
        FONT_BOLD = "Helvetica 13 bold"

        primary_monitor = get_monitors()[0]
        screen_width, screen_height = primary_monitor.width, primary_monitor.height
        #print(screen_height,screen_width)
        #self.window.geometry((str(screen_width-10))+'x'+(str(screen_height-19)))
        self.window.state('zoomed') 
        
        self.frm=Frame(self.window,bg='#044447')
        self.frm.pack(expand=1,fill="both")
        # Get the screen resolution of the primary monitor

        # Navigation bar
        menu_bar = Menu(self.frm)
        # files menu bar
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Open")
        file_menu.add_command(label="Save")
        menu_bar.add_cascade(label="File", menu=file_menu)
        #   edit menu bar
        self.edit_menu = Menu(menu_bar, tearoff=0)
        self.edit_menu.add_command(label="show files",command=self.show_files)
        self.edit_menu.add_command(label="chat area",command=self.show_chat)
        menu_bar.add_cascade(label="Edit",menu=self.edit_menu)        

        menu_bar.add_command(label="About")
        self.window.config(menu=menu_bar)

        self.editor_frm=Frame(self.frm,bg='white')
        self.editor_frm.pack(expand=1,fill=BOTH)

        # Create frames for left, center, and right
        self.files_frame = Frame(self.editor_frm, background="blue", width=(screen_width/100)*15)
        self.code_frame = Frame(self.editor_frm, background="lightgreen", width=400)
        self.chat_frame = Frame(self.editor_frm, background="lightyellow", 
                                width=(screen_width/100)*15,bg=BG_COLOR,border=20)

        # Pack frames to position them
        self.files_frame.pack(side=LEFT,fill="y")
        self.code_frame.pack(side=LEFT,expand=1,fill=BOTH)  # You can also use 'side=RIGHT' for right alignment
        self.chat_frame.pack(side=RIGHT,fill="y")        

        #file manager ---------------------
        #....................
        # ---------------------------------
        #code editor ---------------------
        code=Text(self.code_frame,font=FONT)
        code.pack(fill=BOTH,expand=1)
        # -------------------------------

        lable1 = Label(self.chat_frame, bg=BG_COLOR, fg=TEXT_COLOR, text="Chat Area",
                        font=FONT_BOLD, pady=10, width=20, height=1).pack(side='top')
        
        self.text = Text(self.chat_frame,fg=BG_GRAY,
                           font=FONT, width=15)
        self.text.pack(fill="x",)
        
        #scrollbar = Scrollbar(self.text)
        #scrollbar.place(relheight=1, relx=0.974)
        #e.grid(row=2, column=0)
        
        msg_frm=Frame(self.chat_frame)
        msg_frm.pack(fill='x')
        self.message = Entry(self.chat_frame, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=15)
        self.message.pack(side='left')
        send = Button(self.chat_frame, text="Send", font=FONT_BOLD, bg=BG_GRAY,command=self.send)#.grid(row=2, column=1)
        send.pack(side='right')
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


    def crate_project(self):
        self.delete_frame()
    # Send function
    def send(self):
        send = "You -> " + self.message.get()
        self.text.insert(END, "\n" + send)
    
        user = self.message.get().lower()
    
        if (user == "hello"):
            self.text.insert(END, "\n" + "Bot -> Hi there, how can I help?")
    
        elif (user == "hi" or user == "hii" or user == "hiiii"):
            self.text.insert(END, "\n" + "Bot -> Hi there, what can I do for you?")
    
        elif (user == "how are you"):
            self.text.insert(END, "\n" + "Bot -> fine! and you")
    
        elif (user == "fine" or user == "i am good" or user == "i am doing good"):
            self.text.insert(END, "\n" + "Bot -> Great! how can I help you.")
    
        elif (user == "thanks" or user == "thank you" or user == "now its my time"):
            self.text.insert(END, "\n" + "Bot -> My pleasure !")
    
        elif (user == "what do you sell" or user == "what kinds of items are there" or user == "have you something"):
            self.text.insert(END, "\n" + "Bot -> We have coffee and tea")
    
        elif (user == "tell me a joke" or user == "tell me something funny" or user == "crack a funny line"):
            self.text.insert(
                END, "\n" + "Bot -> What did the buffalo say when his son left for college? Bison.! ")
    
        elif (user == "goodbye" or user == "see you later" or user == "see yaa"):
            self.text.insert(END, "\n" + "Bot -> Have a nice day!")
    
        else:
            self.text.insert(END, "\n" + "Bot -> Sorry! I didn't understand that")
    
        self.message.delete(0, END)
win=CTk()
win.state('zoomed')
win.config(bg='#044447')

page=Editor(win)
page.init_ui()

win.geometry("700x500")


win.mainloop()