# Databricks notebook source
from dis import findlinestarts
import pandas as pd
import json
from yahoo_fin import stock_info as si
from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData
from azure.eventhub.exceptions import EventHubError
import asyncio
import requests
import nest_asyncio
from datetime import datetime
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

# COMMAND ----------

nest_asyncio.apply()

# COMMAND ----------

con_string = 'Endpoint=sb://dev-eventhub-stream.servicebus.windows.net/;SharedAccessKeyName=eh-python-sas;SharedAccessKey=1jTYlsa3sQ3VpX8d21KmOUH3QPc9NgvBX+AEhB1DbJw=;EntityPath=eh-python-stock'
eventhub_name = 'eh-python-stock'
def get_stock_data(stockName):
    stock_pull = si.get_quote_table(stockName)
    stock_df = pd.DataFrame([stock_pull])
    return stock_df.to_dict('record')
datetime.now()
get_stock_data('AAPL')

# COMMAND ----------

async def run():
# Create a producer client to send messages to the event hub.
# Specify a connection string to your event hubs namespace and# the event hub name.
    while True:
        await asyncio.sleep(5)
        producer = EventHubProducerClient.from_connection_string(conn_str=con_string, eventhub_name=eventhub_name)
        async with producer:
            # Create a batch.
            event_data_batch = await producer.create_batch()
            # Add events to the batch.
            event_data_batch.add(EventData(json.dumps(get_stock_data('AAPL'))))
            # Send the batch of events to the event hub.
            await producer.send_batch(event_data_batch)
            print('Stock Data Sent To Azure Event Hub')

# COMMAND ----------

loop = asyncio.get_event_loop()

try:
  loop.run_until_complete(run())
  loop.run_forever()
except KeyboardInterrupt:
  pass
finally:
  print('Closing Loop Now')
  loop.close()
