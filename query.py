import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Virat1412",
  database="retailStore"
)
cur = conn.cursor()

# 1. List all customers
cur.execute("SELECT * FROM Customers")
all_customers = cur.fetchall()
print("1)",all_customers)

# 2. Find all orders placed in January 2023
cur.execute("SELECT * FROM Orders WHERE YEAR(OrderDate) = 2023 AND MONTH(OrderDate) = 1")
january_orders = cur.fetchall()
print("2)",january_orders)

# 3. Get the details of each order, including the customer name and email
cur.execute("SELECT Orders.OrderID, CONCAT(Customers.FirstName,' ',Customers.LastName) AS name, Customers.Email FROM Orders JOIN Customers ON Orders.CustomerID = Customers.CustomerID")
order_details = cur.fetchall()
print("3)",order_details)

# 4. List the products purchased in a specific order (e.g., OrderID = 1)
cur.execute("SELECT Products.ProductName FROM OrderItems JOIN Products ON OrderItems.ProductID = Products.ProductID WHERE OrderItems.OrderID = 1")
products_in_order = cur.fetchall()
print("4)",products_in_order)

# 5. Calculate the total amount spent by each customer
cur.execute("SELECT CONCAT(Customers.FirstName,' ',Customers.LastName) AS customer_name, SUM(OrderItems.Quantity * Products.Price) as total_spent FROM Customers JOIN Orders ON Customers.CustomerID = Orders.CustomerID JOIN OrderItems ON Orders.OrderID = OrderItems.OrderID JOIN Products ON OrderItems.ProductID = Products.ProductID GROUP BY Customers.CustomerID")
total_spent = cur.fetchall()
print("5)",total_spent)

# 6. Find the most popular product (the one that has been ordered the most)
cur.execute("SELECT Products.ProductName, SUM(OrderItems.Quantity) as total_quantity FROM Products JOIN OrderItems ON Products.ProductID = OrderItems.ProductID GROUP BY Products.ProductID ORDER BY total_quantity DESC LIMIT 1")
most_popular_product = cur.fetchall()
print("6)",most_popular_product)

# 7. Get the total number of orders and the total sales amount for each month in 2023
cur.execute("SELECT DATE_FORMAT(OrderDate, '%Y-%m') as month, COUNT(Orders.OrderID) as total_orders, SUM(OrderItems.Quantity * Products.Price) as total_sales FROM Orders JOIN OrderItems ON Orders.OrderID = OrderItems.OrderID JOIN Products ON OrderItems.ProductID = Products.ProductID WHERE YEAR(OrderDate) = 2023 GROUP BY month")
monthly_sales = cur.fetchall()
print("7)",monthly_sales)

# 8. Find customers who have spent more than $1000
cur.execute("SELECT CONCAT(Customers.FirstName,' ',Customers.LastName) AS customer_name, SUM(OrderItems.Quantity * Products.Price) as total_spent FROM Customers JOIN Orders ON Customers.CustomerID = Orders.CustomerID JOIN OrderItems ON Orders.OrderID = OrderItems.OrderID JOIN Products ON OrderItems.ProductID = Products.ProductID GROUP BY Customers.CustomerID HAVING total_spent > 1000")
big_spenders = cur.fetchall()
print("8)",big_spenders)

conn.close()
