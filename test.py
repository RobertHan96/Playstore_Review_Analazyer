import uuid

file_name = 'trending_pie_chart'
def make_uuid():
    return str(uuid.uuid4())

tt = make_uuid()
tt2 = make_uuid()
t1 = "{}-{}".format(make_uuid(), file_name)
t2 = "{}-{}".format(tt2, file_name)
print(t1)
print(t2)
