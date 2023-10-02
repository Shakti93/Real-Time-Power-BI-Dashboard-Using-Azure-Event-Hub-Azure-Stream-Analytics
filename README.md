# Real-Time-Power-BI-Dashboard-Using-Azure-Event-Hub-Azure-Stream-Analytics

## Introduction

This project report outlines the development of a real-time Power BI dashboard using Azure Event Hub and Azure Stream Analytics. The objective is to retrieve real-time stock details and display them on a Power BI dashboard, enabling users to make informed decisions based on live data.

## Solution Diagram

![Python stream solution diagram](https://github.com/Shakti93/Real-Time-Power-BI-Dashboard-Using-Azure-Event-Hub-Azure-Stream-Analytics/assets/84408451/42e19098-94fb-484d-bdbb-6c5258054d1f)


## Prerequisites

Before proceeding with the project, the following prerequisites must be met:

1. An active Azure Subscription.
2. An Azure IoT hub in your Azure Subscription.
3. A Power BI account.
4. Visual Studio Code for Python program development.

## Creating and Configuring Azure Resources

### Create a Resource Group

To begin, a resource group must be created under your Azure Subscription. Follow these steps:

1. Sign in to the Azure portal.
2. Navigate to your resource group section.
3. Create a new resource group under your subscription.

### Create an Event Hub Namespace & Event Hub

1. Search for "Azure Event Hub" in the Azure Marketplace and create an Event Hub Namespace.
2. Within the Event Hub Namespace, create an Event Hub. Configure the partition count as needed.
3. To enable communication with the Python program, create an access policy with the "Manage" option under the Event Hubs namespace in the Shared Access Policies section.

### Create an Azure Stream Analytics Job

1. Search for "Azure Stream Analytics" in the Azure Marketplace and create a Stream Analytics Job. Ensure you select the same geographical location as the Azure Event Hub Namespace.
2. After creating the Stream Analytics job, configure the input for the job by setting up the Event Hub configuration.

## Developing the Python Program
The Python program is responsible for retrieving stock information and sending it to Azure using the configured Azure Event Hub in your Azure account. The following steps outline the process:

### Importing Required Libraries

Import the necessary Python libraries for program development.

  `from dis import findlinestarts
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
  warnings.filterwarnings("ignore", category=DeprecationWarning)`

### Python Program to Send Stock Information to an Azure Event Hub
Develop the Python program with functions to retrieve stock information and send it to the Azure Event Hub. Ensure that the program functions correctly, and verify data transmission by checking the Azure Stream Analytics Job in the Query section.


`def get_stock_data(stockName):
      stock_pull = si.get_quote_table(stockName)
      stock_df = pd.DataFrame([stock_pull])
      return stock_df.to_dict('record')
  datetime.now()
  get_stock_data('AAPL')`

  `async def run():
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
            print('Stock Data Sent To Azure Event Hub')`
  
`loop = asyncio.get_event_loop()
try:
  loop.run_until_complete(run())
  loop.run_forever()
except KeyboardInterrupt:
  pass
finally:
  print('Closing Loop Now')
  loop.close()`

## Building the Power BI Dashboard
In this section, we create a Power BI dashboard using real-time data received through the Azure Event Hub.

### Creating a Power BI Dataset

Configure the output options under "Job Topology" to add the Power BI option. Provide the necessary information and authorization to create a Power BI dataset in your workspace.

### Developing the Power BI Dashboard

1. Navigate to the Power BI workspace to view the dataset created using the Stream Analytics Job.
2. Create a dashboard by selecting the "Dashboard" option in the menu section and naming it.
3. Add visuals to the Power BI report by going to the edit section and selecting "Add Tile."
4. Choose the "Custom Streaming Data" option and select the dataset created using Azure Stream Analytics Job.
5. Customize your dashboard with various components such as Cards, Line Charts, etc., based on your specific requirements.

## Conclusion

This project report has detailed the process of creating a real-time Power BI dashboard using Azure Event Hub and Azure Stream Analytics. By following the steps outlined in this report, users can effectively integrate real-time stock data into a dynamic and informative Power BI dashboard, enabling data-driven decision-making.
