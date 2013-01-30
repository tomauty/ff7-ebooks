#Full script with annotations
full = open('ff7.txt','r')
fullstr = full.read()
#New file with just quotes, easier to select at random
new = open('ff7quotes.txt','w')

#Find quotes
charnum = 0
start = False
end = False
for line in fullstr:
	charnum += 1
	if start is False:
		if line is '"':
			qtstart = charnum
			start = True
	else:
		if line is '"':
			qtend = charnum
			end = True
	if start is True and end is True:
		new.write(fullstr[qtstart:qtend-1])
		new.write('\n')
		start = False
		end = False

