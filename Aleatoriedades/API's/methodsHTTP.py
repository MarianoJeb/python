import requests
import pprint
url="https://learn-http-f798a-default-rtdb.firebaseio.com/.json"
##Get
requisicao=requests.get(url)
pprint.pprint(requisicao.json())

##Post
pessoa={"nome": "Rogério", "idade": 20}
#posting=requests.post(url, json=pessoa)

##json=(dicionario normal)
##data=(dicionario entre parenteses)


#Patch
pathPessoa={"idade": 23, "sobrenome":"Ronaldo"}
#posting=requests.patch("https://learn-http-f798a-default-rtdb.firebaseio.com/-OkEPET4kQ4OT10gMVvJ.json",json=pathPessoa)

#Delete
requests.delete("https://learn-http-f798a-default-rtdb.firebaseio.com/-OkEQjwdCkT3Kh_B3DjH.json")
requests.delete("https://learn-http-f798a-default-rtdb.firebaseio.com/-OkEQvh0yXdQRbNRpRoj.json")
requests.delete("https://learn-http-f798a-default-rtdb.firebaseio.com/-OkER4eWZ3AlknNtsLSz.json")