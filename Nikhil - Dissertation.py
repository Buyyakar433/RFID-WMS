# -*- coding: utf-8 -*-
# **Developing a technology-based Warehouse Management System (WMS) that integrates RFID technology for effective inventory tracking and management**

"Required libraries"

import tkinter as tk

"""Initialise necessary Variables and Data Structures"""

class InventoryItem:
    def __init__(self, item_id, name, quantity, location):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.location = location

class RFIDReader:
    def read_tag(self):
        # Simulate reading RFID tag
        tag_data = "RFID123"
        return tag_data

"""Receive input data such as inventory items, locations and rfid tag infromation"""

class Warehouse:
    def __init__(self, root):
        self.inventory = {}
        self.root=root
        self.root.title("Warehouse Management System")

        # Create and place widgets
        self.label = tk.Label(root, text="Welcome to WMS")
        self.label.grid(row=0, column=0, columnspan=2, pady=10)

        self.button_frame = tk.Frame(root)
        self.button_frame.grid(row=1, column=0, padx=10, pady=10)

        self.button_add_item = tk.Button(self.button_frame, text="Add Item", command=self.add_item)
        self.button_add_item.grid(row=0, column=0, padx=10, pady=5)

        self.button_remove_item = tk.Button(self.button_frame, text="Remove Item", command=self.remove_item)
        self.button_remove_item.grid(row=1, column=0, padx=10, pady=5)

        self.button_track_inventory = tk.Button(self.button_frame, text="View Inventory", command=self.track_inventory)
        self.button_track_inventory.grid(row=2, column=0, padx=10, pady=5)



    def add_item(self, item):
        if item.item_id not in self.inventory:
            self.inventory[item.item_id] = item
        else:
            self.inventory[item.item_id].quantity += item.quantity

    def remove_item(self, item_id, quantity):
        if item_id in self.inventory:
            if self.inventory[item_id].quantity >= quantity:
                self.inventory[item_id].quantity -= quantity
            else:
                print("Insufficient quantity in inventory")

    def track_inventory(self, rfid_reader):
        tag_data = rfid_reader.read_tag()
        # Use tag data to track inventory
        if tag_data in self.inventory:
            print("Item found:", self.inventory[tag_data].name)
            print("Location:", self.inventory[tag_data].location)
        else:
            print("Item not found in inventory")

"""implement core functionalities of the WMS, including inventory tracking, storage optimisation and RFID integration"""

# Usage example

if __name__ == "__main__":
    # Create Tkinter root window
    root = tk.Tk()
    root.geometry("800x400")

    # Initialize Warehouse
    warehouse = Warehouse(root)
    
    # Add inventory items
    item1 = InventoryItem("RFID123", "Widget", 100, "A1")
    warehouse.add_item(item1)

    # Simulate RFID tag reading
    print("Simulating RFID tag reading...")
    rfid_reader = RFIDReader()
    warehouse.track_inventory(rfid_reader)

    wms = Warehouse(root)
    # Start the main event loop
    root.mainloop()

"""Display relevant information"""









