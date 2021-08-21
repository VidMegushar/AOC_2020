subject_num = 7
start_val = 1
divider = 20201227
loop_size = 10


def get_loop_size(public_key, subject_num, tmp_num):
    loop_size = 1
    while True:
        tmp_num = (tmp_num*subject_num) % divider
        if tmp_num == public_key:
            return loop_size
        loop_size += 1

def transform_key(pk, loop_size):
    enc_key = 1
    for _ in range(loop_size):
        enc_key = (enc_key*pk) % divider
    return enc_key


card_public = 19241437
door_public = 17346587

card_loop_size = get_loop_size(card_public, 7, start_val)

print(transform_key(door_public, card_loop_size))

