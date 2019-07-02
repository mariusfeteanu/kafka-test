import faust


## App
app = faust.App('test-join-app', broker='kafka://kafka1:9092')

class RegisteredUser(faust.Record, serializer='json'):
    account_id: str
    email: str
    name: str

class EnquiryInitiated(faust.Record, serializer='json'):
    enquiry_id: str
    date: str
    product: str
    account_id: str

class EnquiryCompleted(faust.Record, serializer='json'):
    enquiry_id: str
    date: str
    best_partner: str

class SaleCompleted(faust.Record, serializer='json'):
    sale_id: str
    enquiry_id: str
    date: str
    amount: float

class FullEnquiryCompleted(faust.Record, serializer='json'):
    enquiry_id: str
    completed_date: str
    product: str
    best_partner: str

registered_topic = app.topic('registered_topic')
enquiry_initiated_topic = app.topic('enquiry_initiated_topic')
enquiry_completed_topic = app.topic('enquiry_completed_topic')
sale_completed_topic = app.topic('sale_completed_topic')

enquiry_initiated_table = app.Table('product_date', default=int)

print(RegisteredUser(account_id='kjduebvfds',
                        email='marius.something@gmail.cob',
                        name='Marius').to_representation())

def mask_user(user):
    return RegisteredUser(
        account_id=user.account_id,
        email=user.email[::-1],
        name=user.name[::-1])


@app.agent(registered_topic)
async def mask_pii(registered_users):
    async for registered_user in registered_users:
        print(f'INFO: Putting mask on {registered_user.account_id}')
        masked_user = mask_user(registered_user)
        yield masked_user

@app.agent(enquiry_initiated_topic)
async def calculate_enquiries_per_date(enquiries_initiated):
    async for enquiry_initiated in enquiries_initiated:
        enquiry_initiated_table[(enquiry_initiated.product, enquiry_initiated.date)] += 1
        yield enquiry_initiated

# @app.task()
# async def full_enquiry_completed_stream():
#     enquiry_initiated = enquiry_initiated_topic.stream()
#     enquiry_completed = enquiry_completed_topic.stream()
#     print("STARTED: full_enquiry_completed_stream")
#     async for event in (enquiry_initiated & enquiry_completed).join():
#         print("EVENT: ", event)
#         yield event
#     print("STOP: Falling out of task")

#
# @app.agent()
# async def somethingsomething(full_enquiry_completed_stream):
#     async for event in full_enquiry_completed_stream:
#         yield event
