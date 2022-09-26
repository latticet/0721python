import re

# TODO ^
print(re.search('^he', 'hello'))
print(re.search('^he', 'lhello'))

# TODO $
print(re.search('good$', 'good'))
print(re.search('good$', 'xxxgood'))
print(re.search('good$', 'xfdsfsdgood'))

# TODO ^ $
print(re.search('^h\w{3}o$', 'hello'))
print(re.search('^h\w{3}o$', 'habco'))

print(re.search('^h\w{3}o$', 'habco1'))
print(re.search('^h\w{3}o$', 'fhabco'))

