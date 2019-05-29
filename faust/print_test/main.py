import faust

app = faust.App(
    'whatevs-app',
    broker='kafka://kafka1:9092',
    value_serializer='raw',
)

test_topic = app.topic('test_topic')

print('Starting')

@app.agent(test_topic)
async def greet(messages):
    async for message in messages:
        print(message)

print('Going out the end')
