from time import sleep

your_name = "Nguyễn Huỳnh Anh Khoa"
your_great = "Xin chào mọi người! mình là "

for c in your_great + your_name:
    print(c, end='', flush=True)
    sleep(0.05)
print()

