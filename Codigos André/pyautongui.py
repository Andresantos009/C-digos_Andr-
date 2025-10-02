import pyautogui as aut
import time

#pressiono a tecla de atalho Win + r


#escreve no notpad
#--------aut.write('notepad', interval=0.3)
aut.hotkey('win')
aut.sleep(1)

# Digita o nome do navegador (por exemplo, "chrome") e pressiona Enter
# Aguarda o navegador abrir

# Digita diretamente a URL do vídeo no YouTube
aut.write('https://youtu.be/8EN4qQIIvt8?si=Nx_ML9YntU3Gobol', interval=0.1)
aut.press('enter')
time.sleep(2)  # Aguarda o vídeo carregar

# Pressiona 'f' para tela cheia
aut.press('f')

aut.sleep(20)

aut.hotkey('Esc')

#----------------------
aut.hotkey('win')

#espera 1 segundo
aut.sleep(1)

aut.write('chrome', interval=0.1)
aut.press('enter')
time.sleep(1)  

aut.press('enter')
time.sleep(1) 

aut.write('https://classroom.google.com/c/NzAwNTU0Njc2MzY3', interval=0.1)
aut.press('enter')
time.sleep(3)  

#-------------aut.mouseInfo()

aut.moveTo(1008, 743)
aut.click()
aut.sleep(1)

aut.moveTo(1590, 363)
aut.click()
aut.sleep(1)

aut.moveTo(945, 609)
aut.click()
aut.sleep(1)

aut.moveTo(1056, 1053)
aut.click()
aut.sleep(3)

aut.moveTo(566, 708)
aut.click()
aut.sleep(3)

aut.moveTo(790, 601)
aut.click()
aut.sleep(1)
aut.hotkey('ctrl', 'x')

aut.moveTo(556, 667)
aut.click()
aut.sleep(1)

aut.moveTo(778, 569)
aut.click()
aut.click()
aut.sleep(1)
aut.hotkey('ctrl', 'x')

aut.moveTo(1592, 401)
aut.click()
aut.sleep(1)

aut.hotkey('win')
aut.write('cmd')
aut.press('enter')
time.sleep(1)

aut.write('code .')
aut.press('enter')
time.sleep(1)