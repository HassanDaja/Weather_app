import requests
from tkinter import *
from tkinter import messagebox
#IP fetch
api_ip='https://api.ipify.org?format=json'
ip=requests.get(api_ip)
ip=ip.json()
ip=ip['ip']
##Current location
IP_API=f"https://ipapi.co/{ip}/json/"
respose1=requests.get(IP_API)
data1=respose1.json()
city=data1['city']


##weather Api
def get_weather():
        try:
            city=e1.get()
            api_key="3419bc2f02b9c803e89254a930da8dd1"
            base="http://api.openweathermap.org/data/2.5/weather"
            url=f"{base}?q={city}&appid={api_key}"
            response2=requests.get(url)
            data2=response2.json()

            temp=int(data2['main']['temp']-273.15)
            pressure=data2['main']['pressure']
            wind_speed=data2['wind']['speed']
            desc=data2['weather'][0]['description']
            Header.config(text=f"Current Weather in \n {city}")
            lab_temp.config(text= f"Temperature:{temp}")
            lab_pre.config(text=f"Pressure : {pressure}")
            lab_desc.config(text=f"Description of Weather : {desc}")
        except:
            messagebox.showinfo("Info","Something went wrong")


#current location information
api_key="3419bc2f02b9c803e89254a930da8dd1"
base="http://api.openweathermap.org/data/2.5/weather"
url=f"{base}?q={city}&appid={api_key}"
response2=requests.get(url)
data2=response2.json()

temp=int(data2['main']['temp']-273.15)
pressure=data2['main']['pressure']
wind_speed=data2['wind']['speed']
desc=data2['weather'][0]['description']
#Tkinter Gui
root=Tk()
root.geometry("350x500")
root.configure(background='#262626')
Header=Label(root,text=f"Current Weather in \n {city}",font=("Arial",14,"bold"),bg='#262626',fg="white")
Header.pack()
lab_temp=Label(root,text=f"Temperature:{temp}",font=("Arial",14),bg='#262626',fg="white")
lab_temp.pack()
lab_pre=Label(root,text=f"Pressure : {pressure}",font=("Arial",14),bg='#262626',fg="white")
lab_pre.pack()
lab_desc=Label(root,text=f"Description of Weather : {desc}",font=("Arial",14),bg='#262626',fg="white")
lab_desc.pack()
Label(root,text="Search For other cities",font=("Arial",14,"bold"),bg='#262626',fg="white").pack(pady=40)
Label(root,text=f"Enter City Name",font=("Arial",14),bg='#262626',fg="white").pack()
e1=Entry(root,width=20,font=("Arial",14),fg="#262626")
e1.pack(pady=10)
Button(root,text="Search",borderwidth = 0,font=("Arial",12,"bold"),fg="#262626",command=get_weather).pack()
root.mainloop()


