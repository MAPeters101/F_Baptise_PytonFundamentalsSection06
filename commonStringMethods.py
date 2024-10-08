message = "The definitive guide to Python"
print(message.upper())
print(message.lower())
print(message)
print(message.title())

print('abc' == 'ABC')
print('aBc'.lower() == 'AbC'.lower())

l = '\u03b1'
u = '\u0391'

print(l, u)
print(l == u)

print(l.lower() == u.lower())

a = '🐍'
print(a.lower() == a.upper())

print(l.casefold(), u.casefold(), l.casefold() == u.casefold())

street = 'stra\N{LATIN SMALL LETTER SHARP S}e'
print(street)
print(street.upper())
print(len(street), len(street.upper()))

data = 'STRASSE'
print(data == street)
print(data.lower(), data.lower() == street)
print(data.lower(), street)
print(data.casefold(), street.casefold())
print(data.casefold() == street.casefold())



