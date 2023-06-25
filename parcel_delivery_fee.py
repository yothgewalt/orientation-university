parcel_weight = int(input())

parcel_delivery_fee: int = 0
if parcel_weight <= 20:
    parcel_delivery_fee = 32

elif parcel_weight <= 100:
    parcel_delivery_fee = 37

elif parcel_weight <= 250:
    parcel_delivery_fee = 42

elif parcel_weight <= 500:
    parcel_delivery_fee = 52

elif parcel_weight <= 1000:
    parcel_delivery_fee = 67

elif parcel_weight <= 1500:
    parcel_delivery_fee = 82

elif parcel_weight <= 2000:
    parcel_delivery_fee = 97

else:
    print("Parcel weight is too heavy.")

print(parcel_delivery_fee)
