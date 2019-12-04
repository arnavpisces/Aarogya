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
# print(names, lat, long)
docid={}
for i in range(50):
    docid['doc'+str(i)]=[names[i],long[i],lat[i]]
print(docid)