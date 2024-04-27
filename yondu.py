share_yondu = 0.0
share_peter = 0.0
share_crew = 0.0

#Get inputs
num_pirates = int(input("How many pirates:\n"))
units = float(input("How many units:\n"))
print("\n")

#crew gets 3 units per member except yondu and peter
share_crew += 3
units = units - (3 * (num_pirates - 2))

#Calculate Yondu's secret share
share_yondu += round((units * .13), 2)
units = round(units - (units * .13), 2) 

#Calculate Peter's secret share
share_peter += round((units * .11), 2)
units = round(units - (units * .11), 2)

#divide remaining share
share_yondu += round(units/num_pirates, 2)
share_peter += round(units/num_pirates, 2)
share_crew += round(units/num_pirates, 2)

#print shares
print(f"Yondu's share: {share_yondu:.2f}")
print(f"Peter's share: {share_peter:.2f}")
print(f"Crew's share: {share_crew:.2f}")