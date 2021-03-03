
#--- Currrency Converter ---

# this program uses Graphical User Interface(GUI)
# using the Python Tkinter Library.
# It will receive 2 currencys and currency value from the user provided
# And will convert the value to another number
# GUI components - root, the input, label and button widgets, dropdown boxes

# Ryan Walker
# 26th February 2021

#- - - Import Libraries - - 
import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk

# Currency Conversions



# Where AUD is the base currency you want to use
url = 'https://v6.exchangerate-api.com/v6/c22d219cc0606d01d9cfe002/latest/AUD'

# Making our request
response = requests.get(url)
data = response.json()

# Your JSON object
print(data)






#- - - Define Function - - -


#- - Design the Graphical User Interface (GUI)

#Build the Main root
root = Tk() #This creates a GUI and assigns it a name.
root.title("Ryan Walker")
root.configure(bg="Black")
root.geometry("350x500+1000+300")#Sets the root dimentions Width, Height, X & Y positions on screen.
#Create the widget including buttons, labels, Entries etc..


# --- Buttons
# Set name, style and assign a function to the command property
# Set its location and dimensions


# - Labels
# Name and set the style
# Set the location on the root


# Entries
# Name and style

# Set the location on the root


#- - - Mainline - - -
#root.mainloop() # This runs the program