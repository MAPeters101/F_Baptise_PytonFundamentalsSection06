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

s1 = '\N{LATIN SMALL LETTER E WITH CIRCUMFLEX}'
s2 = '\N{LATIN SMALL LETTER E}\N{COMBINING CIRCUMFLEX ACCENT}'
print(s1, s2)
print(s1 == s2)
print(s1.upper() == s2.upper())
print(s1.casefold() == s2.casefold())

#  ========== Stripping ==========
name = 'Peter '
print(f'|{name}|')
print(f'|{name.rstrip(' ')}|')


name = '\t Peter\tJones\t '
print(f'|{name}|')
print(f'|{name.strip(' ')}|')
print(f'|{name.strip()}|')

name = 'ababPYTHONabab'
print(f'|{name}|')
print(f'|{name.strip(' ')}|')
print(f'|{name.strip('ab')}|')






