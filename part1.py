years = int(input("Enter the number of years: "))
total_rainfall, total_months = 0, 0
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

for year in range(1, years + 1):
    for month in months:
        prompt = f"Enter amount of rainfall for {month} (year {year}) in inches: "
        total_rainfall += float(input(prompt))
        total_months += 1

print(f"Months: {total_months}\nTotal Rainfall: {total_rainfall} inches\nAverage Rainfall: {total_rainfall / total_months:.2f} inches/month")
