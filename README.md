# IST105 - Assignment 6  
**Building an Interactive Web Application with Conditional Logic (Python + Django + MongoDB)**

## 📘 Overview
This project is a dynamic Django web application that collects five numerical inputs, processes them with Python logical and bitwise operations, and saves the results in a MongoDB database hosted on a separate EC2 instance.

The system demonstrates full integration between:
- A Django WebServer EC2 (Application Layer)
- A MongoDB EC2 instance (Data Layer)
- GitHub for version control and branching workflow

---

## ⚙️ Features
- Validates that all five inputs are numeric and non-negative.  
- Calculates:
  - Average value (checks if > 50)
  - Number of positive values
  - Bitwise even/odd evaluation for each number  
- Generates a sorted list of all values greater than 10.  
- Displays all results in an HTML template dynamically.  
- Saves each processed entry into MongoDB.  
- Includes a second page (`/view_all/`) to display all stored records.  

---

## 🧠 Technologies
- **Python 3.13.7**
- **Django Framework**
- **MongoDB 7.0.4**
- **AWS EC2 (Amazon Linux 2023)**
- **PyMongo**
- **Git & GitHub**

---

## 🗂️ Project Structure
