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

data = {
  'Event Title': 'Pizza Day',
  'Description': 'We eat pizzas',
}
data2 = {
  'Event Title': 'Lollipop Day',
  'Description': 'Suckers'

}
# Add Data
# db.child('Events').child("Tomorrow").set(data)
# db.child('Events').child("Today").set(data2)

# Update Data
# db.child('Events').child("Tomorrow").update({'Description': 'We are Pizzas'})
# db.child('Events').child("Today").update({'Description': 'We are Pizzas'})

# Get Data
# data_retrieve = db.child('Events').child("Tomorrow").get()
# for eventdata in data_retrieve.each():
#     # print keys
#     print(eventdata.key())
#     # print values
#     print(eventdata.val())

# Delete Data
# data_delTmrw = db.child('Events').child("Tomorrow").get()
# for eventdata in data_delTmrw.each():
#   if eventdata.val() == "Pizza Day":
#     db.child('Events').child('Tomorrow').remove()

# data_delTdy = db.child('Events').child("Today").get()
# for eventdata in data_delTdy.each():
#   if eventdata.val() == "Pizza Day":
#     db.child('Events').child('Today').remove()