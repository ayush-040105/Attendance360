import tkinter as tk
from tkinter import Entry, Button, Label, font, PhotoImage, messagebox, ttk
from PIL import Image, ImageTk
import mysql.connector
import fitz  # PyMuPDF library
from io import BytesIO
from datetime import datetime
import os

class MainMenu:
    def __init__(self):
        self.root_menu = tk.Tk()
        self.root_menu.title("Main Menu")

        custom_font = font.Font(family="HK Grotesk", size=13, weight=font.BOLD)

        # Load the background image using Pillow
        background_image = Image.open('1.png')  # Replace 'background_image.png' with your image file
        background_image = ImageTk.PhotoImage(background_image)

        # Create a label to hold the background image
        background_label = tk.Label(self.root_menu, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Set a reference to the image to prevent garbage collection
        background_label.image=background_image

        # Add buttons to navigate to different pages
        self.button_login = Button(self.root_menu, text="Login", font=custom_font, background="#4628e7", foreground="#ECE9FC", command=self.open_login_page)
        self.button_login.place(x=760, y=430, width=120, height=40)

        #theory syllabus

        self.button1 = Button(self.root_menu, text="MATHS", font=custom_font, background='#5943F4', foreground="#FFFFFF", borderwidth=0, highlightthickness=0, command=self.open_pdf_maths)
        self.button1.place(x=160, y=105, width=150, height=25)

        self.button1 = Button(self.root_menu, text="COA", font=custom_font, background="#5943F4", foreground="#FFFFFF", borderwidth=0, highlightthickness=0, command=self.open_pdf_coa)
        self.button1.place(x=160, y=145, width=150, height=25)

        self.button1 = Button(self.root_menu, text="AT", font=custom_font, background="#5943F4", foreground="#FFFFFF", borderwidth=0, highlightthickness=0, command=self.open_pdf_at)
        self.button1.place(x=160, y=185, width=150, height=25)

        self.button1 = Button(self.root_menu, text="OS", font=custom_font, background="#5943F4", foreground="#FFFFFF", borderwidth=0, highlightthickness=0, command=self.open_pdf_os)
        self.button1.place(x=160, y=225, width=150, height=25)

        self.button1 = Button(self.root_menu, text="CNND", font=custom_font, background="#5943F4", foreground="#FFFFFF", borderwidth=0, highlightthickness=0, command=self.open_pdf_cnnd)
        self.button1.place(x=160, y=265, width=150, height=25)

        #lab syllabus
        
        self.button2 = Button(self.root_menu, text="NL", font=custom_font, background='#5943F4', foreground="#FFFFFF", borderwidth=0, highlightthickness=0, command=self.open_pdf_nl)
        self.button2.place(x=160, y=420, width=150, height=25)
        
        self.button2 = Button(self.root_menu, text="MPL", font=custom_font, background="#5943F4", foreground="#FFFFFF", borderwidth=0, highlightthickness=0, command=self.open_pdf_mpl)
        self.button2.place(x=160, y=460, width=150, height=25)

        self.button2 = Button(self.root_menu, text="PYTHON", font=custom_font, background="#5943F4", foreground="#FFFFFF", borderwidth=0, highlightthickness=0, command=self.open_pdf_python)
        self.button2.place(x=160, y=500, width=150, height=25)

        self.button2 = Button(self.root_menu, text="UNIX", font=custom_font, background="#5943F4", foreground="#FFFFFF", borderwidth=0, highlightthickness=0, command=self.open_pdf_unix)
        self.button2.place(x=160, y=540, width=150, height=25)
        
        # MySQL Database Connection (You may want to move this to a separate module)
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ayush@0401",
            database="attendance"
        )

        self.root_menu.geometry("{0}x{1}+0+0".format(1354, 690))
        self.root_menu.mainloop()

    def open_login_page(self):
        self.root_menu.destroy()
        LoginApp()

    # theory
        
    def open_pdf_maths(self):
        self.open_pdf("MATHS SYLLABUS.pdf")

    def open_pdf_coa(self):
        self.open_pdf("COA SYLLABUS.pdf")

    def open_pdf_at(self):
        self.open_pdf("AT SYLLABUS.pdf")

    def open_pdf_os(self):
        self.open_pdf("OS SYLLABUS.pdf")

    def open_pdf_cnnd(self):
        self.open_pdf("CNND SYLLABUS.pdf")

    # lab
        
    def open_pdf_nl(self):
        self.open_pdf("NL SYLLABUS.pdf")

    def open_pdf_mpl(self):
        self.open_pdf("MPL SYLLABUS.pdf")

    def open_pdf_python(self):
        self.open_pdf("PYTHON SYLLABUS.pdf")

    def open_pdf_unix(self):
        self.open_pdf("UNIX SYLLABUS.pdf")

    def open_pdf(self, pdf_file):
        if pdf_file:
            try:
                os.startfile(pdf_file)
            except OSError:
                messagebox.showerror("Error", "Failed to open PDF file.")

class LoginApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("LOGIN")

        # Load the background image using Pillow
        i1 = Image.open('2.png')
        i1 = ImageTk.PhotoImage(i1)

        # Create a custom font
        custom_font = font.Font(family="Times New Roman", size=16, weight=font.BOLD)
        custom_font1 = font.Font(family="Times New Roman", size=14, weight=font.BOLD)

        # Place the background image
        background_label = Label(self.root, image=i1)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.tx1 = Entry(self.root, font=custom_font, foreground="#000000", background="#D9D9D9")
        self.tx1.place(x=600, y=300, width=250, height=25)

        self.tx2 = Entry(self.root, show='*', font=custom_font, foreground="#000000", background="#D9D9D9")
        self.tx2.place(x=600, y=370, width=250, height=25)

        self.button1 = Button(self.root, text="Login", font=custom_font1, background="#4628e7", foreground="#ECE9FC", command=self.login_action)
        self.button1.place(x=600, y=465, width=120, height=35)

        self.root.geometry("{0}x{1}+0+0".format(1354, 690))

        # MySQL Database Connection
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ayush@0401",
            database="attendance"
        )

        self.cursor = self.db.cursor()

        self.root.mainloop()

    def login_action(self):
        username = self.tx1.get()
        password = self.tx2.get()

        # Check if the provided username and password match any record in the database
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        values = (username, password)

        self.cursor.execute(query, values)
        result = self.cursor.fetchone()

        if result:
            # Successful login
            self.root.destroy()  # Close the current window
            # Open the LectureTypePage
            LectureTypePage()
        else:
            # Incorrect credentials, display an error message
            print("Invalid username or password")
            messagebox.showerror("Error", "Invalid username or password. Please try again.")

class LectureTypePage:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Lecture Type Selection")

        self.i1 = Image.open('3.png')
        self.i1 = ImageTk.PhotoImage(self.i1)

        custom_font = font.Font(family="Times New Roman", size=18, weight=font.BOLD)

        background_label = ttk.Label(self.root, image=self.i1)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.var_lab_type = tk.StringVar()
        self.var_lecture_type = tk.StringVar()
        style = ttk.Style(self.root)

        # lecture details
        style.configure("TRadiobutton", font=custom_font, foreground="#4628e7", background='#F9F2FF')

        self.radio_regular = ttk.Radiobutton(self.root, text="Regular", variable=self.var_lecture_type, value="Regular", style="TRadiobutton")
        self.radio_regular.place(x=300, y=182, width=120, height=30)

        self.radio_proxy = ttk.Radiobutton(self.root, text="Proxy", variable=self.var_lecture_type, value="Proxy", style="TRadiobutton")
        self.radio_proxy.place(x=415, y=182, width=100, height=30)

        self.radio_extra = ttk.Radiobutton(self.root, text="Extra", variable=self.var_lecture_type, value="Extra", style="TRadiobutton")
        self.radio_extra.place(x=510, y=182, width=100, height=30)

        #class
        self.entry_class = Entry(self.root, font=custom_font, foreground="#000000", background="#FFF0F5")
        self.entry_class.place(x=300, y=257, width=250, height=30)

        #time slot
        self.entry_time_slots = Entry(self.root, font=custom_font, foreground="#000000", background="#FFF0F5")
        self.entry_time_slots.place(x=300, y=331, width=250, height=30)

        #topic
        self.entry_topic = Entry(self.root, font=custom_font, foreground="#000000", background="#FFF0F5")
        self.entry_topic.place(x=300, y=403, width=250, height=30)

        #date
        self.entry_date = Entry(self.root, font=custom_font, foreground="#000000", background="#FFF0F5")
        self.entry_date.place(x=300, y=472, width=250, height=30)

        #lab details

        self.radio_regular2 = ttk.Radiobutton(self.root, text="Regular", variable=self.var_lab_type, value="Regular", style="TRadiobutton")
        self.radio_regular2.place(x=1020, y=185, width=150, height=30)

        self.radio_proxy2 = ttk.Radiobutton(self.root, text="Proxy", variable=self.var_lab_type, value="Proxy", style="TRadiobutton")
        self.radio_proxy2.place(x=1135, y=185, width=120, height=30)

        self.radio_extra2 = ttk.Radiobutton(self.root, text="Extra", variable=self.var_lab_type, value="Extra", style="TRadiobutton")
        self.radio_extra2.place(x=1230, y=185, width=100, height=30)

        #class
        self.entry_class2 = Entry(self.root, font=custom_font, foreground="#000000", background="#FFF0F5")
        self.entry_class2.place(x=1020, y=260, width=250, height=30)

        #batch
        self.entry_batch = Entry(self.root, font=custom_font, foreground="#000000", background="#FFF0F5")
        self.entry_batch.place(x=1020, y=332, width=250, height=30)

        #time slot
        self.entry_time_slots2 = Entry(self.root, font=custom_font, foreground="#000000", background="#FFF0F5")
        self.entry_time_slots2.place(x=1020, y=402, width=250, height=30)

        #topic
        self.entry_topic2 = Entry(self.root, font=custom_font, foreground="#000000", background="#FFF0F5")
        self.entry_topic2.place(x=1020, y=472, width=250, height=30)

        #date
        self.entry_date2 = Entry(self.root, font=custom_font, foreground="#000000", background="#FFF0F5")
        self.entry_date2.place(x=1020, y=548, width=250, height=30)

        style = ttk.Style(self.root)
        self.button1 = Button(self.root, text="Submit Lab", font=custom_font, background="#4628e7", foreground="#FFFFFF", command=self.submit_lab_type)
        self.button1.place(x=915, y=610, width=200, height=35)

        self.button2 = Button(self.root, text="Submit Lecture", font=custom_font, background="#4628e7", foreground="#FFFFFF", command=self.submit_lecture_type)
        self.button2.place(x=150, y=610, width=200, height=35)

        self.root.geometry("{0}x{1}+0+0".format(1354, 690))
        self.root.mainloop()

    def submit_lecture_type(self):
        lecture_type = self.var_lecture_type.get()
        class_val = self.entry_class.get() 
        time_slots = self.entry_time_slots.get()
        topic = self.entry_topic.get()
        date_str = self.entry_date.get()

        if lecture_type and class_val and time_slots and topic and date_str:
            try:
                date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()

                self.db = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Ayush@0401",
                    database="attendance"
                )
                self.cursor = self.db.cursor()

                query = "INSERT INTO lectures (lecture_type, class, time_slots, topic, date) VALUES (%s, %s, %s, %s, %s)"
                values = (lecture_type, class_val, time_slots, topic, date_obj)

                self.cursor.execute(query, values)
                self.db.commit()

                messagebox.showinfo("Success", "Lecture data saved successfully.")
                self.root.destroy()  # Close the current window

            except ValueError:
                messagebox.showerror("Error", "Invalid date format. Please enter date in YYYY-MM-DD format.")

            except mysql.connector.Error as err:
                print(f"Error: {err}")
                messagebox.showerror("Error", "Failed to save lecture data. Please try again.")

            finally:
                if self.db.is_connected():
                    self.cursor.close()
                    self.db.close()

        else:
            messagebox.showwarning("Warning", "Please fill in all the fields.")

    def submit_lab_type(self):
        lab_type = self.var_lab_type.get()
        class_val = self.entry_class2.get()
        batch = self.entry_batch.get()
        time_slots = self.entry_time_slots2.get()
        topic = self.entry_topic2.get()
        date_str = self.entry_date2.get()

        if lab_type and class_val and batch and time_slots and topic and date_str:
            try:
                date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()

                self.db = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Ayush@0401",
                    database="attendance"
                )
                self.cursor = self.db.cursor()

                query = "INSERT INTO labs (lab_type, class, batch, time_slots, topic, date) VALUES (%s, %s, %s, %s, %s, %s)"
                values = (lab_type, class_val, batch, time_slots, topic, date_obj)

                self.cursor.execute(query, values)
                self.db.commit()

                messagebox.showinfo("Success", "Lab data saved successfully.")
                self.root.destroy()

            except ValueError:
                messagebox.showerror("Error", "Invalid date format. Please enter date in YYYY-MM-DD format.")

            except mysql.connector.Error as err:
                print(f"Error: {err}")
                messagebox.showerror("Error", "Failed to save lab data. Please try again.")

            finally:
                if self.db.is_connected():
                    self.cursor.close()
                    self.db.close()

        else:
            messagebox.showwarning("Warning", "Please fill in all the fields.")

if __name__ == "__main__":
    MainMenu()