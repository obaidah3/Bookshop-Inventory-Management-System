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

🎉 With OOP, your bookstore system is easier to build, expand, debug, and use—today and in the future!  
