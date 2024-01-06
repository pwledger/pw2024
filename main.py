name = input("github 아이디 입력 : ")
mail = input("github 이메일 입력 하시오 : ")

if name and mail :
    f=open("참여명단.txt","a")
    f.write(f"name : {name} , mail : {mail}")
    f.close()
