import json

class contact:

   #Initialises class attributes
   def __init__(self,firstName,surname,address,phoneNumber,birthday):
      self.firstName = firstName
      self.surname = surname
      self.address = address
      self.phoneNumber = phoneNumber
      self.birthday = birthday
      
   #Runs at program startup and loads the entries from the file
   def setup():
      f = open("Contacts.txt","r")
      entries = json.loads(f.read())
      f.close()
   
      contactList = []

      for e in range(len(entries)):
        
         newContact = contact(
            entries[e]["firstName"],
            entries[e]["surname"],
            entries[e]["address"],
            entries[e]["phoneNumber"],
            entries[e]["birthday"] 
            )
         
         contactList.append(newContact)
         
      return(contactList)

   #Writes contacts to the file in JSON
   def write():
      f = open("Contacts.txt","w")
      f.write(json.dumps(contactList, default=lambda o: o.__dict__, sort_keys=True, indent=4))
         
      f.close()

   #Serves as a main menu and asks the user what they want to do
   def choose():
      choice = input("\nRetrieve details or Search contacts or Quit program?\nEnter read or find or quit: ").lower()
      if choice == "read":
         contact.read()
      elif choice == "find":
         contact.search()
      elif choice == "quit":
         quit()
         
      else:
         print("Invalid command")
         contact.choose()
         
   #Reads the contacts 
   def read():
      for i in range(len(contactList)):
         entry = contactList[i]

         print("\nName: " + entry.firstName + " " + entry.surname + "\nAddress: " + entry.address + "\nTel: "
               + entry.phoneNumber +"\nDOB: " + entry.birthday)
         
      contact.choose()
      
   #Searches for the inputted value and changes the contact values
   def search():
      search = input("What would you like to search for? ").lower()
      matches = []
      
      for entry in contactList:
         found = False
        
         if search in entry.firstName.lower() or search in entry.surname.lower() or search in entry.address.lower() or search in entry.phoneNumber.lower() or search in entry.birthday.lower():
            found = True

         if found:
            matches.append(entry)
            

      for m in range(len(matches)):
         print("\n==== MATCH #"+ str(m+1) +" of "+ str(len(matches)) +"====")
         entry = matches[m]
         print("\nName: " + entry.firstName + " " + entry.surname + "\nAddress: " + entry.address + "\nTel: "
               + entry.phoneNumber +"\nDOB: " + entry.birthday)

      if len(matches) > 0:
         change = input("\nWould you like to change anything?\nEnter yes or no: ").lower()

         if change == "yes":
            index = 0
            if len(matches) > 1:
               pendingInput = True
               while pendingInput:
                  try:
                     index = int(input("Which match would you like to change? "))-1
                     if index >= 0 and index < len(matches):
                        pendingInput = False
                  except:
                     print("Enter a number: ")
                     
                  
                     
                  

            if index >= 0 and index < len(matches):
               print("Type new values or press Enter to skip.")
               answer = input("Change first name ("+ matches[index].firstName +") to: ")
               if(answer != ""):
                  matches[index].firstName = answer.title()
                  print(matches[index].firstName)

               answer = input("Change surname ("+ matches[index].surname +") to: ")
               if(answer != ""):
                  matches[index].surname = answer.title()
                  print(matches[index].surname)

               answer = input("Change address ("+ matches[index].address +") to: ")
               if(answer != ""):
                  matches[index].address = answer
                  print(matches[index].address)
                  
               answer = input("Change phoneNumber ("+ matches[index].phoneNumber +") to: ")
               if(answer != ""):
                  matches[index].phoneNumber = answer
                  print(matches[index].phoneNumber)
                  
               answer = input("Change birthday ("+ matches[index].birthday +") to: ")
               if(answer != ""):
                  matches[index].bjrthday = answer
                  print(matches[index].birthday)

               contact.write()
               contact.choose()
            else:
               print ("That is not a contact #.")
               
            
         
         else:
            contact.choose()

      else:
         print("No matches found")
         contact.choose()

      
      
         
contactList = contact.setup()

contact.choose()
