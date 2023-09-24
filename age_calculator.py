from tkinter import *
from PIL import Image, ImageTk
from datetime import date

root = Tk()
root.title("Age Calculator - Which gen do you belong to?")
root.iconbitmap("./supplementary/calculator.ico")        ## by Hamel Khaled - CC 4.0, https://www.iconfinder.com/khaled17
root.geometry("600x700")


# Define function to calculate user's age
def calculate():
    # Logic to calculate user's age
    user_birthdate = date(int(input_year.get()), int(month_dict[input_month_clicked.get()]), int(input_day.get()))
    delta = date.today() - user_birthdate
    user_age_year = delta.days // 365
    user_age_month = (delta.days - (user_age_year * 365)) // 30
    user_age_day = delta.days - (user_age_year * 365) - (user_age_month * 30)

    # Logic to get user's gen classification
    user_birthyear = int(input_year.get())

    if user_birthyear <= 1900:
        user_gen_label_txt = "Lost Generation"
        bg_color = "#66d93d"
    elif user_birthyear >= 1901 and user_birthyear <= 1927:
        user_gen_label_txt = "Greatest/G.I. Generation"
        bg_color = "#3db48d"
    elif user_birthyear >= 1928 and user_birthyear <= 1945:
        user_gen_label_txt = "Silent Generation"
        bg_color = "#adaeae"
    elif user_birthyear >= 1946 and user_birthyear <= 1964:
        user_gen_label_txt = "Baby Boomers"
        bg_color = "#89b1fc"
    elif user_birthyear >= 1965 and user_birthyear <= 1980:
        user_gen_label_txt = "Generation X"
        bg_color = "#fc8989"
    elif user_birthyear >= 1981 and user_birthyear <= 1996:
        user_gen_label_txt = "Millenials/Generation Y"
        bg_color = "#f8d235"
    elif user_birthyear >= 1997 and user_birthyear <= 2012:
        user_gen_label_txt = "Zoomers/Generation Z"
        bg_color = "#d663fc"
    elif user_birthyear >= 2012 and user_birthyear <= date.today().year:
        user_gen_label_txt = "Generation Alpha"
        bg_color = "#fcb139"
    elif user_birthyear > date.today().year:
        user_gen_label_txt = "not born yet..."
        bg_color = "white"

    global user_age_gen_label
    user_age_gen_label = Label(frame_input, text="Your age now is "
                                             + str(user_age_year) + " years, "
                                             + str(user_age_month) + " months, "
                                             + str(user_age_day) + " days.\n\n"
                                             + "You are " + user_gen_label_txt
                           , font=('Arial', 12)
                           , bg=bg_color
                           , wraplength=400
                           , pady=40)
    user_age_gen_label.grid(row=5, column=0, columnspan=4)

    # Configure other bg
    frame_input.configure(bg=bg_color)
    input_year_label.configure(bg=bg_color)
    input_month_label.configure(bg=bg_color)
    input_day_label.configure(bg=bg_color)



# Define clear function
def clear():
    input_year.delete(0,END)
    input_day.delete(0,END)
    input_month_clicked.set(list(month_dict.keys())[0])
    user_age_gen_label.destroy()

    # Configure other bg
    frame_input.configure(bg=root.cget("background"))
    input_year_label.configure(bg=root.cget("background"))
    input_month_label.configure(bg=root.cget("background"))
    input_day_label.configure(bg=root.cget("background"))




# Put image of generation
img_basewidth = 600
gen_map = Image.open("./supplementary/Generation_timeline.png")      ## By Cmglee - Own work, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=91612069
img_ratio = gen_map.size[0] / img_basewidth
gen_map = gen_map.resize(size=( int(gen_map.size[0] / img_ratio), int(gen_map.size[1] / img_ratio)))
gen_map = ImageTk.PhotoImage(gen_map)

gen_map_label = Label(root, image=gen_map)
gen_map_label.pack()

# Print today's date
today = date.today().strftime("%A, %d %B %Y")
today_label = Label(root, text="Today is " + str(today), font=('Arial', 16), pady=30)
today_label.pack()

# Create a frame
frame_input = LabelFrame(root)
frame_input.pack(pady=20)

# Put entries for user's birth year, month, date
input_year_label = Label(frame_input, text="Birth Year:", anchor='e', justify='right', width=15, font=('Arial', 10))
input_year_label.grid(row=2, column=0)
input_month_label = Label(frame_input, text="Birth Month:", anchor='e', justify='right', width=15, font=('Arial', 10))
input_month_label.grid(row=3, column=0)
input_day_label = Label(frame_input, text="Birth Day:", anchor='e', justify='right', width=15, font=('Arial', 10))
input_day_label.grid(row=4, column=0)

# input month options
month_dict = {
    "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6
    , "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12
}
input_month_clicked = StringVar()
input_month_clicked.set(list(month_dict.keys())[0])

input_year = Entry(frame_input, width=30)
input_year.grid(row=2, column=1)
input_month = OptionMenu(frame_input, input_month_clicked, *month_dict.keys())
input_month.config(width=24)
input_month.grid(row=3, column=1)
input_day = Entry(frame_input, width=30)
input_day.grid(row=4, column=1)

# Create Button to calculate
calc_btn = Button(frame_input, text="Calculate my age!", width=10, wraplength=50, height=5, command=calculate)
calc_btn.grid(row=2, column=2, rowspan=3, sticky='wn', padx=10)

# Create Button to clear
clr_btn = Button(frame_input, text="Clear", width=10, wraplength=50, height=5, command=clear)
clr_btn.grid(row=2, column=3, rowspan=3, sticky='wn', padx=10)


root.mainloop()