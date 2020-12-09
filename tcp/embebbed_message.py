message = "hi there"

new_message = "{:<4}".format(message)

print(new_message)

print('----------------------------------')

hhh = 16
msg = "this msg from the server"
send_msg = f"{len(msg):<{hhh}}" + msg
print(send_msg)


print('--------------------------')

example = int(f"{len(msg):<{16}}".encode("UTF-8"))
print(example)