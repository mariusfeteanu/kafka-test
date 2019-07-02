import json

from kafka import KafkaProducer

# from main import *

producer = KafkaProducer(bootstrap_servers='kafka1:9092')

print('Pushing test events')

users = [
    {'account_id': 'kjduebvfds', 'email': 'marius.something@gmail.cob', 'name': 'Marius',
     '__faust': {'ns': 'inno.main.RegisteredUser'}},
    {'account_id': 'werggsaeq', 'email': 'some.guy@gmail.cob', 'name': 'Some guy',
     '__faust': {'ns': 'inno.main.RegisteredUser'}}
]
for user in users:
    producer.send('registered_topic',
                  value=bytes(json.dumps(user), encoding='utf-8'))


enquiries_initiated = [
  {'enquiry_id': '1', 'date': '2018-01-01', 'product': 'A', 'account_id': 'kjduebvfds',
   '__faust': {'ns': 'inno.main.EnquiryInitiated'}},
  {'enquiry_id': '2', 'date': '2018-01-02', 'product': 'B', 'account_id': 'werggsaeq',
   '__faust': {'ns': 'inno.main.EnquiryInitiated'}},
  {'enquiry_id': '3', 'date': '2018-01-02', 'product': 'C', 'account_id': 'werggsaeq',
   '__faust': {'ns': 'inno.main.EnquiryInitiated'}},
]
for enquiry_initiated in enquiries_initiated:
  producer.send('enquiry_initiated_topic',
                value=bytes(json.dumps(enquiry_initiated), encoding='utf-8'))


enquiries_completed = [
  {'enquiry_id': '1', 'date': '2018-01-01', 'best_partner': 'ZZ',
   '__faust': {'ns': 'inno.main.EnquiryCompleted'}},
  {'enquiry_id': '2', 'date': '2018-01-02', 'best_partner': 'yY',
   '__faust': {'ns': 'inno.main.EnquiryCompleted'}},
  {'enquiry_id': '3', 'date': '2018-01-02', 'best_partner': 'ZZ',
   '__faust': {'ns': 'inno.main.EnquiryCompleted'}},
]
for enquiry_completed in enquiries_completed:
  producer.send('enquiry_completed_topic',
                value=bytes(json.dumps(enquiry_completed), encoding='utf-8'))


print('Pushed test events')

producer.flush()
