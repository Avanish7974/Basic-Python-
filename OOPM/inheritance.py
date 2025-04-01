# inheritance - this is a ability to take properties and features of one class to another class
# 1.single level
# 2. multilevel
# 3. multiple
# 4. hirerchial level
# 5. 
# the class which can inherit another class is called derived class(chiled class) 

class myclassA:
    def func1(self):
        print("This is base or parent class ")
class myclassB(myclassA):
    def func2(self):
        print("This is derived or child class ")
        
