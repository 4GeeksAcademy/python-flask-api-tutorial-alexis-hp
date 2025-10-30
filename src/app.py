from flask import Flask,jsonify,request
app = Flask(__name__)

todos =[{ "label": "My first task", "done": False, "position": 1}]

position_counter = 2

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    global position_counter
    data = request.get_json()
    new_todo ={
        "position": position_counter,
        "label": data["label"],
        "done": data["done"],   
    }
    todos.append(new_todo)
    position_counter +=1
    print("Incoming request with the following body", data)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    for todo in todos:
        if todo["position"] == position:
            todos.remove(todo)
   
    print("This is the position to delete:", position)
    return jsonify(todos)    

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
