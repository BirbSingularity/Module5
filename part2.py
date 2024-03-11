points = lambda books: 60 if books >= 8 else 30 if books >= 6 else 15 if books >= 4 else 5 if books >= 2 else 0

books_purchased = int(input("How many books have you purchased this month? "))
print(f"Points awarded: {points(books_purchased)}")
