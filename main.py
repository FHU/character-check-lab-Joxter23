#Remove pass and complete the code
def check_character(word, index):
   text = word[index]
   type = ''

   if text.isalpha():
       type = 'letter'
   elif text.isspace():
       type = 'white space'
   elif text.isdigit():
       type = 'digit'
   else:
       type = 'unknown'

   return type


       

if __name__ == '__main__': 
    print(check_character('happy birthday', 2))
    print(check_character('happy birthday', 5))
    print(check_character('happy birthday 2 you', 15))
    print(check_character('happy birthday!', 14))