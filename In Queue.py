def diff_count(list_all):
	for i in list_all:
		print(i)
		if i == 'g' or i == 'G':
			g_count = g_count + 1
		elif i == 'l' or i == 'L':
			l_count = l_count + 1

g_count = 0
l_count = 0
diff_count("GLGLGL")
print('G' * g_count)

