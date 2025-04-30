# 📚 Bookshop Inventory Management System: OOP in Practice

This system showcases how **Object-Oriented Programming (OOP)** brings structure, reusability, and clarity to a complex project like managing a bookstore. 🏪💻

## 🎯 Abstraction via an `Item` Base Class  
A general `Item` class defines **common properties** (like `title`, `price`) and **abstract methods** (like `display()` and `update_stock()`) 🧱. Specific items like `Book`, `Magazine`, or `DVD` inherit from this blueprint 📘🗞️💿.

➡️ This makes your code more organized and consistent by forcing every item to follow a common interface.  
✨ *"One blueprint, many types!"*

## 🧬 Inheritance in `Book`, `Magazine`, `DVD` Classes  
Each subclass **inherits** from `Item` and adds its own unique attributes (e.g. author for books, duration for DVDs).  
📘 `Book` has `author`,  
🗞️ `Magazine` has `issue`,  
💿 `DVD` has `duration`.

✅ This eliminates repetition and keeps the code DRY (Don't Repeat Yourself)!  
🚀 Add new item types with minimal effort.

## 🔐 Encapsulation of Data (e.g. Price)  
Private or protected attributes like `_price` ensure that **data is hidden** and only accessed or changed through methods (like `set_price()`).  
🛡️ Protects data from bad input (e.g. no negative prices!).  
🎯 Keeps internal logic safe and clean.

## 🔄 Polymorphism with Overridden Methods  
Different item types implement `display()` in their **own way**, but they can be used **interchangeably**:

```python
for item in inventory:
    item.display()  # Works for Book, DVD, Magazine...
```

🎭 This is **polymorphism**: same interface, different behaviors.  
It keeps your code flexible and future-proof.

## 🧩 Modularity and Clear Responsibilities  
Each class has a clear role:
- 🧱 `Item`: common structure
- 📚 `Book`, 🗞️ `Magazine`, 💿 `DVD`: specific types
- 🏬 `Bookstore`: manages the inventory
- 🛒 `Order`: handles purchases
- 👥 `Client` / 🧑‍💼 `Employee`: interact with the system

✅ Easier to debug, expand, or improve one part without breaking others.

## 🛠️ Maintainability and Extensibility  
Want to add a 🧾 `Journal` item later? Just create a new class inheriting from `Item`. No need to rewrite your menus or ordering code.

🔧 Change how `DVD` calculates price? Update the `DVD` class—no ripple effects!

🌱 **The system grows with you.**

## 🧠 Separation of Concerns  
Business logic (like stock updates or searching) lives in classes like `Bookstore`.  
User interaction (menus, input) is handled separately.

🧼 Keeps code clean and focused.  
🧪 Easier to test and debug.

## 🧑‍💻 Interactive CLI Interface  
Your menu system reads input, then delegates work to the classes:

```python
choice = input("1. Add Book\n2. Exit\nChoice: ")
if choice == "1":
    bookstore.add_book(...)
```

👥 The user sees options, but behind the scenes, your object-oriented code keeps everything running smoothly.

---

## ✅ Summary of OOP Benefits (with emojis!)

| Principle       | Description                             | Emoji |
|----------------|-----------------------------------------|-------|
| **Abstraction** | Define common structure via base class  | 🧱    |
| **Inheritance** | Reuse shared logic in child classes     | 🧬    |
| **Encapsulation** | Hide internal data safely              | 🔐    |
| **Polymorphism** | Use different objects the same way     | 🔄    |
| **Modularity** | Each class has one clear job             | 🧩    |
| **Extensibility** | Easy to grow and add new features     | 🌱    |
| **Maintainability** | Easy to fix and change              | 🛠️    |

---

## 💻 Installation

To run this application on your local machine:

1. **Clone the repository:**

```bash
git clone https://github.com/obaidah3/Bookshop-Inventory-Management-System.git
```

2. **Navigate to the project directory:**

```bash
cd Bookshop-Inventory-Management-System
```

> **Note:** Ensure you have Python installed before running the script. If using another language, adjust the setup accordingly.

---

## 🛠️ Usage

### 👩‍💻 Client Interaction Example

```text
---- Welcome to Bookshop 📚 ----
Are you an Employee or a Client ?: client
Enter Name : John Doe

----- Welcome John Doe -----
1. Place an Order 🛒
2. Check Price 💰
3. Search for an Item 🔍

Enter your choice -> 1
**********************
How many items do you want to order? 2

Enter the title of the book? Harry Potter and the Philosopher's Stone
Item exists!
Do you want the Details? (y / n) y

------- Details ---------
Title : Harry Potter and the Philosopher's Stone
Author : J.K. Rowling
Price : 12.99 EGP
**********************

Enter the title of the book? Inception
Item exists!
Do you want the Details? (y / n) y

------- Details ---------
Title : Inception
Author : Christopher Nolan
Price : 14.99 EGP
```

---

### 👩‍💼 Employee Interaction Example

```text
---- Welcome to Bookshop 📚 ----
Are you an Employee or a Client ?: employee
Enter Name : Alice Smith
Enter your Role : Manager
Enter the intended passcode : 1234

---- Employee Menu ----
1. Add to Inventory 📦
2. Check the Price for an Item 💰
3. Search for an Item 🔍
4. View Customer Orders 📊
5. Update an Item ✏️

Enter an Option -> 1
**********************
What do you want to add to the inventory? :
1. Book 📖
2. Magazine 📰
3. DVD 🎥

Enter a Number -> 2
.............................................................................................

Title of the Magazine : Time Out
The Author : David Walsh
The Issue Number : July 2024
Publication Date : 2024-07-01
Enter the Editor : John Doe
Enter Price : 5.99

Time Out by David Walsh is added Successfully ✅
```

#### View Orders:

```text
---- Employee Menu ----
Enter an Option -> 4

Customer: John Doe
Items:
- Harry Potter and the Philosopher's Stone (12.99 EGP)
- Inception (14.99 EGP)
Total: 27.98 EGP 💸
```

#### Update an Item:

```text
---- Employee Menu ----
Enter an Option -> 5
**********************
What do you want to Update? :
1. Book 📖
2. Magazine 📰
3. DVD 🎥

Enter a Number -> 1
What is the title of the book? Harry Potter and the Philosopher's Stone
Item exists!

What do you want to Update? :
1. Title 📚
2. Author 👩‍🎨
3. Genre 🎭
4. ISBN 🔢
5. Number of Pages 📄
6. Price 💰

Enter a Number -> 6
New Price of the Book : 300

Harry Potter and the Philosopher's Stone is updated Successfully ✅
```

---
🎉 With OOP, your bookstore system is easier to build, expand, debug, and use—today and in the future!  
