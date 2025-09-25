from flask import Flask, render_template, request, josonify, redirect, url_for
from datetime import datetime
import json
import resend

#adicionamos a chave da API para para
resend.api_key="09876159-b0fd-4685-9d35-dd970e8ba31d"

app= Flask(__name__)

with open("dados.json", "r", encoding='utf-8') as arquivo:
    dados=json.load(arquivo)
@app.route("/", methods=['POST', 'GET'])
def index():
        if request.method == 'POST':
              nome= request.form['name']
              email=request.form['email'] 
              mensagem=request.form['message']

              # montar o dicionario da nova menssagem
              dados_mensagem={
                    'nome':nome,
                    'email':email,
                    'mensagem':mensagem,
                    'data':f'{datetime.today()}'
              }
#adicionar e salvar no jso.
        dados.append(dados_mensagem)
        with open('dados.json', 'w', encoding='utf-8') as arquivo:
              json.dump(dados, arquivo, indent=4, ensure_ascii=False)


#envisa email.
              r=resend.Email.send({
                  'from':'onboarding@resend.dev',
                    'to':"aulaspython2025@gmail.com",
                    "subject": f"solicitaçãode adoção{nome}"
                    "html":f"<p>Email:{email}<br>{mensagem}</p>"
                    })
        
        return redirect(url_for('index.html'))
        return render_template('index.html')


if __name__ =='__main__':
      app.run(debug=True)