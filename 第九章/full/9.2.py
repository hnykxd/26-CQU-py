dai,lilv,year = map(float, input().split(","))
lilv = lilv/100/12
yuegong = dai*lilv*(1+lilv)**(year*12)/((1+lilv)**(year*12)-1)
print(f"monthly_payment: {yuegong:.2f}, Total interest: {yuegong*year*12-dai:.2f}")