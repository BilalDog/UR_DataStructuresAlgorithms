from collections import deque

#stack practical 1
UR = []
for i in range (3):
    UR.append(f"Lab{i+1}")
UR.pop()
print(f"\nstack practival 1: {UR[-1]}")

#stack practical2
irembo = ["Upload", "Fill Form", "Confirm"]
irembo.pop()
irembo.pop()
print(f"\nstack practical 2: {irembo}")

#stack chanllange1
stack =[]
for i in range (4):
    stack.append(i+1)
for j in range (3):
    stack.pop()
stack.append(5)
print(f"Stack challange1: {stack[-1]}")

print("\nReflection Stack:"
"\nStack is perfect for undo/redo because of LIFO - you always want to undo the most recent action first." \
"\nIt is exactly what popping from a stack does. " \
"\nEach action gets pushed on top, and undo simply pops the top action to reverse it in the correct order.")

#queue practical1
clients = deque()
for j in range (12):
    clients.append(f"client{j+1}")
for i in range (5):
    i+=1
    clients.popleft()
print(f"\nQueue practical1: {clients[0]}")

#queue practical 2
patients = deque()
for k in range (8):
    patients.append(f"patient{k+1}")
print(f"\nQueue practical2: {patients[-1]}")

fans = []
for i in range (5):
    fans.append(f"fan {i+1}")

#challange queue
print("\nchallange queue:")
stack = []
queue = deque()

for fan in fans:
    stack.append(fan)
print("Stack order entering th stadium:")
while stack:
    fan = stack.pop()
    print(fan)

for fan in fans:
    queue.append(fan)
print("\nQueue order of recieving books:")
while queue:
    fan = queue.popleft()
    print(fan)

print("\nReflection Queue" \
"\nRespects arrival order: fans who arrive first enter first"\
"\n-Prevents queue-jumping: No one can skip ahead"\
"\n-Predictable waiting: fans know their position in line"\
"\n-Equal treatment: Everyone follows same rule")
