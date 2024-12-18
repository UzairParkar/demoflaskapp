from flask import Flask,request,jsonify

app = Flask(__name__)
'''
For this App i have used the
datastructures in python as a database 
and will be tesing the api using Postman
'''
db = [{ 
    'id':1,
    'emp_id':2024000001,
    'name':'Mark',
    'surname':'Zukerberg',
    'email':'Zucked@hotmail.com',
    'age':45,
    'salary':30000

},{
    'id':2,
    'emp_id':2024000002,
    'name':'Barry',
    'surname':'Allen',
    'email':'Barry.Exmp@gmail.com',
    'age':28,
    'salary':500000
},
{
    'id':3,
    'emp_id':2024000003,
    'name':'Rahul',
    'surname':'Sharma',
    'email':'Sharma.Rahul@hotmail.com',
    'age':21,
    'salary':3000
}]

@app.route('/')
def home():
    return '''<h1>Hello Programmer, lets get some bugs</h1>
    <p>This is a demo flask application built using Flask and it uses postman as its frontend</p> 
    '''
#to view all the data or read
@app.route('/r',methods=['GET'])
def read_all():
    return jsonify(db),200

#to view all the data by using the ids of the employees
@app.route('/r/<int:id>',methods=['GET'])
def read_by_id(id):
    for existing_id in db:
        if id == existing_id['id']:
            return jsonify(existing_id),201

#read by employee id
@app.route('/r/e/<int:emp_id>',methods=['GET'])
def read_by_emp_id(emp_id):
    for exemp_id in db:
        if emp_id == exemp_id['emp_id']:
            return jsonify(exemp_id),202
        
#Creating more employees
@app.route('/c/e',methods=['POST'])
def add_emp():
    new_emp = request.json
    new_id = len(db)+1
    new_emp_id = 202400000 + len(db) + 1
    emp = {
        'id':new_id,
        'emp_id':new_emp_id,
        'name':new_emp['name'],
        'surname':new_emp['surname'],
        'email':new_emp['email'],
        'age':new_emp['age'],
        'salary':new_emp['salary']
    }
    db.append(emp)
    return jsonify(emp),203

#Update existing employees
@app.route('/u/e/<int:id>',methods=['PUT'])
def update_emp(id):
    for old_id in db:
        if old_id['id'] == id:
            old_id['emp_id'] = old_id['emp_id']
            old_id['name'] = request.json.get('name',old_id['name'])
            old_id['surname'] =  request.json.get('surname',old_id['surname'])
            old_id['email'] =  request.json.get('email',old_id['email'])
            old_id['age'] =  request.json.get('age',old_id['age'])
            old_id['salary'] = request.json.get('salary',old_id['salary'])
            return jsonify(old_id),204

#Firing Employees   
@app.route('/d/e/<int:id>',methods=['DELETE'])
def firing_employees(id):
    for old_id in db:
        if old_id['id'] == id:
            db.remove(old_id)
            return jsonify({"notification":f'The Employee {id}has been fired'}),200


if __name__ == '__main__':
    app.run(debug=False)
