# to run this file from cmmand line you will have to enter the following cammand
# python manage.py shell < dummydata.py

import os
from mainSite import databaseManager
from django.core.management import call_command

os.remove('db.sqlite3')
call_command('syncdb', interactive = False)

userList = [{'username':'kayush', 'department':'cse', 'name':'Ayush', 'course':'btech', 'hostel' : 'Siang'},
		 {'username':'adgfd', 'department':'cse', 'name':'sdg', 'course':'btech', 'hostel' : 'Kameng'},
		 {'username':'Student1', 'department':'ece', 'name':'Nice Name', 'course':'mtech', 'hostel' : 'Subuansiri'},
		 {'username':'Student2', 'department':'des', 'name':'Hiyaa', 'course':'phd', 'hostel' : 'Siang'}
		]

passy = databaseManager.registerUsers(userList)

databaseManager.makeCandidate('adgfd','[{"id": "field0", "type": "text", "value": "Ad Fg Jkl"}, {"id": "field1", "type": "radio", "value": "Male"}, {"id": "field2", "type": "file", "value": "/agendas/not-available.pdf"}]', 'Vice President', '/static/candidates/photos/adgfd.jpg', True)

from mainSite.models import Posts
post = Posts(postname="Vice President", info_fields="[{'description': u'Name', 'type': u'text', 'id': 'field0', 'validation': u'', 'placeholder': u'', 'options': u''}, {'description': u'Gender', 'type': u'radio', 'id': 'field1', 'validation': u'', 'placeholder': u'', 'options': u'Male; Female'}, {'description': u'Agenda', 'type': u'file', 'id': 'field2', 'validation': u'*.pdf', 'placeholder': u'', 'options': u''}]")
post.save()

print passy
databaseManager.registerVote("some text pertaining to a vote", "kayush", passy[0])
databaseManager.registerVote("some text pertaining to a vote", "kayush", passy[0])
databaseManager.registerVote("some text pertaining to a vote", "kayush", passy[0])
