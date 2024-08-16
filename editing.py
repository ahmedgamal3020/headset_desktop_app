from customtkinter import *
import  dashboard 
import pandas as pd

import tkinter as tk

   


def details_about(self,app,tabs,dt_string='' ,frame="",american_name='',serial='',name='',id='',date='',headset_type=''):
    if frame == "":
        pass
    else:
        frame.pack_forget()
 
    cl= dashboard.Dashboard
    connection=cl.connection
    cursor=cl.cursor
    def commit(sql):
        connection.commit()
        cursor.execute(query=sql)
        cursor.execute('commit')
      
    
    american_n = tk.StringVar()
    american_n.set(american_name)
    ser = tk.StringVar()
    ser.set(serial)
    na = StringVar()
    na.set(name)
    agent_id = tk.StringVar()
    agent_id.set(id)
    da = tk.StringVar()
    da.set(date)
    type = tk.StringVar()
    type.set(headset_type)
    font_1 = CTkFont(family="arial", weight="bold", size=40)
    font2 = CTkFont(family="arial", size=30)
    current_date =dt_string
    cl.headset_data=pd.read_sql(''' select
                                 serial,
                                status,
                                agent_id,
                                date,
                                name from headset
                               ''',cl.engine)
    checkbox1_var = tk.BooleanVar()
    checkbox2_var = tk.BooleanVar()
    def toggle_checkbox1(*args):
        if checkbox1_var.get():
            checkbox2_var.set(False)
    
    def toggle_checkbox2(*args):
        if checkbox2_var.get():
            checkbox1_var.set(False)

    def delete_state():
        if checkbox1_var.get():

            sql=(f"""
                    update headset 
                    set status='available',serial='{serial}',name='-',agent_id='-',date='-'
                        where  lower(serial)='{serial.strip().replace(' ', '').lower()}' 
                            """)
            commit(sql=sql)

            
            sql=(f"""
                update serial_hestory 
                set last_date='{current_date}'
                    where  lower(serial)='{serial.strip().replace(' ', '').lower()}' and lower(agent_name)='{ent1.get().lower()}' 
                        """)

            commit(sql=sql)


            ent1.delete(0,END)
            ent2.delete(0,END)
            ent3.delete(0,END)
            ent4.delete(0,END)
            ent5.delete(0,END)
            
            cl.refresh_data(self)

            tabs.set("Dashboard")
            tabs.configure("Dashboard")
       
        elif checkbox2_var.get():
            sql=(f"""
                    update headset 
                    set status='not available',serial='{serial}',name='-',agent_id='-',date='-'
                        where  lower(serial)='{serial.strip().replace(' ', '').lower()}' 
                        """)
            commit(sql=sql)

           

            sql=(f"""
                update serial_hestory 
                set last_date='{current_date}'
                    where  lower(serial)='{serial.strip().replace(' ', '').lower()}' and lower(agent_name)='{ent1.get().lower()}' 
                        """)

            commit(sql=sql)


            
    

            ent1.delete(0,END)
            ent2.delete(0,END)
            ent3.delete(0,END)
            ent4.delete(0,END)
            ent5.delete(0,END)
            
            cl.refresh_data(self)

            tabs.set("Dashboard")
            tabs.configure("Dashboard")
       
        else:
            label_6.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
    
    def update_but():

        if checkbox1_var.get():
            sql=(f"""
                    update headset 
                    set status='available',serial='{serial}',name='-',agent_id='-',date='-'
                        where  lower(serial)='{serial.strip().replace(' ', '').lower()}' 
                            """)
            commit(sql=sql)

            sql=(f"""
                    insert into serial_hestory (serial,agent_name,first_date,last_date)
                    VALUES ('{ent2.get().strip().replace(' ', '')}','{ent1.get()}','{ent5.get().strip().replace(' ', '')}','-')
                            """)

            commit(sql=sql)

            sql=(f"""
                update serial_hestory 
                set last_date='{current_date}'
                    where  lower(serial)='{serial.strip().replace(' ', '').lower()}' and lower(agent_name)='{ent1.get().lower()}' 
                        """)
            commit(sql=sql)


            sql=(f"""
                update headset 
                set status='{ent1.get()}',serial='{ent2.get().strip().replace(' ', '')}',name='{ent3.get()}',agent_id='{ent4.get().strip().replace(' ', '')}',date='{ent5.get().strip().replace(' ', '')}'
                    where lower(serial) ='{ent2.get().strip().replace(' ', '').lower()}'
                        """)

            commit(sql=sql)
          

            ent1.delete(0,END)
            ent2.delete(0,END)
            ent3.delete(0,END)
            ent4.delete(0,END)
            ent5.delete(0,END)
            
            cl.refresh_data(self)

            tabs.set("Dashboard")
            tabs.configure("Dashboard")

            
        elif checkbox2_var.get():

            sql=(f"""
                    update headset 
                    set status='not available',serial='{serial}',name='-',agent_id='-',date='-'
                        where  lower(serial)='{serial.strip().replace(' ', '').lower()}' 
                            """)
            commit(sql=sql)

            sql=(f"""
                    insert into serial_hestory (serial,agent_name,first_date,last_date)
                    VALUES ('{ent2.get().strip().replace(' ', '')}','{ent1.get()}','{ent5.get().strip().replace(' ', '')}','-')
                            """)

            commit(sql=sql)

            sql=(f"""
                update serial_hestory 
                set last_date='{current_date}'
                    where  lower(serial)='{serial.strip().replace(' ', '').lower()}' and lower(agent_name)='{ent1.get().lower()}' 
                        """)

            commit(sql=sql)


            sql=(f"""
                update headset 
                set status='{ent1.get()}',serial='{ent2.get().strip().replace(' ', '')}',name='{ent3.get()}',agent_id='{ent4.get().strip().replace(' ', '')}',date='{ent5.get().strip().replace(' ', '')}'
                    where lower(serial) ='{ent2.get().strip().replace(' ', '').lower()}'
                        """)

            commit(sql=sql)
            # connection.close()
            # cursor.close()

            ent1.delete(0,END)
            ent2.delete(0,END)
            ent3.delete(0,END)
            ent4.delete(0,END)
            ent5.delete(0,END)
            
            cl.refresh_data(self)

            tabs.set("Dashboard")
            tabs.configure("Dashboard")
        else:
            label_6.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
    
    def check_but():
            
            dateText.grid_forget()
            m=ent2.get().strip().replace(' ', '').lower()
    
            new_serial=cl.headset_data[cl.headset_data['serial'].str.lower().isin([f'{m}'])]
            if ent2.get().strip().replace(" ","").lower()==serial.lower() :
                existsText = CTkLabel(frame,text='''it's a same serial ''',font=font2,text_color='red')
                existsText.grid(row=5, column=0,columnspan=2 , sticky="we", padx=12,pady=12)

            elif ent2.get()=='':
                existsText = CTkLabel(frame,text='serial field must be not empty',font=font2,text_color='red')
                existsText.grid(row=5, column=0,columnspan=2 , sticky="we", padx=12,pady=12)

            elif 'not available' in list(new_serial['status'].str.lower()):
                existsText = CTkLabel(frame,text='''this serial is not available ''',font=font2,text_color='red')
                existsText.grid(row=5, column=0,columnspan=2 , sticky="we", padx=12,pady=12)

            elif 'available' in list(new_serial['status'].str.lower()):
                if ent5.get().strip().replace(' ','')==date:
                    dateText.grid(row=5, column=0,columnspan=2 , sticky="we", padx=12,pady=12)
                else:
                    dateText.grid_forget()

                    ent1.configure(state="disabled")
                    ent2.configure(state="disabled")
                    ent3.configure(state="disabled")
                    ent4.configure(state="disabled")
                    ent5.configure(state="disabled")

                    check_serial.grid(row=5, column=0, columnspan=2, padx=10, pady=50)
                    serial_text.grid(row=0, column=0, columnspan=2, padx=10, pady=10) 

                    checkbox1.grid(row=1,column=0,padx=(40,),pady=10,sticky='w')
                    checkbox2.grid(row=1,column=1,padx=(0,40),pady=10,sticky='e')
                    button = CTkButton(master=check_serial,bg_color='transparent' ,
                                        text='Submit',command= update_but) 
                    button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
           
            elif ent2.get().strip().replace(" ","").lower() in list(new_serial['status'].str.lower()) :
                existsText = CTkLabel(frame,text='This serial already in use',font=font2,text_color='red')
                existsText.grid(row=5, column=0,columnspan=2 , sticky="we", padx=12,pady=12)
            else:
                existsText = CTkLabel(frame,text='this seria is not exists',font=font2,text_color='red')
                existsText.grid(row=5, column=0,columnspan=2 , sticky="we", padx=12,pady=12)
    
    def add_but():
       
        x=ent2.get().strip().replace(' ', '').lower()

        new_serial=cl.headset_data[cl.headset_data['serial'].str.lower().isin([f'{x}'])]
      
        if ent1.get().lower() in list(cl.headset_data['status'].str.lower()):
            existsText = CTkLabel(frame,text='This name already exists',font=font2,text_color='red')
            existsText.grid(row=5, column=0,columnspan=2 , sticky="we", padx=12,pady=12)
        elif ent1.get().strip().replace(' ','')=='' or ent2.get().strip().replace(' ','')=='' or ent3.get().strip().replace(' ','')=='' or ent4.get().strip().replace(' ','')=='' or ent5.get().strip().replace(' ','')=='' :
             existsText = CTkLabel(frame,text='all fields must be not empty',font=font2,text_color='red')
             existsText.grid(row=5, column=0,columnspan=2 , sticky="we", padx=12,pady=12)     
        elif  'available' in list(new_serial['status'].str.lower()) :
                
                sql=(f"""
                    update headset 
                    set status='{ent1.get()}',serial='{ent2.get().strip().replace(' ', '')}',name='{ent3.get()}',agent_id='{ent4.get().strip().replace(' ', '')}',date='{ent5.get().strip().replace(' ', '')}'
                        where lower(serial) ='{ent2.get().strip().replace(' ', '').lower()}'
                            """)

                commit(sql=sql)
                # connection.close()
                # cursor.close()
                sql=(f"""
                    insert into serial_hestory (serial,agent_name,first_date,last_date)
                    VALUES ('{ent2.get().strip().replace(' ', '')}','{ent1.get()}','{ent5.get().strip().replace(' ', '')}','-')
                            """)

                commit(sql=sql)

                ent1.delete(0,END)
                ent2.delete(0,END)
                ent3.delete(0,END)
                ent4.delete(0,END)
                ent5.delete(0,END)
                
                cl.refresh_data(self)

                tabs.set("Dashboard")
                tabs.configure("Dashboard")
        elif  'not available' in list(new_serial['status'].str.lower()) : 
            existsText = CTkLabel(frame,text='this serial not available',font=font2,text_color='red')
            existsText.grid(row=5, column=0,columnspan=2 , sticky="we", padx=12,pady=12)
        elif  not('not available' in list(new_serial['status'].str.lower())) and not('available' in list(new_serial['status'].str.lower())) and ent2.get().strip().replace(' ','').lower() in list(cl.headset_data['serial'].str.lower()) : 
            existsText = CTkLabel(frame,text='this serial is already exists',font=font2,text_color='red')
            existsText.grid(row=5, column=0,columnspan=2 , sticky="we", padx=12,pady=12)
        elif  not(ent2.get().strip().replace(' ','').lower() in list(cl.headset_data['status'].str.lower())) :

            existsText = CTkLabel(frame,text='this serial not exists',font=font2,text_color='red')
            existsText.grid(row=5, column=0,columnspan=2 , sticky="we", padx=12,pady=12)
        else:

            existsText = CTkLabel(frame,text='this serial not exists or not available',font=font2,text_color='red')
            existsText.grid(row=5, column=0,columnspan=2 , sticky="we", padx=12,pady=12)
       
    def delete_but():
        ent1.configure(state="disabled")
        ent2.configure(state="disabled")
        ent3.configure(state="disabled")
        ent4.configure(state="disabled")
        ent5.configure(state="disabled")

        check_serial.grid(row=5, column=0, columnspan=2, padx=10, pady=50)
        serial_text.grid(row=0, column=0, columnspan=2, padx=10, pady=10) 

        checkbox1.grid(row=1,column=0,padx=(40,),pady=10,sticky='w')
        checkbox2.grid(row=1,column=1,padx=(0,40),pady=10,sticky='e')
        button = CTkButton(master=check_serial,fg_color='transparent',border_color='#2986CC',border_width=1,
                            text='Submit',command= delete_state) 
        button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        
       
    frame = CTkFrame(master=app)
    frame.pack(pady=40, padx=100, fill="both", expand=True)
    frame.columnconfigure((0, 1), weight=1)
  
    lab1 = CTkLabel(master=frame, text="Update headset status", font=font_1)
    lab1.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="we")
    if american_name=='':
        ent1 = CTkEntry(master=frame,placeholder_text='American name')
        ent1.grid(row=1, column=0, padx=10, pady=10, sticky="we")
       
        ent2 = CTkEntry(master=frame,placeholder_text='Serial')
        ent2.grid(row=1, column=1, padx=10, pady=10, sticky="we")

        ent3 = CTkEntry(master=frame,placeholder_text='Name')
        ent3.grid(row=2, column=0, padx=10, pady=10, sticky="we")

        ent4 = CTkEntry(master=frame,placeholder_text='ID')
        ent4.grid(row=2, column=1, padx=10, pady=10, sticky="we")

        ent5 = CTkEntry(master=frame,placeholder_text='Date')
        ent5.grid(row=3, column=0, padx=10, pady=10, sticky="we")


        update_button = CTkButton(frame,text='add!',fg_color='transparent',border_color='#2986CC',border_width=1,font=font2,command=add_but)
        update_button.grid(row=4, column=0, sticky="ws", padx=12,pady=12)

        print(ent1.get())
    else:
        ent1 = CTkEntry(master=frame,textvariable=american_n,)
        ent1.grid(row=1, column=0, padx=10, pady=10, sticky="we")

        ent2 = CTkEntry(master=frame,textvariable=ser)
        ent2.grid(row=1, column=1, padx=10, pady=10, sticky="we")
        
        ent3 = CTkEntry(master=frame,textvariable=na)
        ent3.grid(row=2, column=0, padx=10, pady=10, sticky="we")

        
        ent4 = CTkEntry(master=frame,textvariable=agent_id)
        ent4.grid(row=2, column=1, padx=10, pady=10, sticky="we")

        ent5 = CTkEntry(master=frame,textvariable=da)
        ent5.grid(row=3, column=0, padx=10, pady=10, sticky="we")

        dateText = CTkLabel(frame,text='''You msut to replace the date  ''',font=font2,text_color='red')

        back_button = CTkButton(frame,text='Delete',fg_color='transparent',border_color='#2986CC',border_width=1,font=font2,command=delete_but)

        back_button.grid(row=4, column=1, sticky="es", padx=12,pady=12)
        add_button = CTkButton(frame,text='Update!',fg_color='transparent',border_color='#2986CC',border_width=1,font=font2,command=check_but)
        add_button.grid(row=4, column=0, sticky="ws", padx=12,pady=12)
    check_serial = CTkFrame(master=frame)
    serial_text=CTkLabel(master=check_serial,text="Old serial",font=font2)
    label_6= CTkLabel(master=check_serial,text='Add status',text_color='red')
    checkbox1 =CTkCheckBox(master=check_serial, text="Available",corner_radius=40, variable=checkbox1_var, command=toggle_checkbox1)
    checkbox2 = CTkCheckBox(master=check_serial, text="Not Available",corner_radius=40, variable=checkbox2_var, command=toggle_checkbox2)
    

    print(ent1.get().lower())
    return frame
