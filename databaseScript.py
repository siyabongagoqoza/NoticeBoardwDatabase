import datetime

import pyrebase

firebaseConfig = {
  'apiKey': "AIzaSyB9iup_nEv0uAuqIFp7YuamIi1r0IWte4k",
  'authDomain': "noticeboard-323c1.firebaseapp.com",
  'databaseURL': "https://noticeboard-323c1-default-rtdb.firebaseio.com/",
  'projectId': "noticeboard-323c1",
  'storageBucket': "noticeboard-323c1.appspot.com",
  'messagingSenderId': "86255604236",
  'appId': "1:86255604236:web:92e1668ccb0591b70f1429",
  'measurementId': "G-FXYR3YWF1X"
}

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()


# Add Data
wanna_add = input("Want to add an event?").lower()
if wanna_add == "yes":
  add_eventDate = input("Add Date YYYY-MM-DD")
  if not(add_eventDate is None or add_eventDate == ""):
      add_eventName = input("Add Event Name")
      if not(add_eventName is None or add_eventName == ""):
        db.child('Events').child(str(add_eventDate)).set(add_eventName)
        print("The event {0} on the {1} has been added".format(add_eventName,add_eventDate))

# Update Data
wanna_update = input("Want to update an event?").lower()
if wanna_update == 'yes':
    updtDate = input("Type the date of the you want to update in YYYY-MM-DD format:")
    if not(updtDate is None or updtDate == ""):
        updtName = input("What should I name the event?")
        if not(updtName is None or updtName == ""):
            db.child('Events').update({updtDate: updtName})
            print("The event on the {1} has been updated to {0}".format(updtName, updtName))


# Delete Data
wanna_del = input("Want to delete an event?").lower()
if wanna_del == 'yes':
    delDate = input("Type the date of the event you want to delete in YYYY-MM-DD format:")
    if not(delDate is None or delDate == ""):
        data_del = db.child('Events').get()
        for eventdata in data_del.each():
          if eventdata.key() == str(delDate):
            db.child('Events').child(str(delDate)).remove()
            print("The event on the {} was deleted".format(delDate))

# Get Data
print("Getting Information on the event today")
data_retrieve = db.child('Events').get()
for eventdata in data_retrieve.each():
    # print keys
    # print(eventdata.key())
    # print values
    # print(eventdata.val())
    if eventdata.key() == str(datetime.date.today()):
      eventdetails = eventdata.val()
      print("true")

print("Today is " + eventdetails)
