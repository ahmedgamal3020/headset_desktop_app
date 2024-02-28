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
    serial_hestory=pd.read_sql(''' select * from serial_hestory

                               ''',cl.engine)
    serial_hestory['serial']=serial_hestory['serial'].str.upper()
    data['serial']=data['serial'].str.upper()
    serialData=data['serial'].unique()

    font2 = CTkFont(family="arial", size=30)
    font_1 = CTkFont(family="arial", weight="bold", size=40)

    def filter_list(event):
        
        search_text = label_1.get().lower()
        filtered_list = [item for item in serialData if search_text in item.lower()]
        listbox.delete(0, tk.END)
        for item in filtered_list:
            listbox.insert(tk.END, item) 
        if len(filtered_list)==len(serialData):
            listbox.config(height=10)
            print('y')
            empty_label()
        elif len(filtered_list)<=35:
            listbox.config(height=listbox.size())
            
        elif len(filtered_list)>35:
            listbox.config(height=35)
            
        elif len(filtered_list)==0:
            listbox.config(height=0)

   
            # editing.details_about(app,parent_hight,parent_width,frame,selected_item)
    
    def sun_frame(status): 
            
            agent=list(status['agent_name'])
            print(agent)
            date_frame=CTkScrollableFrame(master=frame,fg_color='transparent') 
            date_frame.grid_columnconfigure((0),weight=1)
            date_frame.grid_rowconfigure((0),weight=1)
            date_frame.grid(row=1, column=1,rowspan=5,sticky='wens',pady=10,padx=(0,10)) 
            if len(agent)>=1:
                for i in range(len(agent)) :   
                    print(len(agent))
                    frame_child5 = CTkFrame(master=date_frame,fg_color='#2B2B2B')
                    frame_child5.grid(
                    row=i, column=0, sticky="we", pady=(0, 10))
                    frame_child5.grid_columnconfigure((0,1),weight=1)
                    frame_child5.grid_rowconfigure((0,1),weight=1)
                    name=status['agent_name'][i]
                    first_date=status['first_date'][i]
                    last_date=status['last_date'][i]

                    agent_name=CTkLabel(frame_child5,text=f'{name.title()}',font=font_1)    
                    agent_name.grid(row=i,column=0,sticky='wn',padx=(10,0),pady=10) 
                    start_date=CTkLabel(frame_child5,text=f'{first_date}',font=font2)    
                    start_date.grid(row=i+1,column=0,sticky='w',padx=(80,0),pady=10)  
                    end_date=CTkLabel(frame_child5,text=f'{last_date}',font=font2)    
                    end_date.grid(row=i+1,column=1,sticky='e',padx=(0,80),pady=10) 
            else:
                frame_child5 = CTkLabel(master=date_frame,text='This series has no status',text_color='red')
                frame_child5.grid(
                    row=0, column=0, sticky="we", pady=(0, 10))

    def empty_label():
         date_frame=CTkFrame(master=frame,fg_color='transparent') 
         date_frame.grid_columnconfigure((0),weight=1)
         date_frame.grid_rowconfigure((0,1,2,3,4),weight=1)
         date_frame.grid(row=0, column=1,rowspan=5,sticky='wens',pady=10,padx=(0,10)) 
         
    def on_select(event):
        selected_index = listbox.curselection()
        if selected_index:
            selected_item = listbox.get(selected_index[0])
            status=serial_hestory[serial_hestory['serial'].isin([f'{selected_item}'])]
            status.reset_index(inplace=True,level=False)
            print(status)
            sun_frame(status=status)
        else:
            pass  
  
    def press_enter(event):
        search_text = label_1.get().lower()
        listbox_item=listbox.get(0).lower()
        if search_text ==listbox_item :
            status=serial_hestory[serial_hestory['serial'].isin([f'{search_text.upper()}'])]
            status.reset_index(inplace=True,level=False)
            print(status)
            sun_frame(status=status)
                      # editing.details_about(app,parent_hight,parent_width,frame,search_text)
        else:
            print('ahmedssss')
    def toggle_checkbox1(*args):
        if checkbox1_var.get():
            checkbox2_var.set(False)

    def toggle_checkbox2(*args):
        if checkbox2_var.get():
            checkbox1_var.set(False)
    def but():
       if entry_var.get()!=None:
            if checkbox1_var.get():
                if entry_var.get().strip().replace(' ','').lower() in list(data['serial']):
                    existsText.grid(row=5, column=0, sticky="wen", padx=10,pady=10)
                else:
                    sql=(f"""
                        insert into headset (status,serial,name,agent_id,date,headset_type)
                        VALUES ('availble','{entry_var.get().strip().replace(' ', '')}','-','-','-','Plantrasonic')
                            
                                    """)

                    connection.commit()
                    cursor.execute(query=sql)
                    cursor.execute('commit')
                    label_6.grid_forget()
                    cl.refresh_data(self)
            elif checkbox2_var.get():
                if entry_var.get().strip().replace(' ','').lower() in list(data['serial']):
                    existsText.grid(row=5, column=0, sticky="wen", padx=10,pady=10)
                else:
                    sql=(f"""
                        insert into headset (status,serial,name,agent_id,date,headset_type)
                        VALUES ('not availble','{entry_var.get().strip().replace(' ', '')}','-','-','-','Plantrasonic')
                            
                                    """)


                    connection.commit()
                    cursor.execute(query=sql)
                    cursor.execute('commit')
                    label_6.grid_forget()
                    cl.refresh_data(self)
            else:
               
                label_6.grid(row=5,column=0,padx=10,pady=10,sticky='wen')
      
        
    checkbox1_var = tk.BooleanVar()
    checkbox2_var = tk.BooleanVar()
    entry_var=tk.StringVar()
    entry_var2=tk.StringVar()
    frame = CTkFrame(master=app) 
    frame.pack(pady=20,padx=10,fill='both',expand=True) 
    frame.columnconfigure((1),weight=3)
    frame.rowconfigure((2),weight=1)
    # frame.grid_rowconfigure(,weight=3)

    # Set the label inside the frame 
    label_0= CTkLabel(master=frame,text='Serial',corner_radius=0,width=parent_width*.25,font=font_1)
    label_0.grid(row=0,column=0,padx=10,pady=10,sticky='wen')
    label_2= CTkLabel(master=frame,text='status',corner_radius=0,width=parent_width*.25,font=font_1)
    label_2.grid(row=0,column=1,padx=10,pady=10,sticky='wen')

    label_1 = CTkEntry(master=frame,corner_radius=0,width=parent_width*.25) 
    label_1.grid(row=1,column=0,padx=10,pady=10,sticky='wen')
    label_1.bind("<KeyRelease>", filter_list)
    label_1.bind("<Return>", press_enter)
    listbox = tk.Listbox(frame,bg='#333333',fg='#ffffff')
    for item in serialData:
        listbox.insert(tk.END, item)
    listbox.grid(row=2,column=0,padx=10,pady=(0,10),sticky='wen',)
    listbox.bind("<<ListboxSelect>>", on_select)

    sub_frame=CTkFrame(master=frame,fg_color='transparent')
    sub_frame.grid(row=3,column=0,padx=10,pady=10,sticky='wen')
    sub_frame.columnconfigure((0,1,2,3),weight=1)

    label_3= CTkLabel(master=sub_frame,text='Add New Serial',corner_radius=0,font=font_1)
    label_3.grid(row=0,column=0,columnspan=2,padx=10,pady=10,sticky='wen')

    label_4 = CTkEntry(master=sub_frame,placeholder_text='Serial',textvariable= entry_var, corner_radius=0,) 
    label_4.grid(row=1,column=0,padx=10,pady=10,sticky='w')

    label_5 = CTkEntry(master=sub_frame,placeholder_text='headset type',textvariable= entry_var2, corner_radius=0) 
    label_5.grid(row=1,column=1,padx=10,pady=10,sticky='e')

    
    checkbox1 =CTkCheckBox(master=sub_frame, text="Availble", variable=checkbox1_var, command=toggle_checkbox1)
    checkbox2 = CTkCheckBox(master=sub_frame, text="Not Availble", variable=checkbox2_var, command=toggle_checkbox2)

    checkbox1.grid(row=2,column=0,padx=(40,),pady=10,sticky='w')
    checkbox2.grid(row=2,column=1,padx=(0,40),pady=10,sticky='e')
    button = CTkButton(master=frame, 
                        text='add',command= but) 
    button.grid(row=4,column=0,padx=10,pady=10,sticky='wen')
    label_6= CTkLabel(master=frame,text='add status ',text_color='red')
    existsText = CTkLabel(frame,text='this serial is already exists or the field is empty  ',text_color='red')
    return frame





