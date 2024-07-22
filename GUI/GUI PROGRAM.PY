import tkinter as tk
from tkinter import Toplevel
from tkinter import ttk
from PIL import Image,ImageTk
bikes={
    'Fz':'fz.jpg',
    'Ktm':'ktm.jpg',
    'Mt':'mt.jpg',
    'Pulsar':'pulsar.jpg',
    'R15':'r15.jpg',
    'Royal enfild':'royal enfiled.jpg',
    'Rx100':'Rx100.jpg'
}
def show_bike_image():
    selected_bike = bike_combobox.get()
    if selected_bike:
        new_window=Toplevel(root)
        new_window.title(selected_bike)
        img=Image.open(bikes[selected_bike])
        img=ImageTk.PhotoImage(img)
        img_label = tk.Label(new_window, image=img)
        img_label.image = img
        img_label.pack()
root = tk.Tk()
root.title("Latest Bike")
root.geometry("800x600")
background_image = Image.open("r15.jpg")
background_image = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)
frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75,relheight=0.1, anchor='n')
bike_combobox = ttk.Combobox(frame, values=list(bikes.keys()), state='readonly')
bike_combobox.set("Select a bike")
bike_combobox.pack(side=tk.LEFT, padx=10, pady=10)
show_button = tk.Button(frame, text="Show Bike", command=show_bike_image)
show_button.pack(side=tk.LEFT, padx=10, pady=10)
root.mainloop()
        
