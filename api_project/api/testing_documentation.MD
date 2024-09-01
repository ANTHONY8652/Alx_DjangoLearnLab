# **Testing Documentation for Django REST Framework API**

This guide outlines the steps to test CRUD operations for the Book API using the Django Browsable API, Postman, and curl.

## **1. Testing Using the Django Browsable API**

### **Objective:** 
Verify CRUD operations through the browsable API interface.

### **Steps:**

1. **Navigate to the API Endpoint:**  
   Open your browser and go to your API endpoint, such as `http://127.0.0.1:8000/books/`.

2. **Create a Resource (POST Request):**
   - Click on the "POST" button.
   - Fill out the form with the required data for the new resource (e.g., title and author for a book).
   - Click **Submit** to create the resource.
   - Confirm that the resource appears in the list with the correct data.

3. **Read/Retrieve a Resource (GET Request):**
   - From the list of resources, click on the link for a specific resource (e.g., `http://127.0.0.1:8000/books/1/`).
   - Verify that the details of the resource are correctly displayed.

4. **Update a Resource (PUT Request):**
   - On the detail page of a specific resource (e.g., `http://127.0.0.1:8000/books/1/`), modify the data in the form.
   - Click **PUT** to update the resource.
   - Verify that the updated data is correctly reflected on the page.
