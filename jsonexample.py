import json
print("this is python operation")

jasonuser = '''{
  "name":"ajit",
  "age":23,
  "address":"kasegaon" 
}'''

jsondemo = json.loads(jasonuser)
print(type(jasonuser))
first_dict = {
  "name":"py dict",
  "first":"py example json"
}
dictdemo = json.dumps(first_dict)
print(dictdemo)
print(type(dictdemo))

