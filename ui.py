import random
from tkinter import *
from tkinter.ttk import *

class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_text_m27qkagn = self.__tk_text_m27qkagn(self)
        self.tk_button_m27qm1i7 = self.__tk_button_m27qm1i7(self)
        self.tk_label_m27qqav2 = self.__tk_label_m27qqav2(self)
        
    def __win(self):
        self.title("微信多开助手")
        # 设置窗口大小、居中
        width = 320
        height = 80
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        
        self.resizable(width=False, height=False)
        
    def scrollbar_autohide(self,vbar, hbar, widget):
        """自动隐藏滚动条"""
        def show():
            if vbar: vbar.lift(widget)
            if hbar: hbar.lift(widget)
        def hide():
            if vbar: vbar.lower(widget)
            if hbar: hbar.lower(widget)
        hide()
        widget.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Leave>", lambda e: hide())
        if hbar: hbar.bind("<Enter>", lambda e: show())
        if hbar: hbar.bind("<Leave>", lambda e: hide())
        widget.bind("<Leave>", lambda e: hide())
    
    def v_scrollbar(self,vbar, widget, x, y, w, h, pw, ph):
        widget.configure(yscrollcommand=vbar.set)
        vbar.config(command=widget.yview)
        vbar.place(relx=(w + x) / pw, rely=y / ph, relheight=h / ph, anchor='ne')
        
    def h_scrollbar(self,hbar, widget, x, y, w, h, pw, ph):
        widget.configure(xscrollcommand=hbar.set)
        hbar.config(command=widget.xview)
        hbar.place(relx=x / pw, rely=(y + h) / ph, relwidth=w / pw, anchor='sw')
        
    def create_bar(self,master, widget,is_vbar,is_hbar, x, y, w, h, pw, ph):
        vbar, hbar = None, None
        if is_vbar:
            vbar = Scrollbar(master)
            self.v_scrollbar(vbar, widget, x, y, w, h, pw, ph)
        if is_hbar:
            hbar = Scrollbar(master, orient="horizontal")
            self.h_scrollbar(hbar, widget, x, y, w, h, pw, ph)
        self.scrollbar_autohide(vbar, hbar, widget)
        
    def __tk_text_m27qkagn(self,parent):
        text = Text(parent)
        text.place(x=100, y=16, width=116, height=50)
        return text
    
    def __tk_button_m27qm1i7(self,parent):
        btn = Button(parent, text="打开", takefocus=False,)
        btn.place(x=226, y=16, width=80, height=50)
        return btn
    
    def __tk_label_m27qqav2(self,parent):
        label = Label(parent,text="数量",anchor="center", )
        label.place(x=10, y=16, width=85, height=50)
        return label
    
class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        self.ctl.init(self)
        
    def __event_bind(self):
        self.tk_button_m27qm1i7.bind('<Button>',self.ctl.open_wechat)
        pass
    
    def __style_config(self):
        pass
