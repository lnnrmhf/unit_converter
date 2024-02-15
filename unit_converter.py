import sys
import math

print(f"The value to be converted is: {sys.argv[1]}")
print(f"The unit of the value is: {sys.argv[2]}")
print(f"The unit of the value should be: {sys.argv[3]}")

sys.argv[1] = float(sys.argv[1])

if sys.argv[2] == "m" and sys.argv[3] == "au":
    m_to_au = sys.argv[1]/(1.496*10**11)
    print(f"Converted value: {m_to_au}")

elif sys.argv[2] == "m" and sys.argv[3] == "pc":
    m_to_pc = sys.argv[1]/(3.086*10**16)
    print(f"Converted value: {m_to_pc}")

elif sys.argv[2] == "au" and sys.argv[3] == "m":
    au_to_m = sys.argv[1]*1.496*10**11
    print(f"Converted value: {au_to_m}")

elif sys.argv[2] == "au" and sys.argv[3] == "pc":
    au_to_pc = sys.argv[1]*4.848*10**-6
    print(f"Converted value: {au_to_pc}")

elif sys.argv[2] == "pc" and sys.argv[3] == "m":
    pc_to_m = sys.argv[1]*3.086*10**16
    print(f"Converted value: {pc_to_m}")

elif sys.argv[2] == "pc" and sys.argv[3] == "au":
    pc_to_au = sys.argv[1]/4.848*10**-6
    print(f"Converted value: {pc_to_au}")

else:
    print("Sorry, invalid input. Please use m, au or pc.")

