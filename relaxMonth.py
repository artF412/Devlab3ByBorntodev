price = int(input("ราคาสินค้า : "))
dow = int(input("เงินดาวน์ : "))
month = int(input("เงินที่ผ่อนต่อเดือน : "))
priceInMonth = (price - dow)/month
print(priceInMonth)