unit_price = float(input("Enter unit price: "))
quantity = int(input("Enter quantity: "))
GST = 0.07

subtotal = unit_price * quantity
gst_price = subtotal * GST
final = subtotal + gst_price

print(f"Subtotal: {subtotal}\nGST: {gst_price}\nTotal: {final}")