from customtkinter import *
import tkinter as tk
import dashboard
import pandas as pd


def getmeframe(self,app,tabs ,parent_hight, parent_width,data, frame="", ):
    if(frame == ""):
        pass
    else:
        frame.pack_forget()
    cl=dashboard.Dashboard
    connection=cl.connection
    cursor=cl.cursor
    serial_history=pd.read_sql(''' select * from serial_hestory
                               ''',cl.engine)
    serial_history['serial']=serial_history['serial'].str.upper()
    data['serial']=data['serial'].str.upper()
    serialData=data['serial'].unique()
    serialData=list(serialData)
    serialData.append('Available')
    serialData.append('Not Available')

    font_1 = CTkFont(family="arial", weight="bold", size=40)
    font2 = CTkFont(family="arial", size=30)
    font3 = CTkFont(family="arial", size=10)

    def delete_serial(serial):
        serial_data=data[data['serial'].isin([serial])]
        print(serial_data)
        
        sql=(f"""
            delete from  headset 
              where lower(serial)='{serial.lower()}'
               
                        """)

        connection.commit()
        cursor.execute(query=sql)
        cursor.execute('commit')

        

        if 'available'in list(serial_data['status'].str.lower()):
                cl.refresh_data(self)
                serial=data[data['status'].isin(['Available'])]
                serial.reset_index(inplace=True,level=False)
               
                serial_status(serial)

        elif 'not available'in list(serial_data['status'].str.lower()): 
                cl.refresh_data(self)
                serial=data[data['status'].isin(['Not Available'])]
                serial.reset_index(inplace=True,level=False)
                
                serial_status(serial)

    
        #     delete serial_hestory 
        #       where lower(serial)='{serial.lower()}'
        #                 """)

        # connection.commit()
        # cursor.execute(query=sql)
        # cursor.execute('commit')


    def serial_status(serial):
            print(serial)
            date_frame=CTkScrollableFrame(master=frame,fg_color='transparent') 
            date_frame.grid_columnconfigure((0),weight=1)
            date_frame.grid_rowconfigure((0),weight=1)
            date_frame.grid(row=3, column=1,rowspan=5,sticky='wens',pady=10,padx=(0,10)) 
            
            serial_count=list(serial['serial'])       
            for i in range(len(serial_count)):

                frame_child5 = CTkFrame(master=date_frame,fg_color='#2B2B2B')
                frame_child5.grid(
                row=i, column=0, sticky="we", pady=(0, 10))
                frame_child5.grid_columnconfigure((0,1),weight=1)
                frame_child5.grid_rowconfigure((0,1),weight=1)
                serial_name=serial['serial'][i]

                agent_name=CTkLabel(frame_child5,text=f'{serial_name}',font=font_1)    
                agent_name.grid(row=0,column=0,sticky='w',padx=(10,0),pady=10) 

                delete_but=CTkButton(frame_child5,text='X',fg_color='transparent',hover_color='red',font=font_1,command=lambda: delete_serial(serial_name))  
                delete_but.grid(row=0,column=1,sticky='e',padx=(10),pady=10) 

    def serial_filter_list(event=""):
        
        search_text = label_1.get().lower()
        filtered_list = [item for item in serialData if search_text in item.lower()]
        listbox2.delete(0, tk.END)
        for item in filtered_list:
            listbox2.insert(tk.END, item) 
        if len(filtered_list)==len(serialData):
            listbox2.config(height=20)
            serial_empty_label()
        elif len(filtered_list)<=19:
            listbox2.config(height=listbox2.size())
            
        elif len(filtered_list)>20:
            listbox2.config(height=19)
            
        elif len(filtered_list)==0:
            listbox2.config(height=0)
   
    def serial_sub_frame(status):
            
            agent=list(status['agent_name'])
            u_serial=''.join(status['serial'])
            
            date_frame=CTkScrollableFrame(master=frame,fg_color='transparent') 
            date_frame.grid_columnconfigure((0),weight=1)
            date_frame.grid_rowconfigure((0),weight=1)
            date_frame.grid(row=3, column=1,rowspan=5,sticky='wens',pady=10,padx=(0,10)) 
            if len(agent)>=1:
                st=data[data['serial'].isin([u_serial])]
                st=''.join(st['status'])
                for i in range(len(agent)) :   
                   
                    frame_child5 = CTkFrame(master=date_frame,fg_color='#2B2B2B')
                    frame_child5.grid(
                    row=i, column=0, sticky="we", pady=(0, 10))
                    frame_child5.grid_columnconfigure((0,1),weight=1)
                    frame_child5.grid_rowconfigure((0,1),weight=1)
                    name=status['agent_name'][i]
                    first_date=status['first_date'][i]
                    last_date=status['last_date'][i]
                    if last_date=='-':
                        stat='Working'
                        color='grey'
                    else:
                        stat=st
                        if stat.lower()=='available':
                            color='green'
                        else:
                            color='red'


                    agent_name=CTkLabel(frame_child5,text=f'{name.title()}',font=font_1)    
                    agent_name.grid(row=i,column=0,sticky='wn',padx=(10,0),pady=10) 

                    serial_status=CTkLabel(frame_child5,text=f'{stat.title()}',text_color=color,font=font3)    
                    serial_status.grid(row=i,column=1,sticky='e',padx=(10),pady=10) 

                    start_date=CTkLabel(frame_child5,text=f'{first_date}',font=font2)    
                    start_date.grid(row=i+1,column=0,sticky='w',padx=(80,0),pady=10)  

                    end_date=CTkLabel(frame_child5,text=f'{last_date}',font=font2)    
                    end_date.grid(row=i+1,column=1,sticky='e',padx=(0,80),pady=10) 
            else:
                frame_child5 = CTkLabel(master=date_frame,text='This series has no status',text_color='red')
                frame_child5.grid(
                    row=0, column=0, sticky="we", pady=(0, 10))

    def serial_empty_label():
         date_frame=CTkFrame(master=frame,fg_color='transparent') 
         date_frame.grid_columnconfigure((0),weight=1)
         date_frame.grid_rowconfigure((0,1,2,3,4),weight=1)
         date_frame.grid(row=3, column=1,rowspan=5,sticky='wens',pady=10,padx=(0,10)) 
         
    def serial_on_selects(event=""):
        serial_empty_label
        selected_index2 = listbox2.curselection()
    
        if selected_index2:
            selected_item2 = listbox2.get(selected_index2[0])
            if selected_item2=='Available':

                serial=data[data['status'].isin(['Available'])]
                serial.reset_index(inplace=True,level=False)
                serial_status(serial)

            elif selected_item2=='Not Available': 
                serial=data[data['status'].isin(['Not Available'])]
                serial.reset_index(inplace=True,level=False)
                serial_status(serial)

            else:
                status=serial_history[serial_history['serial'].isin([f'{selected_item2}'])]
                status.reset_index(inplace=True,level=False)
                serial_sub_frame(status=status)
                
        else:
              print('falsess')
  
    def serial_press_enter(event):
        serial_empty_label
        search_text = label_1.get().lower()
        listbox_item=listbox2.get(0).lower()
        if search_text ==listbox_item :
            status=serial_history[serial_history['serial'].isin([f'{search_text.upper()}'])]
            status.reset_index(inplace=True,level=False)
          
            serial_sub_frame(status=status)
        else:
            print('ahmedssss')
    
    def serial_toggle_checkbox1(*args):
        if checkbox1_var.get():
            label_6.grid_forget()
            existsText.grid_forget()
            emptyText.grid_forget()
            successText.grid_forget()
            button.grid(row=4,column=0,columnspan=2,padx=50,pady=10,sticky='wen')
            checkbox2_var.set(False)
    
    def serial_toggle_checkbox2(*args):

        search_text = label_4.get().lower()
      
        if checkbox2_var.get():
            label_6.grid_forget()
            existsText.grid_forget()
            emptyText.grid_forget()
            successText.grid_forget()
            button.grid(row=4,column=0,columnspan=2,padx=50,pady=10,sticky='wen')
            checkbox1_var.set(False)
    
    def serial_but():
        if entry_var.get().strip().replace(' ','')!='' and entry_var2.get().strip().replace(' ','')!='':
            
            if checkbox1_var.get():
                if entry_var.get().strip().replace(' ','').lower() in list(data['serial'].str.lower()):
                    existsText.grid(row=5, column=0,columnspan=4, sticky="we", padx=10,pady=3)
                    button.grid_forget()
                else:
                    sql=(f"""
                        insert into headset (status,serial,name,agent_id,date,headset_type)
                        VALUES ('available','{entry_var.get().strip().replace(' ', '')}','-','-','-','{entry_var2.get().strip().replace(' ', '')}')
                            
                                    """)

                    connection.commit()
                    cursor.execute(query=sql)
                    cursor.execute('commit')
                    label_6.grid_forget()
                    successText.grid(row=5,column=0,columnspan=4,padx=10,pady=3,sticky='we')
                    button.grid_forget()
                    cl.refresh_data(self)
            elif checkbox2_var.get():
                
                if entry_var.get().strip().replace(' ','').lower() in list(data['serial'].str.lower()):
                    existsText.grid(row=5, column=0,columnspan=4, sticky="we", padx=6,pady=3)
                    button.grid_forget()
                else:
                    
                    sql=(f"""
                        insert into headset (status,serial,name,agent_id,date,headset_type)
                        VALUES ('not available','{entry_var.get().strip().replace(' ', '')}','-','-','-','{entry_var2.get().strip().replace(' ', '')}')
                            
                                    """)


                    connection.commit()
                    cursor.execute(query=sql)
                    cursor.execute('commit')
                    label_6.grid_forget()
                    successText.grid(row=5,column=0,columnspan=4,padx=3,pady=3,sticky='we')
                    button.grid_forget()
                    cl.refresh_data(self)
                    
            else:
                emptyText.grid_forget()
                label_6.grid(row=5,column=0,columnspan=4,padx=3,pady=3,sticky='we')
                button.grid_forget()
        else:
           
            emptyText.grid(row=5,column=0,columnspan=4,padx=3,pady=3,sticky='we')
            button.grid_forget()

    def check_serial(event):
        search_text = label_4.get().lower()
        if not(search_text  is None):
             label_6.grid_forget()
             existsText.grid_forget()
             emptyText.grid_forget()
             successText.grid_forget()
             button.grid(row=4,column=0,columnspan=2,padx=50,pady=10,sticky='wen')
             
        
        

    checkbox1_var = tk.BooleanVar()
    checkbox2_var = tk.BooleanVar()
    entry_var=tk.StringVar()
    entry_var2=tk.StringVar()
    entry_var2.set('plantrasonic')
    print(entry_var2)
    frame = CTkFrame(master=app) 
    frame.pack(pady=20,padx=10,fill='both',expand=True) 
    frame.columnconfigure((1),weight=3)
    frame.columnconfigure((0),weight=1)
    frame.rowconfigure((3,4),weight=6)
    # frame.grid_rowconfigure(,weight=3)

    ################# add now srial #####################
    sub_frame=CTkFrame(master=frame,border_color='#26619c',border_width=5)
    sub_frame.grid(row=0,column=0,columnspan=4,padx=300,pady=(0,5),sticky='wen')
    sub_frame.columnconfigure((0,1),weight=1)

    label_3= CTkLabel(master=sub_frame,text='Add New Serial',corner_radius=0,font=font_1)
    label_3.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

    lab1 = CTkLabel(master=sub_frame,text='serial',font=CTkFont(size=10) ,corner_radius=0,) 
    lab1.grid(row=1,column=0,padx=10,sticky='w')
    lab2 = CTkLabel(master=sub_frame,text='headset type',font=CTkFont(size=10), corner_radius=0) 
    lab2.grid(row=1,column=1,padx=10,sticky='w')

    label_4 = CTkEntry(master=sub_frame,placeholder_text='Serial',textvariable= entry_var, corner_radius=0) 
    label_4.grid(row=2,column=0,padx=10,pady=(0,10),sticky='we')
    label_4.bind("<KeyRelease>", check_serial)

    label_5 = CTkEntry(master=sub_frame,placeholder_text='headset type',textvariable= entry_var2, corner_radius=0) 
    label_5.grid(row=2,column=1,padx=10,pady=(0,10),sticky='we')


    checkbox1 =CTkCheckBox(master=sub_frame, text="Available",corner_radius=50, variable=checkbox1_var, command=serial_toggle_checkbox1)
    checkbox2 = CTkCheckBox(master=sub_frame, text="Not Available",corner_radius=50, variable=checkbox2_var, command=serial_toggle_checkbox2)

    checkbox1.grid(row=3,column=0,padx=(0,20),pady=10,sticky='e')
    checkbox2.grid(row=3,column=1,padx=(20,0),pady=10,sticky='w')
    button = CTkButton(master=sub_frame, 
                        text='add',command= serial_but) 
    button.grid(row=4,column=0,columnspan=2,padx=50,pady=10,sticky='wen')

    label_6= CTkLabel(master=sub_frame,text='add status ',text_color='red')
    existsText = CTkLabel(sub_frame,text='this serial is already exists',text_color='red')
    successText= CTkLabel(sub_frame,text='Successfully',text_color='green')
    emptyText = CTkLabel(sub_frame,text='the field is empty ',text_color='red')
###########################################################################################################################################################################

    line=CTkFrame(master=frame,fg_color='#26619c',height=3)
    line.grid(row=1,column=0,columnspan=4,padx=10,pady=10,sticky='wens')


    # ############################################################################# search corner #################################################################
    search_corner=CTkFrame(master=frame)
    search_corner.grid(row=2,column=0,rowspan=4, padx=10,pady=(0,5),sticky='wens')
    search_corner.columnconfigure((0,1),weight=1)
    label_0= CTkLabel(master=search_corner,text='Serial',font=font_1)
    label_0.grid(row=0,column=0,columnspan=2,padx=(0),pady=5,sticky='wens')
    # width=parent_width*.25)
    label_1 = CTkEntry(master=search_corner,) 
    label_1.grid(row=1,column=0,columnspan=2,padx=(0,5),pady=10,sticky='wens')
    label_1.bind("<KeyRelease>", serial_filter_list)
    label_1.bind("<Return>", serial_press_enter)
    listbox2 = tk.Listbox(search_corner,bg='#333333',fg='#ffffff')
    listbox2.config(height=20)
    for item in serialData:
        listbox2.insert(tk.END, item)
    listbox2.grid(row=2,column=0,columnspan=2,rowspan=4,padx=10,pady=(0,10),sticky='wens',)
    listbox2.bind("<<ListboxSelect>>", serial_on_selects)

    label_2= CTkLabel(master=frame,text='status',corner_radius=0,width=parent_width*.25,font=font_1)
    label_2.grid(row=2,column=1,padx=10,pady=0,sticky='wen')
   
   
    
    
    

    
    return frame





