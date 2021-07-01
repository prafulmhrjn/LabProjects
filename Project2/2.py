''' If temperature is greater than 30, it's a hot day otherwise if it's less than 10, it's a cold day,
otherwise it's neither hot neither cold.
'''

temperature_today = float(input("Enter todays temperature:"))
if temperature_today> 30:
    print(f"its a hot day")
elif temperature_today<10:
    print(f"its cold today")
else:
    print(f"its neither hot nor cold")