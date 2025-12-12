def input_int(p):
    while True:
        try: return int(input(p))
        except: print('Input harus angka!')
