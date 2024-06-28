def generate_secret_code(message):
    code_mapping={
        'a':'!','b':'@','c':'#','d':'$','e':'%',
        'f':'^','g':'&','h':'*','i':'(','j':')',
        'k':'-','l':'+','m':'=','n':'[','o':']',
        'p':'{','q':'}','r':';','s':':','t':'<',
        'u':'>','v':',','W':'.','x':'/','y':'?',
        'z':'~','':'_'
        }
    secret_code=''
    for char in message.lower():
          secret_code+=code_mapping.get(char,char)
    return secret_code
def main():
    message=input("enter the message to generate the secret code:")
    secret_code=generate_secret_code(message)
    print("\nGenerated Secret Code:",secret_code)
if __name__=="__main__":
  main()
