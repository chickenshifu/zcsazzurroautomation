'''
Please declare your total battery capacity and your minimum discharge level.

Example:
Your Battery has a total charging capacity of 12.25 kilowatt hours. You provide the value "12.25" for totalBatteryCapacity as seen below. If your Battery for instance is a Lithium iron phosphate battery you might don't want to discharge it to 0.0% for longevity reasons. Instead you would want to discharge it to at highest 20.0%. In such a case you would provide "0.20" for minimumDischargeLevel.

If your minimum discharge level is 0.0%, please provide 0.0000001.

priceOfElectricity (float): provided in Cents/Pence/Centime/etc...

denomination (str): any value

language (str): ENG or GER
'''

language = 'ENG' # ENG or GER

totalBatteryCapacity = 12.25    # kWh
minimumDischargeLevel = 0.2   # equals 20.0 % // 0.0000001 if 0.0%

denomination = 'EUR'
priceOfElectricity = 0.50 #EUR, GBP, USD, you name it