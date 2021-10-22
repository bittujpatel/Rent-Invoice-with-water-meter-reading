import sys
from datetime import date, timedelta

Date = date.today()
Month = Date.strftime("%B")

Mday = date.today().replace(day=1)
lastm = Mday - timedelta(days=1)
prev_month = lastm.strftime("%B")
mnt_code = prev_month[0:4]

orig_stdout = sys.stdout
f = open('out.txt', 'w')
sys.stdout = f

#Add Required From and To Details


#RENT
Rent = int(input("Enter Rent Amount "))

print("**********\n😇Reminder : \n**********\n ")
if Rent != 0:
    print(f'Rent ({mnt_code.upper()})                ₹ {Rent}')

M_type = int(input('Type of Meter\n \t1) Simple \n\tor\n\t2) X10\n'))

#WATER_BILL
print(f"----------------------------------------\nWater Bill\n----------------------------------------")
Nos_m = int(input('Number of Meters '))
t = 0
i = 0
for i in range(Nos_m):
  if Nos_m != 0:
    Last_Reading = int(input("Enter Pevious Reading "))
    New_Reading = int(input("Enter New Reading "))
    if  M_type == 2:
      Last_Reading = 10*Last_Reading
      New_Reading = 10*New_Reading

    if New_Reading != 0:
      wtr_use = (New_Reading) - (Last_Reading)
      Rate = float(0.15)
      amount = int(round(wtr_use * Rate))
      print(f"({New_Reading}-{Last_Reading})\n  = {wtr_use} L\n\n({wtr_use})L×({Rate})\n")
      t = t + amount
print('                           ₹' , t)

#CALCULATIONS
Balance = int(input("Enter Balance Amount "))
current = int(input("Electricity Bill "))
Total = Rent + t + Balance + current

if current != 0:
  print(f"----------------------------------------\nCurrent Bill            ₹{current}")
if Balance != 0:
  print(f"________________________________________\nBalance                    ₹ {Balance}")
print(f"----------------------------------------\nTotal                     ₹ {Total}\n----------------------------------------")

sys.stdout = orig_stdout
f.close()
