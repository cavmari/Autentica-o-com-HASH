import hashlib
import itertools
import time

def brute_force_md5(hash_to_crack, charset, max_length):
    start_time = time.time()
    for length in range(1, max_length + 1):
        for guess in itertools.product(charset, repeat=length):
            guess = ''.join(guess)
            if hashlib.md5(guess.encode()).hexdigest() == hash_to_crack:
                end_time = time.time()
                return guess, end_time - start_time

hashes = ["81dc9bdb52d04dc20036dbd8313ed055", "eccbc87e4b5ce2fe28308fd9f2a7baf3", "a87ff679a2f3e71d9181a67b7542122c", "c4ca4238a0b923820dcc509a6f75849b"]
for hash_to_crack in hashes:
    cracked_password, time_taken = brute_force_md5(hash_to_crack, charset="0123456789", max_length=4)
    print(f"Hash: {hash_to_crack}, Senha: {cracked_password}, Tempo: {time_taken} segundos")
