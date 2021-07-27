import data_manager
import flight_search
import flight_data
import notification_manager
import smtplib
from tkinter import *
from tkinter import messagebox
BACKGROUNDCOLOR = "#E8F1F5"
CANVASCOLOR = "#E8F1F5"
ENTRYCOLOR ="#74F9FF"
LABELCOLOR = "#3282B8"
BUTTONCOLOR = "#3282B8"

fs = flight_search.FlightSearch()
data = data_manager.DataManager()
flight_finder = flight_data.FlightData()
notify = notification_manager.NotificationManager()
window = Tk()
sheet_data = data.read_data()
user_data = data.get_users()["users"]

for i in sheet_data:
    if i['iataCode'] == "":
        id_to_use = i["id"]
        flight_data = fs.find_iata(i["city"])
        flight_iata = flight_data["locations"][0]["code"]
        i["iataCode"]= flight_iata
        print(i)
        data.write_iata(code=i, id=id_to_use)

# for i in flights_list:
#     if i != []:
#         notify.send_sms(i[0])
#         print(i[0])

def send_email():
    flights_list = []
    users_data = data.get_users()
    for i in sheet_data:
        city = i["iataCode"]
        price = i["lowestPrice"]
        flights_list.append(flight_finder.compare_prices(price=price, city=city))
    for i in users_data["users"]:
        text = f"Hello {i['firstName']}\n We have some good flight deals for you today: \n"
        for j in flights_list:
            if j != []:
                text = text + j[0] +"\n"
                print(text)
        notify.send_email(email=i["email"], text=text)
    messagebox.showinfo(title="Success", message="Your email has been sent. Check your mailbox")


def add_button():
    user_data_fct = data.get_users()["users"]
    email = email_entry.get()
    last_name = l_name_entry.get()
    first_name = f_name_entry.get()
    for i in user_data_fct:
        print(i)
        if i["email"] ==email:
            messagebox.showerror(title="Email", message="This email is already in use, insert another email.")
        elif i["email"]=="":
            messagebox.showerror(title="Email", message="Please insert an email.")
        else:
            e_ok = True

        if last_name == "":
                messagebox.showerror(title="Email", message="Please type your last name.")
        else:
            l_ok = True
        if first_name == "":
            messagebox.showerror(title="Email", message="Please type your first name.")
        else:
            f_ok = True
        if e_ok and l_ok and f_ok :
            data.post_users(f_name=first_name, l_name=last_name, email=email)
            messagebox.showinfo(title="Info", message="Your info has been saved, press send an email "
                                                      "to get the cheapest flights")
            e_ok = False
            l_ok = False
            f_ok = False



image_logo = PhotoImage(file="Logo.png")
window.title("Flight Manager")
window.config(bg=BACKGROUNDCOLOR, padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0, bg=CANVASCOLOR)
canvas.create_image(100, 100, image=image_logo)
canvas.grid(column=1, row=0, columnspan=2)

f_name_label = Label(text="First Name",width=17, bg=LABELCOLOR)
f_name_label.grid(column=0, row=1)

f_name_entry = Entry(width=20)
f_name_entry.grid(column=0, row=2)

l_name_label = Label(text="Last Name",width=17,bg=LABELCOLOR)
l_name_label.grid(column=0, row=3)

l_name_entry = Entry()
l_name_entry.grid(column=0, row=4)

email_label = Label(text="Email",width=17,bg=LABELCOLOR)
email_label.grid(column=0, row=5)

email_entry = Entry()
email_entry.grid(column=0, row=6)

button_add = Button(text="Add",width=36, bg=BUTTONCOLOR, command=add_button)
button_add.grid(column=0, row=7, columnspan=2)

button_send_mail = Button(text="Send Email",width=36, bg=BUTTONCOLOR, command=send_email)
button_send_mail.grid(column=2, row=7, columnspan=2)

window.mainloop()