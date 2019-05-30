import faust

app = faust.App(
    'word_count',
    broker='kafka://kafka1:9092',
    value_serializer='raw',
)

test_topic = app.topic('test_topic')
word_count_topic = app.Table('word_count_table', default=int)

print('Starting')

@app.agent(test_topic)
async def process(stream):
    async for event in stream:
        # split sentences into words
        for word in event.split():
            # word_event = ???
            yield word.forward(word_count_topic)

print('Going out the end')
