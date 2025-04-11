examples = """
Example 1: 
------
def check_number(num):  
    if num % 2 == 0  
        print(f"{num} is even.")  
    else:  
        print(f"{num} is odd.")  
  
# Error: Missing colon after the 'if' condition  
check_number(5) 

Ruff errors:
>ruff check .
error: Failed to parse test.py:4:22: Expected '":"', but got Newline
test.py:4:22: E999 SyntaxError: Expected '":"', but got Newline
Found 1 error.
--------
Example 2:
--------
def calculate_area(radius):  
    return 3.14159 * radius * radius  
  
# Error: Misspelled function name  
area = calculat_area(5)  
print(f"The area is: {area}")  

Ruff errors:
ruff check .
test.py:20:8: F821 Undefined name `calculat_area`
Found 1 error.
---------
Example 3:
---------
def calculate_discount(price, discount):  
    if discount > 0:  
        discounted_price = price * (1 - discount / 100)  
        print(f"Discounted price: {discounted_price}")  
       else:  
        print("No discount applied.")  
  
# Error: 'else' block is not properly indented to match 'if' block  
calculate_discount(100, 10) 

Ruff errors:
ruff check .
error: Failed to parse test.py:39:8: unindent does not match any outer indentation level
test.py:39:8: E999 SyntaxError: unindent does not match any outer indentation level
Found 1 error.
----------------
Example 4:
import sys  
  
class Contact:  
    def __init__(self, firstname, lastname, phone, email):  
        self.firstname = firstname  
        self.lastname = lastname  
        self.phone = phone  
        self.email = email  
  
    def __str__(self):  
        return f"{self.firstname} {self.lastname}, Phone: {self.phone}, Email: {self.email}"  
  
# Error: Dictionary keys should be strings, and missing colons in dictionary  
contacts = {  
    1: Contact("John", "Doe", "555-1234", "john@example.com"),  
    2: Contact("Jane", "Doe", "555-5678", "jane@example.com"),  
}  
  
def list_contacts():  
    for id, contact in contacts.items():  
        print(f"Contact {id}: {contact}")  
  
def add_contact(firstname, lastname, phone, email):  
    # Error: 'contacts' is a dictionary, not a list. Cannot append to a dictionary.  
    new_contact = Contact(first_name, last_name, phone, email)  
    contacts.append(new_contact)  
  
def remove_contact(contact_id):  
    # Error: 'contact_id' should be converted to int before use, and KeyError handling is missing  
    del contacts[contact_id]  
  
def find_contact(query):  
    # Error: The function should iterate over the dictionary values, not the keys  
    for contact in contacts:  
        if query.lower() in contact.firstname.lower() or query.lower() in contact.lastname.lower():  
            print(contact)  
            break  
    else:  
        print("Contact not found.")  
  
def main():  
    if len(sys.argv) < 2:  
        print("Usage: contacts.py [list|add|remove|find] [arguments]")  
        sys.exit(1)  
  
    command = sys.argv[1].lower()  
    if command == "list":  
        list_contacts()  
    elif command == "add":  
        # Error: Not checking the correct number of arguments for the 'add' command  
        add_contact(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])  
    elif command == "remove":  
        # Error: Not converting the argument to integer before passing to remove_contact  
        remove_contact(sys.argv[2])  
    elif command == "find":  
        # Error: Not checking if the 'find' command has the necessary argument  
        find_contact(sys.argv[2])  
    else:  
        print("Invalid command.")  
  
# Error: Missing call to main function  
main

ruff errors:
ruff check .
test.py:25:27: F821 Undefined name `first_name`
test.py:25:39: F821 Undefined name `last_name`
Found 2 errors.
----------------
Example 5:
---------------
# This script is designed to manage blog posts, including creating, reading, and deleting posts.  
  
blog_posts = [  
    {"id": 1, "title": "Python Basics", "content": "Introduction to Python."},  
    {"id": 2, "title": "Advanced Python", "content": "Deep dive into Python."},  
]  
  
def list_blog_posts():  
    for post in blog_posts:  
        print(f"ID: {post['id']}, Title: {post['title']}")  
  
def create_blog_post(title, content):  
    # Error: 'id' calculation is incorrect, it should be based on the last post's id  
    new_id = len(blog_posts)  
    new_post = {"id": new_id, "title": title, "content": content}  
    # Error: The new post should be appended to the 'blog_posts' list, not the dictionary  
    blog_posts = new_post  
  
def read_blog_post(post_id):  
    # Error: 'post_id' should be converted to int before use  
    for post in blog_posts:  
        if post['id'] == post_id:  
            print(f"Title: {post['title']}\nContent:\n{post['content']}")  
            return  
    print("Post not found.")  
  
def delete_blog_post(post_id):  
    # Error: The loop should iterate over a range or a copy of the list when removing items  
    for post in blog_posts:  
        if post['id'] == post_id:  
            blog_posts.remove(post)  
            print("Post deleted.")  
            break  
    else:  
        print("Post not found.")  
  
def main():  
    print("Welcome to the Blog Post Manager.")  
    while True:  
        action = input("What would you like to do? [list|create|read|delete|exit]: ")  
        action = action.lower()  
          
        if action == "list":  
            list_blog_posts()  
        elif action == "create":  
            title = input("Enter the title of the post: ")  
            # Error: 'content' variable is not defined before use  
            create_blog_post(title, content)  
        elif action == "read":  
            post_id = input("Enter the ID of the post to read: ")  
            read_blog_post(post_id)  
        elif action == "delete":  
            post_id = input("Enter the ID of the post to delete: ")  
            # Error: Not converting the argument to integer before passing to delete_blog_post  
            delete_blog_post(post_id)  
        elif action == "exit":  
            break  
        else:  
            print("Invalid action.")  
  
# Error: Calling 'main' without parentheses  
main  
  
# This script is supposed to be run interactively in a terminal or command prompt.  

ruff errors:
ruff check .
test.py:14:18: F823 Local variable `blog_posts` referenced before assignment
test.py:17:5: F841 Local variable `blog_posts` is assigned to but never used
test.py:48:37: F821 Undefined name `content`
Found 3 errors.
No fixes available (1 hidden fix can be enabled with the `--unsafe-fixes` option).
----------
Example 6:
------------
# This script is intended to provide basic inventory management for a small store.  
# It includes a variety of intentional errors for educational purposes.  
  
class Inventory:  
    def __init__(self):  
        self.items = {}  
        self.total_value = 0  
  
    def add_item(self, item_name, price, quantity):  
        if item_name in self.items:  
            # Error: Incorrectly updating quantity and total value  
            self.items[item_name]['quantity'] += quantity  
            self.total_value += price  
        else:  
            # Error: Price and quantity should be converted to the correct type before assignment  
            self.items[item_name] = {'price': price, 'quantity': quantity}  
            self.total_value += price * quantity  
  
    def remove_item(self, item_name, quantity):  
        if item_name not in self.items:  
            print(f"Item {item_name} not found in inventory.")  
            return  
  
        # Error: Not checking if the quantity to remove exceeds the current stock  
        self.items[item_name]['quantity'] -= quantity  
        self.total_value -= self.items[item_name]['price'] * quantity  
  
    def get_inventory_value(self):  
        # Error: Incorrect calculation of total inventory value  
        for item in self.items.values():  
            self.total_value += item['price'] * item['quantity']  
        return self.total_value  
  
    def __str__(self):  
        inventory_list = []  
        for item_name, details in self.items.items():  
            inventory_list.append(f"{item_name} - Price: {details['price']}, Quantity: {details['quantity']}")  
        return "\n".join(inventory_list)  
  
inventory = Inventory()  
  
# Error: Missing quotes around item names  
inventory.add_item(Keyboard, 99.99, 5)  
inventory.add_item(Mouse, 49.99, 10)  
inventory.add_item(Monitor, 199.99, 2)  
  
# Error: Not handling the case where the item does not exist  
inventory.remove_item('Laptop', 1)  
  
# Error: Incorrect function call (should be inventory.get_inventory_value())  
print("Total inventory value:", Inventory.get_inventory_value())  
  
# Error: Misuse of __str__ method  
print(inventory.__str_())  
  
# Error: Logical error - total_value gets incremented every time get_inventory_value() is called  
print("Total inventory value after re-check:", inventory.get_inventory_value())  

Ruff Errors:
ruff check .
test.py:43:20: F821 Undefined name `Keyboard`
test.py:44:20: F821 Undefined name `Mouse`
test.py:45:20: F821 Undefined name `Monitor`
Found 3 errors.
"""

# print(examples)
