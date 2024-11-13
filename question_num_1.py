#START NUMBER 1
friend_Dani: int = int(input("How many friends came?"))
pizza_triangles: int = int(input("How many pizza triangles are there?"))

calculation: int = pizza_triangles // friend_Dani
rest: int = pizza_triangles % friend_Dani

print(f"For {pizza_triangles} pizza triangles. Each member got {calculation} triangle and {rest} remained")

#END

#START NUMBER 2

a = 1
b = 1
if a == b:
    print(f"was True for {a} {b}")
else:
    print(f"was False for {a} {b}")

a = 1
b = 0
if a == b:
    print(f"was True for {a} {b}")
else:
    print(f"was False for {a} {b}")

a = 2
b = 2
c = 2
d = 2
if a + b and c + d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

a = 0
b = 0
c = 0
d = 0
if a + b and c + d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

a = 5
b = 0
c = 5
d = 0
if a >= b or c > d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

a = -3
b = 0
c = 0
d = 0
if a >= b or c < d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

a = 2
b = 2
c = 3
d = 3
if a == b and c <= d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

a = 2
b = 2
c = 4
d = 3
if a == b and c <= d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

a = 0
b = 5
c = 3
d = 0
if True and a + b + c + d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

a = 0
b = 0
c = 0
d = 0
if True and a + b + c + d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

a = 0
b = 5
if a != b:
    print(f"was True for {a} {b}")
else:
    print(f"was False for {a} {b}")

a = 0
b = 0
if a != b:
    print(f"was True for {a} {b}")
else:
    print(f"was False for {a} {b}")

a = 4
b = 3
c = 2
if a != b and a <= c or a <= b or True:
    print(f"was True for {a} {b} {c}")
else:
    print(f"was False for {a} {b} {c}")

a = 3
b = 3
c = 0
if a != b and a <= c or a <= b or False:
    print(f"was True for {a} {b} {c}")
else:
    print(f"was False for {a} {b} {c}")

a = 3
b = 3
c = 4
d = 3
if a % b == 0 and c % d == 1:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

a = 3
b = 5
c = 4
d = 3
if a % b == 0 and c % d == 1:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

#END

#START NUMBER 3

# if 4 < 9: True
# if (2*3+4) * (7+7): True
# if 18 + 18: True
# if 10 == 10: True
# if 10 == 10 and 20 == 30: False
# if 10 == 10 or 20 == 30: True
# if 20 == 30 or 10 == 10: True
# if not 3: False
# if 3: True
# if (33 > 20) and (2 < 12) and 10: True
# if True and True: True
# if True and False: False
# if True or False: True
# if False or True: True
# if (not 10) and 10: False
# if (not 10) and (not 10): False
# if 5 != 5 and 5 == 5: False
# if 2 == 2 or 3 == 3: True
# if  2 == 2 and 3 == 3: True
# if 40 == 30 and 1 >= 4: False
# if 13 >= 3 or 47 >= 5: True

#END

for a in range(10, 20+1):
    print(a, end=", ")

for b in range(10, 20+1, 2):
    print(b, end=", ")

gap: int = int(input("Please  enter a gap"))
for i in range(10, 20+1, gap):
    print(i, end=", ")