from selenium import webdriver
from time import sleep
import pyautogui as pag
import os


def getfiles(path,max):
	files = os.listdir(f'C:\\Users\\Levi Ricardo\\Documents\\Livros\\HQs\\{path}')
	missing = []
	for i in range(1,max+1):
		if f'{i}.zip' in files:
			continue
		else:
			missing.append(i)

	return missing




pag.FAILSAFE = False

path = 'Gambit\\Excalibur'
link = 's2/excalibur-2019'
last = 4
modo = int(input('1 para serial e 2 para checagem\n'))	#1 é download serial e 2 é download de checagem



if modo == 1:

	cap = 1
	URL = 'https://google.com'
	folder = webdriver.ChromeOptions()
	folder.add_experimental_option('prefs',{'download.default_dihttps://www.zipcomic.com/storage/s2/deadpool-v-gambit/3.ziprectory':f'C:\\Users\\Levi Ricardo\\Documents\\Livros\\HQs\\{path}'})
	driver = webdriver.Chrome(chrome_options = folder)
	driver.get(URL)
	while cap <= last:
		pag.hotkey('f6')
		URL = f'https://www.zipcomic.com/storage/{link}/{cap}.zip'
		sleep(5)
		pag.typewrite(URL)
		sleep(5)
		pag.hotkey('enter')
		sleep(15)
		cap += 1


if modo == 2:

	cap = getfiles(path,last)
	if not cap:
		print('Files list is complete')
		raise SystemExit(0)

	print(f'{cap} Missing before check')
	URL = 'https://google.com'
	folder = webdriver.ChromeOptions()
	folder.add_experimental_option('prefs',{'download.default_directory':f'C:\\Users\\Levi Ricardo\\Documents\\Livros\\HQs\\{path}'})
	driver = webdriver.Chrome(chrome_options = folder)
	driver.get(URL)
	for i in cap:
		pag.hotkey('f6')
		URL = f'https://www.zipcomic.com/storage/{link}/{i}.zip'
		sleep(5)
		pag.typewrite(URL)
		sleep(5)
		pag.hotkey('enter')
		sleep(15)

