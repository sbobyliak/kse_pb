import datetime
user_bday=input("ввести дату народження (у форматі рррр-мм-дд)")
bday_date=datetime.datetime.strptime(user_bday, "%Y-%m-%d")
today=datetime.date.today()
days_lived=(today - bday_date.date()).days
print(f"Ви прожили вже {days_lived} днів")