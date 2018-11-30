class Birds:
    def __init__(self):
        '''Constructor'''
        #Create some member of this class
        self.members = ['Sparrow' , 'Robin', 'Duck']

    def printMembers(self):
        print('Print members of the Birds class')
        for member in self.members:
            print('t\%s '%member)
