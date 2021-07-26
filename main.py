import random
n = int(input("enter the length of the password you want : "))
low = "abcdefghijklmnopqrstuvwxyz"
high = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
dig = "1234567890"
sym = "!@#$%^&*(){}|:<>?/"
all_s = low+high+dig+sym
passwd = "".join(random.sample(all_s, n))
print("suggested password : ", passwd)
