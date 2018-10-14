from colorama import Fore, Back, Style, init


def enter():
  print("Enter/Paste your content. Ctrl-Z to save it. strings:")
  contents = []
  while True:
    try:
      line = input()
    except EOFError:
      break
    contents.append(line)
  return contents





init(autoreset=True)

s1 = enter()
s2 = enter()


if len(s1) != len(s2):
  print('Warning:len(s1) != len(s2)', len(s1), len(s2))




if len(s1) < len(s2):
  leng = len(s2)
else:
  leng = len(s1)
  
m = 65

for i in range(leng):
  if s1[i] == s2[i]:
    print(Style.BRIGHT + Fore.GREEN + s1[i]+' '*(m-len(s1[i]))+'| '+s2[i])
  else:
    print(Style.BRIGHT + Fore.GREEN + Back.RED + s1[i]+' '*(m-len(s1[i]))+'| '+s2[i])
	
	

	



