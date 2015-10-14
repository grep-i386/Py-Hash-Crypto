#!/usr/bin/python
#coding: utf-8
# Распространяется согласно GNU/GPL v2
# Автор - grep<dot>i386<at>yandex<dot>com
import random,hashlib

# Пример хэш-шифрования - создание шифротекста
# Создаёт 3 хэша с рандомным сообщением от 0 до 1000000

SHARED_SECRET="b5d695df31349a773e23d3587a5bdcf1" #ключ шифрования

for a in range(0,3):
	print hashlib.sha256(SHARED_SECRET+hashlib.sha256(str(random.randint(0,1000000))).hexdigest()).hexdigest()
#генерируем шифротекст по алгоритму: sha256(KEY+sha256(text))
