# Width and Multiline

# Data

data_nama  = "ucup surucup"
data_umur = 17
data_tinggi = 150.1
data_ukuran_sepatu = 44

# string standard
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, sepatu = {data_ukuran_sepatu}"
print(5*"="+"Data String"+5*"=")
print(data_string)

# String Multiline (dengan menggunakan enter, newline, \n)
data_string = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nsepatu = {data_ukuran_sepatu}"
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)

# String multiline (kutip triplets)
data_string = f"""nama = {data_nama} 
umur = {data_umur} 
tinggi = {data_tinggi} 
sepatu = {data_ukuran_sepatu}
"""
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)

# Mengatur Lebar
data_nama = "Ucup"
data_string = f"""
nama = {data_nama:>5} 
umur = {data_umur:>5} 
tinggi = {data_tinggi:>5} 
sepatu = {data_ukuran_sepatu:>5}
"""
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)









