#%%
class MyClass1:
    """A simple example class"""
    i = 12345
    def f(self):
        return 'hello world'

#%%
aClass = MyClass1()
print(aClass.f())
bClass = MyClass2()
print(bClass.f())
#%%
class MyClass2:
    """A simple example class 2"""
    i = 12345
    def __init__(self,name):
        self.name = name
    def f(self):
        return 'hello world from ' + self.name
#%%
aClass = MyClass2("John")
print(aClass.f())
bClass = MyClass2("Lucy")
print(bClass.f())

#%%
import json
data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}
#%% 
with open('out.json','w') as fh:
    json.dump(data, fh)

#%%
# Importing data from a json file:
with open('out.json', 'r') as nfh:
    obj = json.load(nfh)
    print(obj)
    print(obj["president"]["name"])

#%%
from PIL import Image
#%%
mode = 'RGBA'
size = (100, 100)
color = (100,255,100,255)
ourimage = Image.new(mode, size, color)
ourimage
#%%
for x in range(ourimage.size[0]):
    for y in range(ourimage.size[1]):
        value = float(x)/ourimage.size[0]
        value = int(value*255.0)
        ourimage.putpixel((x,y),(value,value,value,255))
ourimage
#%%
ourimage.getpixel((59,50))
#%%
ourimage.save('allblack.png')
#%%
