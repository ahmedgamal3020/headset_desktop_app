from customtkinter import *
import dashboard
from urllib.parse import quote_plus
import pandas as pd
from sqlalchemy.engine import create_engine

uri = "postgresql://postgres:%s@localhost/postgres" % quote_plus("123321")
engine = create_engine(uri)
login_data = pd.read_sql('''
        select * from login
        ''',engine)

def getmeframe(app,parent_hight,parent_width,frame=""):
    if(frame == ""):
        pass
    else:
        frame.pack_forget()
    toggel=True
    def but(t):
        username=str(user_name.get())
        password=str(user_pass.get())
        if username.lower() in list(login_data['username']) and password.lower()in list(login_data['password']):
            dashboard.Dashboard(app=app,parent_hight=parent_hight,parent_width=parent_width,old_frame=frame)
            frame.pack_forget()
        else :
                    
            checkbox = CTkLabel(master=frame, 
                                text='Wrong username or password',text_color='red') 
            checkbox.grid(row=5,column=0,pady=12,padx=10)

            user_name.delete(0,END)
            user_pass.delete(0,END) 
        
           
             
    def press_enter(event):
        username=str(user_name.get())
        password=user_pass.get()
        if username.lower() in list(login_data['username']) and password.lower()in list(login_data['password']):
            dashboard.Dashboard(app=app,parent_hight=parent_hight,parent_width=parent_width,old_frame=frame)
            frame.pack_forget()
 
        else :
                checkbox = CTkLabel(master=frame, 
                                text='Wrong username or password',text_color='red') 
                checkbox.grid(row=5,column=0,pady=12,padx=10) 
                user_name.delete(0,END)
                user_pass.delete(0,END) 
    

            

    frame = CTkFrame(master=app) 
    # Set the label inside the frame 
    label = CTkLabel(master=frame, 
                        text=' Login!',font=CTkFont(family='bold',size=30)) 
    label.grid(row=0,column=0,pady=12,padx=10)  

    # Create the text box for taking 
    # username input from user 
    user_name= CTkEntry(master=frame, 
                            placeholder_text="Username",corner_radius=15) 
    user_name.grid(row=1,column=0,pady=12,padx=10) 
    user_name.bind("<Return>",press_enter)
    
    # Create a text box for taking 
    # password input from user 
    user_pass= CTkEntry(master=frame, 
                            placeholder_text="Password",corner_radius=15,
                            show="*") 
    user_pass.grid(row=2,column=0,pady=12,padx=10) 
    user_pass.bind("<Return>",press_enter)
    

    # Create a login button to login 
    button = CTkButton(master=frame, 
                        text='Login',command=lambda: but(t=toggel)) 
    button.grid(row=3,column=0,pady=12,padx=10) 

    # Create a remember me checkbox 
    checkbox = CTkCheckBox(master=frame, 
                            text='Remember Me') 
    checkbox.grid(row=4,column=0,pady=12,padx=10) 
    

    return frame





