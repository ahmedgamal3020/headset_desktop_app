from tkinter import StringVar
from customtkinter import *
import datetime 
import  dashboard 
from urllib.parse import quote_plus
import pandas as pd
from sqlalchemy.engine import create_engine
from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%Y/%m/%d")
   

def details_about(self,app,tabs ,frame="",american_name='',serial='',name='',id='',date='',headset_type=''):
    if frame == "":
        pass
    else:
        frame.pack_forget()
    print(dt_string)
    cl= dashboard.Dashboard
    connection=cl.connection
    cursor=cl.cursor
    
    american_n = StringVar()
    american_n.set(american_name)
    ser = StringVar()
    ser.set(serial)
    na = StringVar()
    na.set(name)
    agent_id = StringVar()
    agent_id.set(id)
    da = StringVar()
    da.set(date)
    type = StringVar()
    type.set(headset_type)
    font_1 = CTkFont(family="arial", weight="bold", size=40)
    font2 = CTkFont(family="arial", size=30)
    current_date =dt_string
    cl.headset_data=pd.read_sql(''' select * from headset

                               ''',cl.engine)
    def update_but():
            cl.headset_data=cl.headset_data
            print(serial)
            m=ent2.get().strip().replace(' ', '').lower()
            print(f'{m}') 
            
            new_serial=cl.headset_data[cl.headset_data['serial'].str.lower().isin([f'{m}'])]
            print(new_serial)
            if ent2.get()==serial or not('availble' in list(new_serial['status'].str.lower())) :
                existsText = CTkLabel(frame,text='this serial is already in use or not exists',font=font2,text_color='red')
                existsText.grid(row=5, column=0,columnspan=2 , sticky="we", padx=12,pady=12)
            elif ent2.get()=='':
                existsText = CTkLabel(frame,text='serial field must be not empty',font=font2,text_color='red')
                existsText.grid(row=5, column=0,columnspan=2 , sticky="we", padx=12,pady=12)
            else:
                sql=(f"""
                    update headset 
                    set status='availble',serial='{serial}',name='-',agent_id='-',date='-',headset_type='{ent6.get().replace(' ', '')}'
                        where  lower(serial)='{serial.strip().replace(' ', '').lower()}' 
                            """)
                connection.commit()
                cursor.execute(query=sql)
                cursor.execute('commit')

                sql=(f"""
                        insert into serial_hestory (serial,agent_name,first_date,last_date)
                        VALUES ('{ent2.get().strip().replace(' ', '')}','{ent1.get()}','{ent5.get().strip().replace(' ', '')}','-')
                                """)

                connection.commit()
                cursor.execute(query=sql)
                cursor.execute('commit')

                sql=(f"""
                    update serial_hestory 
                    set last_date='{current_date}'
                        where  lower(serial)='{serial.strip().replace(' ', '').lower()}' and lower(agent_name)='{ent1.get().lower()}' 
                            """)

                connection.commit()
                cursor.execute(query=sql)
                cursor.execute('commit')


                sql=(f"""
                    update headset 
                    set status='{ent1.get()}',serial='{ent2.get().strip().replace(' ', '')}',name='{ent3.get()}',agent_id='{ent4.get().strip().replace(' ', '')}',date='{ent5.get().strip().replace(' ', '')}',headset_type='{ent6.get().strip().replace(' ', '')}'
                        where lower(serial) ='{ent2.get().strip().replace(' ', '').lower()}'
                            """)

                connection.commit()
                cursor.execute(query=sql)
                cursor.execute('commit')
                # connection.close()
                # cursor.close()

                ent1.delete(0,END)
                ent2.delete(0,END)
                ent3.delete(0,END)
                ent4.delete(0,END)
                ent5.delete(0,END)
                ent6.delete(0,END)
                
                cl.refresh_data(self)

                tabs.set("Dashboard")
                tabs.configure("Dashboard")
       
    def add_but():
       
        x=ent2.get().strip().replace(' ', '').lower()

        new_serial=cl.headset_data[cl.headset_data['serial'].str.lower().isin([f'{x}'])]
        print(new_serial)
        if ent1.get().lower() in list(cl.headset_data['status'].str.lower()):
            existsText = CTkLabel(frame,text='This name already exists',font=font2,text_color='red')
            existsText.grid(row=5, column=0,columnspan=2 , sticky="we", padx=12,pady=12)
        elif ent1.get().strip().replace(' ','')=='' or ent2.get().strip().replace(' ','')=='' or ent3.get().strip().replace(' ','')=='' or ent4.get().strip().replace(' ','')=='' or ent5.get().strip().replace(' ','')=='' or ent6.get().strip().replace(' ','')=='':
             existsText = CTkLabel(frame,text='all fields must be not empty',font=font2,text_color='red')
             existsText.grid(row=5, column=0,columnspan=2 , sticky="we", padx=12,pady=12)
            
        elif  'availble' in list(new_serial['status'].str.lower()) :
                
                sql=(f"""
                    update headset 
                    set status='{ent1.get()}',serial='{ent2.get().strip().replace(' ', '')}',name='{ent3.get()}',agent_id='{ent4.get().strip().replace(' ', '')}',date='{ent5.get().strip().replace(' ', '')}',headset_type='{ent6.get().strip().replace(' ', '')}'
                        where lower(serial) ='{ent2.get().strip().replace(' ', '').lower()}'
                            """)

                connection.commit()
                cursor.execute(query=sql)
                cursor.execute('commit')
                # connection.close()
                # cursor.close()
                sql=(f"""
                    insert into serial_hestory (serial,agent_name,first_date,last_date)
                    VALUES ('{ent2.get().strip().replace(' ', '')}','{ent1.get()}','{ent5.get().strip().replace(' ', '')}','-')
                            """)

                connection.commit()
                cursor.execute(query=sql)
                cursor.execute('commit')

                ent1.delete(0,END)
                ent2.delete(0,END)
                ent3.delete(0,END)
                ent4.delete(0,END)
                ent5.delete(0,END)
                ent6.delete(0,END)
                
                cl.refresh_data(self)

                tabs.set("Dashboard")
                tabs.configure("Dashboard")
        elif  'not availble' in list(new_serial['status'].str.lower()) : 
            existsText = CTkLabel(frame,text='this serial not availble',font=font2,text_color='red')
            existsText.grid(row=5, column=0,columnspan=2 , sticky="we", padx=12,pady=12)
        elif  not('not availble' in list(new_serial['status'].str.lower())) and not('availble' in list(new_serial['status'].str.lower())) and ent2.get().strip().replace(' ','').lower() in list(cl.headset_data['serial'].str.lower()) : 
            existsText = CTkLabel(frame,text='this serial is already exists',font=font2,text_color='red')
            existsText.grid(row=5, column=0,columnspan=2 , sticky="we", padx=12,pady=12)
        elif  not(ent2.get().strip().replace(' ','').lower() in list(cl.headset_data['status'].str.lower())) :

            existsText = CTkLabel(frame,text='this serial not exists',font=font2,text_color='red')
            existsText.grid(row=5, column=0,columnspan=2 , sticky="we", padx=12,pady=12)
        else:

            existsText = CTkLabel(frame,text='this serial not exists or not availble',font=font2,text_color='red')
            existsText.grid(row=5, column=0,columnspan=2 , sticky="we", padx=12,pady=12)


            # sql=(f"""
            #     insert into headset (status,serial,name,agent_id,date,headset_type)
            #     VALUES ('{ent1.get()}','{ent2.get().strip().replace(' ', '')}','{ent3.get()}','{ent4.get().strip().replace(' ', '')}','{ent5.get().strip().replace(' ', '')}','{ent6.get().strip().replace(' ', '')}')
                       
            #                 """)

            # cursor.execute(query=sql)
            # cursor.execute('commit')

            # sql=(f"""
            #         insert into serial_hestory (serial,agent_name,first_date,last_date)
            #         VALUES ('{ent2.get().strip().replace(' ', '')}','{ent1.get()}','{ent5.get().strip().replace(' ', '')}','-')
            #                 """)

            # connection.commit()
            # cursor.execute(query=sql)
            # cursor.execute('commit')

           
            
        # else:
        #     existsText = CTkLabel(frame,text='This serial is not exist',font=font2,text_color='red')
        #     existsText.grid(row=5, column=0,columnspan=2 , sticky="we", padx=12,pady=12)
 
       
    def delete_but():
    
        sql=(f"""
                 update headset 
                    set status='availble',serial='{ent2.get().strip().replace(' ', '')}',name='-',agent_id='-',date='-',headset_type='{ent6.get().strip().replace(' ', '')}'
                        where  lower(serial)='{ent2.get().strip().replace(' ','').lower()}' 
                            """)

        connection.commit()
        cursor.execute(query=sql)
        cursor.execute('commit')

        tabs.update()
        
        sql=(f"""
                update serial_hestory 
                    set last_date='{current_date}'
                        where  lower(serial)='{ent2.get().strip().replace(' ','').lower()}' and lower(agent_name)='{ent1.get().lower()}' 
                            """)

        connection.commit()
        cursor.execute(query=sql)
        cursor.execute('commit')

        ent1.delete(0,END)
        ent2.delete(0,END)
        ent3.delete(0,END)
        ent4.delete(0,END)
        ent5.delete(0,END)
        ent6.delete(0,END)
        ent1.clipboard_clear()

        cl.refresh_data(self)

        tabs.set("Dashboard")


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

        ent6 = CTkEntry(master=frame,placeholder_text='Headset name')
        ent6.grid(row=3, column=1, padx=10, pady=10, sticky="we")

        update_button = CTkButton(frame,text='add!',font=font_1,command=add_but)
        update_button.grid(row=4, column=0, sticky="ws", padx=12,pady=12)

        print(ent1.get())
    else:
        ent1 = CTkEntry(master=frame,textvariable=american_n)
        ent1.grid(row=1, column=0, padx=10, pady=10, sticky="we")

        ent2 = CTkEntry(master=frame,textvariable=ser)
        ent2.grid(row=1, column=1, padx=10, pady=10, sticky="we")
        
        ent3 = CTkEntry(master=frame,textvariable=na)
        ent3.grid(row=2, column=0, padx=10, pady=10, sticky="we")

        
        ent4 = CTkEntry(master=frame,textvariable=agent_id)
        ent4.grid(row=2, column=1, padx=10, pady=10, sticky="we")

        ent5 = CTkEntry(master=frame,textvariable=da)
        ent5.grid(row=3, column=0, padx=10, pady=10, sticky="we")

        ent6 = CTkEntry(master=frame,textvariable=type)
        ent6.grid(row=3, column=1, padx=10, pady=10, sticky="we")
        back_button = CTkButton(frame,text='Delete',font=font_1,command=delete_but)

        back_button.grid(row=4, column=1, sticky="es", padx=12,pady=12)
        add_button = CTkButton(frame,text='Update!',font=font_1,command=update_but)
        add_button.grid(row=4, column=0, sticky="ws", padx=12,pady=12)

        print(ent1.get().lower())
    return frame
