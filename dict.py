marks = {"name":"ajit",
          "age":20,
         "mark":[12,30,40,50],
         "sub":(50,40,60,80),
         "address":{"village":"kasegaon","pin":413304}
        }
print(marks.values())
print(marks.keys())
print(marks.items())
print(marks.update({"ajit":30}))
print(marks.get("ajit"))
marks.popitem()
print("dict is")
print(marks)