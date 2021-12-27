from tkinter import *
import customtkinter
from tkinter import messagebox
import webbrowser

window = Tk()
window.minsize(300, 320)
window.config(bg="black")
window.resizable(0, 0)
window.title("Simple BMI & BMR Calculator")
window.iconbitmap("bmi&bmr.ico")
customtkinter.set_appearance_mode("Dark")


def bmi_conversion():
    forget()
    bmi_frame.pack(fill="both", expand=1)

    weight_label = Label(bmi_frame, text="Weight (Kg): ", bg="black", fg="white")
    weight_entry = customtkinter.CTkEntry(bmi_frame, corner_radius=5)

    height_label = Label(bmi_frame, text="Height (M): ", bg="black", fg="white")
    height_entry = customtkinter.CTkEntry(bmi_frame, corner_radius=5)

    weight_entry.place(x=100, y=100)
    weight_label.place(x=20, y=100)
    height_entry.place(x=100, y=150)
    height_label.place(x=20, y=150)

    bmi2 = Button(bmi_frame, text=" BMI", compound=LEFT, image=bmi_image, width=150, height=50, highlightthickness=0,
                  border=0, bg="black",
                  activebackground="black", command=bmi_conversion, fg="white", activeforeground="white",
                  cursor="hand2")
    bmr3 = Button(bmi_frame, text=" BMR", compound=LEFT, image=bmr_image, width=150, height=50, highlightthickness=0,
                  border=0, bg="black",
                  activebackground="black", command=bmr_conversion, fg="white", activeforeground="white",
                  cursor="hand2")
    about_app = Button(bmi_frame, bg="black", image=about_image, width=32, height=32, highlightthickness=0,
                       border=0, command=about_this_app, fg="white", activeforeground="white", activebackground="black")
    bmi2.place(x=10, y=0)
    bmr3.place(x=150, y=0)
    about_app.place(x=260, y=280)

    def converted():
        try:
            weight = float(weight_entry.get())
            height = float(height_entry.get())

            calculation = weight / (height * height)

            if calculation < 18.5:
                result_label.config(text=f"{calculation:.6}\nYou are Underweight", fg="red")
            elif calculation >= 18.5 or calculation < 24.9:
                result_label.config(text=f"{calculation:.6}\nYou are Healthy", fg="green")
            elif calculation >= 25.0 or calculation < 29.9:
                result_label.config(text=f"{calculation:.6}\nYou are Overweight", fg="red")
            elif calculation >= 30.0:
                result_label.config(text=f"{calculation:.6}\nYou are Obese", fg="red")
        except ValueError:
            messagebox.showerror(title="Error", message="Please fill out every entries.")

    # calculate = Button(bmi_frame, text="Calculate", command=converted, bg="black", fg="white", activebackground="black",
    #                    activeforeground="white", width=17, highlightthickness=0)
    calculate = customtkinter.CTkButton(master=bmi_frame, text="Calculate", height=10, command=converted,
                                        cursor="hand2")
    calculate.place(x=100, y=200)

    result_label = Label(bmi_frame, text="", bg="black", fg="white")
    result_label.place(x=90, y=240)


def bmr_conversion():
    forget()
    bmr_frame.pack(fill="both", expand=1)

    bmi2 = Button(bmr_frame, text=" BMI", compound=LEFT, image=bmi_image, width=150, height=50, highlightthickness=0,
                  border=0, bg="black",
                  activebackground="black", command=bmi_conversion, fg="white", activeforeground="white",
                  cursor="hand2")
    bmr3 = Button(bmr_frame, text=" BMR", compound=LEFT, image=bmr_image, width=150, height=50, highlightthickness=0,
                  border=0, bg="black",
                  activebackground="black", command=bmr_conversion, fg="white", activeforeground="white",
                  cursor="hand2")
    about_app = Button(bmr_frame, bg="black", image=about_image, width=32, height=32, highlightthickness=0,
                       border=0, command=about_this_app, fg="white", activeforeground="white", activebackground="black")

    var = StringVar()

    male_gender = Radiobutton(bmr_frame, text="Male", variable=var, value="male", activebackground="black",
                              background="black", fg="white", selectcolor="#3174e0")
    female_gender = Radiobutton(bmr_frame, text="Female", variable=var, value="female", selectcolor="#cf0a56",
                                activebackground="black", background="black", fg="white", )

    male_gender.place(x=90, y=90)
    female_gender.place(x=150, y=90)

    weight_label = Label(bmr_frame, text="Weight (Kg): ", bg="black", fg="white")
    weight_entry = customtkinter.CTkEntry(bmr_frame, corner_radius=5)

    height_label = Label(bmr_frame, text="Height (cm): ", bg="black", fg="white")
    height_entry = customtkinter.CTkEntry(bmr_frame, corner_radius=5)

    age_label = Label(bmr_frame, text="Age: ", bg="black", fg="white")
    age_entry = customtkinter.CTkEntry(bmr_frame, corner_radius=5)

    weight_entry.place(x=100, y=130)
    weight_label.place(x=20, y=130)
    height_entry.place(x=100, y=170)
    height_label.place(x=20, y=170)
    age_entry.place(x=100, y=205)
    age_label.place(x=20, y=205)

    bmi2.place(x=10, y=0)
    bmr3.place(x=150, y=0)
    about_app.place(x=260, y=280)

    def converted():
        try:
            weight = float(weight_entry.get())
            height = float(height_entry.get())
            age = int(age_entry.get())
            gender = str(var.get())

            if gender == "male":
                calculation = 66 + (13.7 * weight) + (5 * height) - (6.8 * age)
            elif gender == "female":
                calculation = 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)

            result_label.config(text=f"{calculation:.5}")
        except ValueError:
            messagebox.showerror(title="Error", message="Please fill out every entries.")

    # calculate = Button(bmr_frame, text="Calculate", command=converted, bg="black", fg="white", activebackground="black",
    #                    activeforeground="white", width=17, highlightthickness=0)
    calculate = customtkinter.CTkButton(master=bmr_frame, text="Calculate", height=10, command=converted,
                                        cursor="hand2")
    calculate.place(x=100, y=240)

    result_label = Label(bmr_frame, text="", bg="black", fg="white")
    result_label.place(x=90, y=270)


def dev_link():
    webbrowser.open("https://akashmahmud.ml/")


def about_this_app():
    forget()
    about_frame.pack(fill="both", expand=1)

    bmi2 = Button(about_frame, text=" BMI", compound=LEFT, image=bmi_image, width=150, height=50, highlightthickness=0,
                  border=0, bg="black",
                  activebackground="black", command=bmi_conversion, fg="white", activeforeground="white",
                  cursor="hand2")
    bmr3 = Button(about_frame, text=" BMR", compound=LEFT, image=bmr_image, width=150, height=50, highlightthickness=0,
                  border=0, bg="black",
                  activebackground="black", command=bmr_conversion, fg="white", activeforeground="white",
                  cursor="hand2")
    about_app = Button(about_frame, bg="black", image=about_image, width=32, height=32, highlightthickness=0,
                       border=0, command=about_this_app, fg="white", activeforeground="white", activebackground="black")

    bmi2.place(x=10, y=0)
    bmr3.place(x=150, y=0)
    about_app.place(x=260, y=280)

    # About Labels
    app_title = Label(about_frame, text="Simple BMI & BMR Calculator", font=("Arial", 13, "bold"), bg="black",
                      fg="white")
    description = Label(about_frame, text="It was just a hobby project.", font=("Arial", 10, "normal"), bg="black",
                        fg="white")
    developer_name = Label(about_frame, text="\nDeveloper\nNiaz Mahmud Akash", font=("Arial", 10, "normal"), bg="black",
                           fg="white")
    version = Label(about_frame, text="\nVersion\n1.0", font=("Arial", 10, "normal"),
                    bg="black", fg="white")

    def open_facebook():
        webbrowser.open("https://www.facebook.com/niazmahmud.akash.7/")

    def open_github():
        webbrowser.open("https://twitter.com/Viperz75")

    def open_twitter():
        webbrowser.open("https://github.com/Viperz75")

    facebook_button = Button(about_frame, image=facebook, highlightthickness=0, border=0, bg="black",
                             activebackground="black",
                             command=open_facebook, fg="white", activeforeground="white")
    github_button = Button(about_frame, image=github, highlightthickness=0, border=0, bg="black",
                           activebackground="black", command=open_github, fg="white", activeforeground="white")
    twitter_button = Button(about_frame, image=twitter, highlightthickness=0, border=0, bg="black",
                            activebackground="black", command=open_twitter, fg="white", activeforeground="white")

    facebook_button.place(x=110, y=240)
    github_button.place(x=140, y=240)
    twitter_button.place(x=170, y=240)

    app_title.place(x=38, y=60)
    description.place(x=68, y=90)
    developer_name.place(x=90, y=125)
    version.place(x=125, y=175)


def forget():
    for widgets in bmi_frame.winfo_children():
        widgets.destroy()
    for widgets in bmr_frame.winfo_children():
        widgets.destroy()
    for widgets in background_frame.winfo_children():
        widgets.destroy()
    for widgets in about_frame.winfo_children():
        widgets.destroy()
    about_frame.pack_forget()
    background_frame.pack_forget()
    bmi_frame.pack_forget()
    bmr_frame.pack_forget()


background_frame = Frame(window, width=300, height=320, bg="black")
bmi_frame = Frame(window, width=300, height=320, bg="black")
bmr_frame = Frame(window, width=300, height=320, bg="black")
about_frame = Frame(window, width=300, height=320, bg="black")

# Buttons
forget()
background_frame.pack(fill="both", expand=1)

calculator_background = PhotoImage(file="images/bmi-removebg-preview.png")
bmi_image = PhotoImage(file="images/bmi2.png")
bmr_image = PhotoImage(file="images/body-variant.png")
about_image = PhotoImage(file="images/about.png")
facebook = PhotoImage(file="images/facebook.png")
github = PhotoImage(file="images/github.png")
twitter = PhotoImage(file="images/twitter.png")

bmi = Button(background_frame, text=" BMI", compound=LEFT, image=bmi_image, width=150, height=50, highlightthickness=0,
             border=0,
             bg="black",
             activebackground="black", command=bmi_conversion, fg="white", activeforeground="white", cursor="hand2")
bmr = Button(background_frame, text=" BMR", compound=LEFT, image=bmr_image, width=150, height=50, highlightthickness=0,
             border=0,
             bg="black",
             activebackground="black", command=bmr_conversion, fg="white", activeforeground="white", cursor="hand2")
bmi_background = Button(background_frame, bg="black", image=calculator_background, width=320, height=130,
                        highlightthickness=0,
                        border=0, command=dev_link, fg="white", activeforeground="white", activebackground="black")
about = Button(background_frame, bg="black", image=about_image, width=32, height=32, highlightthickness=0,
               border=0, command=about_this_app, fg="white", activeforeground="white", activebackground="black")

bmi.place(x=10, y=0)
bmr.place(x=150, y=0)
bmi_background.place(x=-10, y=85)
about.place(x=260, y=280)

if __name__ == '__main__':
    window.mainloop()
