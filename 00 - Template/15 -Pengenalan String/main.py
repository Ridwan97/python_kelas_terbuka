data = "ini adalah string"
print(data)
print(type(data))

# 1. cara membuat string

'''
    1. dengan menggunakan single quote '...' 
    2. dengan menggunakan double qupte "..."
'''

data = 'menggunakan single quote'
print(data)

data = "menggaunakan double quote"
print(data)

print('"Halo, apa Kabar?"')
print("'Halo, apa kabar?'")
print("ini adalah hari juma`t")

# 2. Menggaunakan tanda \

# membuat tanda ' menjadi string
print('mari shalat jum\'at')
print('g\'day, isn\`t it?')

#backslash
print("C:\\user\\Ucup")

# tab
print("ucup\t\t\totong, semakin jauhan")

# backspace
print("ucup \btotong, jadi deketan")

#newline
print("baris pertama, \nbaris kedua.") # LF -> Line Feed
print("baris pertama, \rbaris kedua.") # RF -> Carriage Return -> Commodore, Acorn, Lisp
print("baris pertama, \r\nbaris kedua.") # CRLF -> Linde Feed Carriage Return -> Dipakao windows

# String Literal atau raw

# hati - hati 
print('c:\new folder') # akan salah pathnya

# mengguunkan raw string
print(r'c:\new folder')

# multiline literal string
print('''
Nama : Ucup 
Kelas : 3 SD
''')

# multiline literal string dan RAW
print('''
Nama : Ucup 
Kelas : 3 SD\new normal
Website : www.ucup.com/newID
''')