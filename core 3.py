def decimal_to_binary(n):
    if n == 0:
        return "0"
    
    binary_str=""
    while n > 0:
        binary = n % 2
        binary_str = str(binary) + binary_str
        n = n//2
        
    return binary_str
    


n=int(input("n sonini kiriting: ")) # 23
natija=decimal_to_binary(n)
print("Natija: ",natija)
