from flask import Flask, jsonify, request

app=Flask(__name__)
tasks=[
    {
    'id':1,
    'name':u"Raju",
    'contact': 00000000
    'done':False
},
{
  'id':2,
  'name':u"Harshil",
  'contact': 7678098898,
  'done':False  
}
]

@app.route("/add-data",methods="POST")
def add_task():
    if not request.json:
        return jsonify({
            "status":"Error"
            "Message": "Please provide the data."
        },400)
    task={
        'id':tasks[-1]['id']+1,
        'name':request.json['name'],
        'contact':request.json.get('contact')
        'done':False
    }
    tasks.append(task)
    return jsonify({
        "status":"Success",
        "Message": "Task done successfully"
    })

@app.route("get-data")
def get_tasks():
    return jsonify({
        "data": tasks
    })

if __name__=='__main__':
    app.run()