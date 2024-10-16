days_driving = int(input("How many days have you been driving for?"))
years = days_driving // 365  
remaining_days = days_driving % 365
weeks = remaining_days // 7
remaining_days = remaining_days % 7
print("Years:", years)
print("Weeks:", weeks)
print ("Days:", remaining_days)