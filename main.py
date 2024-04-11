import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
class TrainBookingSystem:
def _init_(self, master):
self.master = master
self.master.title("Train Booking System")
self.master.geometry("375x494")
self.customer_name = tk.StringVar()
self.customer_age = tk.StringVar()
self.customer_gender = tk.StringVar()
self.from_station = tk.StringVar()
self.to_station = tk.StringVar()
self.ticket_class = tk.StringVar()
self.booked_tickets = [] # List to store booked tickets
# Additional attributes for cost
self.ticket_cost = tk.StringVar()
# Additional attribute for custom route cost
self.custom_route_cost = {
"chrompet-tambaram": {"First Class": 25, "Second Class": 5, "Vendors
Class": 5},
"tambaram-chrompet": {"First Class": 25, "Second Class": 5, "Vendors
Class": 5},
"chrompet-potheri": {"First Class": 55, "Second Class": 5, "Vendors Class":
5},
"potheri-chrompet": {"First Class": 55, "Second Class": 5, "Vendors Class":
5},
"tambaram-potheri": {"First Class": 55, "Second Class": 5, "Vendors Class":
5},
"potheri-tambaram": {"First Class": 55, "Second Class": 5, "Vendors Class":
5},
"vandalur-potheri": {"First Class": 55, "Second Class": 5, "Vendors Class":
5},
"Vandalur-Potheri": {"First Class": 55, "Second Class": 5, "Vendors Class":
5},
"potheri-perungalathur": {"First Class": 55, "Second Class": 5, "Vendors
Class": 5},
"urapakkam-potheri": {"First Class": 55, "Second Class": 5, "Vendors Class":
5},
"potheri-urapakkam": {"First Class": 55, "Second Class": 5, "Vendors Class":
5},
"guduvanchery-potheri": {"First Class": 55, "Second Class": 5, "Vendors
Class": 5},
"potheri-guduvanchery": {"First Class": 55, "Second Class": 5, "Vendors
Class": 5}
}
self.create_widgets()
def create_widgets(self):
tk.Label(self.master, text="Customer Name:").grid(row=0, column=0, padx=10,
pady=10, sticky='w')
tk.Entry(self.master, textvariable=self.customer_name).grid(row=0, column=1,
padx=10, pady=10)
tk.Label(self.master, text="Customer Age:").grid(row=1, column=0, padx=10,
pady=10, sticky='w')
tk.Entry(self.master, textvariable=self.customer_age).grid(row=1, column=1,
padx=10, pady=10)
tk.Label(self.master, text="Customer Gender:").grid(row=2, column=0,
padx=10, pady=10, sticky='w')
gender_combobox = ttk.Combobox(self.master,
textvariable=self.customer_gender, values=["Male", "Female"])
gender_combobox.grid(row=2, column=1, padx=10, pady=10)
gender_combobox.set("Male") # Set default value
# Dropdown menu for "From" station
tk.Label(self.master, text="From Station:").grid(row=3, column=0, padx=10,
pady=10, sticky='w')
from_station_combobox = ttk.Combobox(self.master,
textvariable=self.from_station, values=["tambaram", "chrompet", "potheri",
"vandalur", "perungalathur", "urapakkam", "guduvanchery"])
from_station_combobox.grid(row=3, column=1, padx=10, pady=10)
from_station_combobox.set("tambaram") # Set default value
# Dropdown menu for "To" station
tk.Label(self.master, text="To Station:").grid(row=4, column=0, padx=10,
pady=10, sticky='w')
to_station_combobox = ttk.Combobox(self.master, textvariable=self.to_station,
values=["tambaram", "chrompet", "potheri", "vandalur", "perungalathur",
"urapakkam", "guduvanchery"])
to_station_combobox.grid(row=4, column=1, padx=10, pady=10)
to_station_combobox.set("chrompet") # Set default value
tk.Label(self.master, text="Ticket Class:").grid(row=5, column=0, padx=10,
pady=10, sticky='w')
ticket_class_combobox = ttk.Combobox(self.master,
textvariable=self.ticket_class, values=["First Class", "Second Class", "Vendors
Class"])
ticket_class_combobox.grid(row=5, column=1, padx=10, pady=10)
ticket_class_combobox.set("First Class") # Set default value
tk.Label(self.master, text="Ticket Cost:").grid(row=6, column=0, padx=10,
pady=10, sticky='w')
tk.Entry(self.master, textvariable=self.ticket_cost,
state="readonly").grid(row=6, column=1, padx=10, pady=10)
tk.Button(self.master, text="Book Ticket",
command=self.book_ticket).grid(row=7, column=1, pady=20)
tk.Button(self.master, text="View History",
command=self.view_history).grid(row=8, column=1, pady=10)
def calculate_ticket_cost(self):
from_station = self.from_station.get()
to_station = self.to_station.get()
ticket_class = self.ticket_class.get()
# General distance-based cost calculation
distance_key = f"{from_station}-{to_station}"
distance_rate = 0
if distance_key in self.custom_route_cost:
route_cost = self.custom_route_cost[distance_key].get(ticket_class)
if route_cost is not None:
return route_cost
return distance_rate
def book_ticket(self):
customer_name = self.customer_name.get()
customer_age = self.customer_age.get()
customer_gender = self.customer_gender.get()
from_station = self.from_station.get()
to_station = self.to_station.get()
ticket_class = self.ticket_class.get()
booking_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
if not customer_name or not customer_age or not customer_gender or not
from_station or not to_station or not ticket_class:
messagebox.showerror("Error", "Please fill in all the details.")
else:
ticket_cost = self.calculate_ticket_cost()
self.ticket_cost.set(ticket_cost)
ticket_info = (customer_name, customer_age, customer_gender,
from_station, to_station, ticket_class, booking_date, ticket_cost)
self.booked_tickets.append(ticket_info)
messagebox.showinfo("Success", "Ticket booked!")
def view_history(self):
history_window = tk.Toplevel(self.master)
history_window.title("Booking History")
# Table for booking history
columns = ("Customer", "Age", "Gender", "From", "To", "Class", "Booking
Date", "Ticket Cost")
history_tree = ttk.Treeview(history_window, columns=columns,
show="headings")
for col in columns:
history_tree.heading(col, text=col)
history_tree.column(col, width=100)
for ticket_info in self.booked_tickets:
history_tree.insert("", "end", values=ticket_info)
history_tree.pack(pady=10)
def main():
root = tk.Tk()
app = TrainBookingSystem(root)
root.mainloop()
if _name_ == "_main_":
main()