import csv
import tkinter as tk

win = tk.Tk()
win.geometry("300x300")
win.title('clubInfoGetter')
win.config(bg="#FFF9EE")

output = []


def getName():
    for i in range(0, len(rows)):
        if nameEntry.get() == rows[i][9] or nameEntry.get() == rows[i][12]:
            return i
        else:
            outputLabel.config(text="Invalid Name")


def monthsPaid():
    global output
    notPaid = []
    nameRow = getName()
    for i in range(15, 26):
        if rows[nameRow][i] == "FALSE":
            notPaid.append(header[i])
    output.append(f"{nameEntry.get()} has not paid for {notPaid}\n")
    outputLabel.config(text=f"{nameEntry.get()} has not paid for {notPaid}\n")


def getCOF():
    cof = rows[getName()][11]
    output.append(f"The last four digits of the card on file is {cof}\n")
    return cof


def getNumbers():
    numbers = tk.StringVar()
    for i in range(0, len(rows)):
        numbers += rows[10][i]
    outputLabel.config(text=f"{numbers}")
    return numbers

def printNumbers():
    numbers = getNumbers()
    outputLabel.config(text=f"{numbers}")


def getEmails():
    emails = []
    for i in range(0, len(rows)):
        emails.append(rows[11][i])
    print(emails)
    return emails


nameLabel = tk.Label(text="Enter Name:")
nameLabel.config(bg="#FFF9EE")
nameLabel.grid(row=0,column=0)
nameEntry = tk.Entry()
nameEntry.grid(row=1,column=0)

infoButton = tk.Button(text="Get Information", command=monthsPaid)
infoButton.config(bg="#AFABA3")
infoButton.grid(row=1,column=1,ipadx=8)

numbersButton = tk.Button(text="Get all numbers", command=getNumbers)
numbersButton.grid(row=2,column=1,ipadx=8)

outputLabel = tk.Label(text="",bg="#AFABA3")
outputLabel.grid(row=2,column=0,padx=20,pady=10)

file = open('clubInfo.csv')
type(file)

rows = []

with open('clubInfo.csv', 'r') as csvfile:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
        #print(row)


win.mainloop()