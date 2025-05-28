class Marry:
    def engagementDate(self):
        print("Engagement will be done on 23 Dec.")

 # Overridden method
    def marryDate(self):
        print("Marry will be on 29 Dec")

class Change(Marry):
 # Overriding method
    def marryDate(self):
        print("Marry will be on 01 Jan")

# Create an instance of subclass Change.
obj = Change()

# Call methods of subclass. 
obj.engagementDate()
obj.marryDate()
