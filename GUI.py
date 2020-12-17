from tkinter import *
from SeleniumTest import *  # Import the Selenium script from the directory


# Class structure of the Tkinter GUI application
class ZoomAttendanceReportScraper:
    def __init__(self, master):  # tk() will be passed as an instance variable
        self.master = master
        master.title("ALPFA Zoom Attendance Reports Scraper")
        master.geometry("350x400")
        self.Username = StringVar()
        self.Password = StringVar()

        self.Password.trace_add('write', self.verifyEntry)

        self.displayImage(master)

        self.Heading = Label(master, text="Zoom Attendance Report Scraper", font=("Times New Roman", 15))
        self.Heading.pack(pady=10)

        self.UsernameLabel = Label(master, text="Enter your NetID")
        self.UsernameLabel.pack(pady=5)

        self.UsernameEntry = Entry(master, text=self.Username)
        self.UsernameEntry.pack(pady=5)

        self.PasswordLabel = Label(master, text="Enter your Password")
        self.PasswordLabel.pack(pady=5)

        self.PasswordEntry = Entry(master, text=self.Password, show="*")
        self.PasswordEntry.pack(pady=8)

        # Assign a Button variable to a predefined Tk() Button function that utilizes a lambda function to trigger
        # the Selenium script when pressed
        self.Button = Button(master, text='Submit', state='disabled',
                             command=lambda: SeleniumScript(self.Username.get(), self.Password.get()))
        self.Button.pack(pady=8)

        # Allows users to execute the script by pressing enter
        master.bind('<Return>', lambda x: SeleniumScript(self.Username.get(), self.Password.get()))

    # Displays the ALPFA Rutgers-Newark image from the img folder
    def displayImage(self, master):
        self.canvas = Canvas(master, height=864, width=576)
        self.canvas.pack()
        self.img = PhotoImage(file='img/alpfalogo.png')
        self.bg = Label(self.canvas, image=self.img)
        self.bg.pack(pady=8)

    # Verifies if user has inputted both their username & password to enable the button
    def verifyEntry(self, *_):
        if not self.Password and not self.Username:
            self.Button.config(state='disabled')
        else:
            self.Button.config(state='normal')

# Assign the variable root to Tk() function
root = Tk()

# Creates an object that references the Zoom Attendance Report Scraper class
App = ZoomAttendanceReportScraper(root)

# Initiates the GUI
root.mainloop()
