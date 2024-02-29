from customtkinter import *
import login
import ctypes

# Selecting GUI theme - dark, 
# light , system (for system default) 
set_appearance_mode("dark") 
# Selecting color theme-blue, green, dark-blue 

set_default_color_theme("dark-blue") 
set_window_scaling(1)

class App(CTk):
    def __init__(self):
        super().__init__()
        self.parent_hight = 700
        self.parent_width = 900
        
    def get_screen_resolution(self):
        user32 = ctypes.windll.user32
        width = user32.GetSystemMetrics(1)
        height = user32.GetSystemMetrics(1)/1.5
        return width, height 
    def resize_window(self):
        self.parent_width,self.parent_hight= self.get_screen_resolution()
        self.geometry(f"{self.parent_width}x{self.parent_hight}")
        self.main_frame = login.getmeframe(self,self.parent_hight,self.parent_width)
        self.main_frame.pack(anchor='s',pady=self.parent_hight*1/6)
    

app = App()
app.iconbitmap("assets\icon-headset_87991.ico")
app.title('Headset System')
app.resize_window()
app.mainloop()
