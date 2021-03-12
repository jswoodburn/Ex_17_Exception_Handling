from account import Account

barry = Account("barry", "jones", 1000)

print(barry._full_name)

barry.forename = "jeff"
print(barry.forename)
print(barry._full_name)

barry.surname = "bridges"
print(barry.surname)
print(barry._full_name)

# setattr(barry, "cust_no", "001")
# print(barry.cust_no)
