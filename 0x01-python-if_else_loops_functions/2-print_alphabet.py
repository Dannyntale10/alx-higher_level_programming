#!/usr/bin/python3
for alpha_letters in range(97, 122):
    if alpha_letters == ord('e') | alpha_letters == ord('q'):
        continue
    print("{:c}".format(alpha_letters), end ="")
