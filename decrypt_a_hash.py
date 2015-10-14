#!/usr/bin/python
#coding: utf-8
# Распространяется согласно GNU/GPL v2
# Автор - grep<dot>i386<at>yandex<dot>com
import random,hashlib

# расшифровка: перебор "зашифрованных" номеров при известном ключе

SHARED_SECRET="b5d695df31349a773e23d3587a5bdcf1" #ключ шифрования
CIPHER = str(raw_input("ШИФР: "))

for n in range(0,1000001): # просто перебираем
	Nhash = hashlib.sha256(str(n)).hexdigest()
	NShash = hashlib.sha256(SHARED_SECRET+Nhash).hexdigest()
	if NShash == CIPHER:
		print "РАСШИФРОВАННО:",n
		break
