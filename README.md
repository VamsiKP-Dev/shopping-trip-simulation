
# Shopping Trip Simulation in Python

This is a simple Python program that simulates a shopping trip using a class to organize data like destination, shopping items, and friends joining. 
It demonstrates object-oriented programming principles in a real-life context.

---
## Detailed Explanation

### Class: `ShoppingTrip`

The program uses a class called `ShoppingTrip` to encapsulate all related information and actions for a fictional shopping trip.

---

###  `__init__` Method (Initializer)

This method initializes the shopping trip with the following data:

- **Destination Details**:
  - `Destination = "M.G.Road"`
  - `time = "10:10 am"`
  - `mystop = "Halasur"`
  - `shop = "Shoppers Stop"`

- **Shopping List**:
  - A list is initialized with basic items:
    ```python
    self.shopping = ["Items List", "money", "Mobile"]
    ```
  - More items are added using `.append()`:
    - `"CreditCards"`
    - `"Carry Bag"`

- **Friends Joining the Trip**:
  - Individual friend status:
    ```python
    self.Ramesh = "Yes"
    self.Suresh = "No"
    self.Somesh = "Later"
    ```
  - All statuses are also stored in a dictionary:
    ```python
    self.friends = {"Ramesh": "Yes", "Suresh": "No", "Somesh": "May Be"}
    ```

- The dictionary is printed immediately to show the original values.

---

###  `start_trip` Method

This method simulates the start of the trip by performing the following:

1. **Update Friend's Status**:
   - `Somesh`'s status is changed from `"May Be"` to `"Yes"`:
     ```python
     self.friends["Somesh"] = "Yes"
     ```

2. **Print Updated Friend Info**:
   - The updated `friends` dictionary is printed.

3. **Print Shopping List**:
   - Displays the complete list of items planned for shopping.

4. **Final Output**:
   - All relevant details are printed for review.

---

###  Execution

At the end of the file, an object is created and the method is called:

```python
trip = ShoppingTrip()
trip.start_trip()
