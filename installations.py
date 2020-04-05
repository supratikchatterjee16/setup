import pip
import sys
import subprocess

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

def install(item_list):
	#Refer https://pip.pypa.io/en/latest/user_guide/#using-pip-from-your-program
	try:
		installed_file = open('installed.txt','r')
		installed_list = installed_file.read().split('\n')
		item_list = [x for x in item_list if x not in installed_list]
	except Exception as e:
		print(e)
	
	for item in item_list:
		print('Attempting install of {}'.format(item))
		output = 0
		try:
			output = subprocess.run([sys.executable, '-m', 'pip', 'install', item], capture_output=True, check=True)
			if output.returncode==0:
				print(str(output.stdout, 'utf-8'))
				print('Completed Installation of {}'.format(item))
				with open('installed.txt', 'a') as installed_list:
					installed_list.write(item+'\n')
			else:
				print('Failure while installing {}'.format(item))
				print(str(output.stderr, 'utf-8'))
				break
		except Exception as e:
			print(e)

if __name__ == '__main__':
	with open('requirements.txt', 'r') as requirements_list:
		items_list = requirements_list.read().split('\n')
		install(items_list)
		import nltk
		nltk.download('all') 
 
