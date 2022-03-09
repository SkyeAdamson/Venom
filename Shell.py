import Run

while False:
	text = input('Venom > ')
	if text.strip() == "": continue
	result, error = Run.run('<stdin>', text)

	if error:
		print(error.as_string())
	elif result:
		if len(result.elements) == 1:
			print(repr(result.elements[0]))
		else:
			print(repr(result))

with open("example.myopl") as file:
	text = ''.join(file.readlines())
	result, error = Run.run('example.myopl', text)

	if error:
		print(error.as_string())
	elif result:
		if len(result.elements) == 1:
			print(repr(result.elements[0]))
		else:
			print(repr(result))