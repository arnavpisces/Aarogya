import pygeoj, xlrd
loc=("clinics.xlsx")
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
names=[]
long=[]
lat=[]
for i in range(50):
    names.append(str(sheet.cell_value(i,0)))
    long.append(float(sheet.cell_value(i,2)))
    lat.append(float(sheet.cell_value(i,1)))
print(names, lat, long)
# testfile.pygeoj.new()
testfile=pygeoj.load(filepath="download.json")
# print len(testfile)
# for feature in testfile:
    # print feature
docid={}
for i in range(50):
    docid['doc'+str(i)]=names[i]
    testfile.add_feature(properties={"name":names[i]},
                         geometry={"type":"Point","coordinates":[long[i],lat[i]]})
# # testfile.add_feature(properties={"name":"Norway"},
#                     # geometry={"type":"Point", "coordinates":[a,b]} )
testfile.add_all_bboxes()
testfile.update_bbox()
testfile.save("download.json")