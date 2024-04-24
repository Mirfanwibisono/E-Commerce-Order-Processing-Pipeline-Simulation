# Membuat class Order
class Order:
    # Membuat constructor untuk menginisialisasi  atribut
    def __init__(self, order_id, customer_name, order_date, total_amount):
        self.order_id = order_id # Atribut order_id
        self.customer_name = customer_name # Atribut nama customer
        self.order_date = order_date # Atribut tanggal order
        self.total_amount = total_amount # Atribut total harga pesanan

    # Membuat method untuk menghitung pajak dari total harga pesanan
    def calculate_tax(self, tax_rate):
        return self.total_amount * tax_rate # Mengembalikan hasil dari total harga pesanan dikali tarif pajak
    

    # Mencetak detail pesanan dari atribut 
    def display_order(self):
        print("Order ID: ", self.order_id) # Mencetak order_id
        print("Customer Name: ", self.customer_name) # Mencetak nama customer
        print("Order Date: ", self.order_date) # Mencetak tanggal order
        print("Total Amount: ", self.total_amount) # Mencetak total harga pesanan

# Membuat class OrderProcessor
class OrderProcessor:

    # Membuat constructor untuk menginisialisasi sebuah list kosong daro orders yg akan digunakan menyimpan semua pesanan
    def __init__(self):
        self.orders = []

    # Membuat method untuk menambahkan pesanan ke orders
    def add_order(self, order):
        self.orders.append(order)
    
    # Membuat method untuk menghitung semua total harga pesanan yg sudah diproses
    def calculate_total_revenue(self):
        total_revenue = sum(order.total_amount for order in self.orders)
        return total_revenue
    
    # Membuat method untuk menghitung total pajak yg harus di bayar dari semua pesanan yg sudah diproses
    def calculate_total_tax(self, tax_rate):
        total_tax = sum(order.calculate_tax(tax_rate) for order in self.orders)
        return total_tax
    
    # Mencetak semua pesanan yg sudah diproses
    def display_orders(self):
        for order in self.orders:
            order.display_order() # Memanggil method display_order dari setiap pesanan untuk menampilkan detailnya
            print()

# Membuat objek bernama order1 dan order2 dari kelas Order
order1 = Order("001", "Holmes", "2024-03-27", 54000)
order2 = Order("002", "Watson", "2024-03-28", 37000)

# Membuat objek OrderProcessor
order_processor = OrderProcessor()

# Menambahkan pesanan ke OrderProcessor
order_processor.add_order(order1)
order_processor.add_order(order2)

# Menghitung dan menampilkan total pendapatan dan total pajak
tax_rate = 0.1 # Tarif pajak sebesar 10%
total_revenue = order_processor.calculate_total_revenue()
total_tax = order_processor.calculate_total_tax(tax_rate)

print("Total Revenue: ", total_revenue) # Menampilkan total harga semua pesanan Order
print("Total Tax: ", total_tax) # Menampilkan total pajak semua pesanan Order

# Menampilkan detail dari semua pesanan
order_processor.display_orders()