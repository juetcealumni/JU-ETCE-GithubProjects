from flask import Flask,render_template
import requests
import json
app = Flask(__name__,static_url_path='/static')

@app.route('/')
def Github():
   json_data=requests.get('https://api.github.com/orgs/juetcefreshers/repos')
   data=json.loads(json_data.content)
   context=[]
   for i in range(len(data)):
        context.append({
           'id':i,
           'name':data[i]['name'],
           'url':data[i]['html_url'],
           'desc':data[i]['description'],
           'lang':data[i]['language'],
           'fork':data[i]['forks'],
           'star':data[i]['stargazers_count'],
           'license': data[i]['license'] if data[i]['license']==None else data[i]['license']['name'],
           })
        
   return render_template('index.html',context=context)

if __name__=='__main__':
    app.run(debug=True)