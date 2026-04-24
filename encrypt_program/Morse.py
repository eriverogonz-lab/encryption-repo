# usando ., _ , tres espacios entre palabras y uno entre letras
def morse_decryption(txt):
  txt=txt+" "
  alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0', '1', '2', '3','4', '5', '6','7','8','9']
  morse_alphabet = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-', '..-','...-','.--','-..-','-.--','--..', '-----', '.----', '..---', '...--','....-', '.....',  '-....', '--...','---..','----.']
  letter= ""
  word= ""
  final_txt=""
  number_spaces=0
  
  for x in txt:
    if x != " ":
      letter=letter +x
      number_spaces=0
      
    else:
      number_spaces=number_spaces+1
      if number_spaces ==3:
        final_txt=final_txt+" "
      elif number_spaces==1:
        for j in range(len(morse_alphabet)):
          if letter == morse_alphabet[j]:
            final_txt= final_txt+alphabet[j]
            letter=""
  return final_txt



def morse_encryption(txt):
  final_txt=""
  number_spaces =0
  txt=txt.upper()
  alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0', '1', '2', '3','4', '5', '6','7','8','9']
  morse_alphabet = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-', '..-','...-','.--','-..-','-.--','--..', '-----', '.----', '..---', '...--','....-', '.....',  '-....', '--...','---..','----.']
  for x in txt:
    if x==" ":
      final_txt = final_txt +"  "
    else:
      for i in range(len(alphabet)):
        if x==alphabet[i]:
          final_txt= final_txt+morse_alphabet[i]+" "
  return final_txt 


