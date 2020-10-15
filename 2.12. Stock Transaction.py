""" 
12. Stock Transaction Program
Last month Joe purchased some stock in Acme Software, Inc. Here are the 
  details of the purchase:
- The number of shares that Joe purchased was 2,000.
- When Joe purchased the stock, he paid $40.00 per share
- Joe paid his stock broker a commission that amounted to 3% of the amount he
   paid for the stock
Two weeks later Joe sold the stock. Here are the details of the sale:
- The number of shares that Joe sold was 2,000.
- He sold the stock for $42.75 per share
- He paid his stockbroker another commission that amounted to 3 percent 
 of the amount he received for the stock                               
Write a program that displays the following information:
The amount of money Joe paid for the stock.
The amount of commission Joe paid his broker when he bought the stock.
The amount that Joe sold the stock for. 
The amount of commission Joe paid his broker when he sold the stock. 
Display the amount of money that Joe had left when he sold the stock 
and paid his broker(both times). 
If this amount is positive, then Joe made a profit. 
If the amount is negative, then Joe lost money.
Reference:
(1) Starting out with Python, Third Edition, Tony Gaddis Chapter 2
(2) https://youtu.be/t6MV_A54IkI
"""
# let store the values in variable
number_of_share_purchased = 2000
amount_paid_per_share = 40.00
# Calculate the amount paid per stock
amount_paid_per_stock = number_of_share_purchased * amount_paid_per_share
# Calculate the commission for buying
commission_for_buying = 0.03 * amount_paid_per_stock
number_of_share_sold = 2000
amount_sold_per_share = 42.75
# Calculate the amount he received for the stock
amount_received_per_stock = number_of_share_sold * amount_sold_per_share
# Calculate the commission for sold
commission_for_sold = 0.03 * amount_received_per_stock
# Calculate the profit
profit = amount_received_per_stock - commission_for_sold \
    - amount_paid_per_stock - commission_for_buying

# displays the information
print("Amount Paid for stock : $" + format(amount_paid_per_stock, ",.2f") , \
      "Commission for buying : $" + format(commission_for_buying, ",.2f") , \
      "Amount received per stock : $"  + \
      format(amount_received_per_stock, ",.2f"),
      "Commission for selling : $"  + \
      format(commission_for_sold, ",.2f"),\
      "profit : $"  + format(profit, ",.2f") , sep = "\n")
