# About streaming-producers

Set of scripts that produce streaming traffic.  
  
**Script:** `crypto.py`  
**Description:** Provides real-time cryptocurrency prices via WebSocket.  
**Data Sample:**   
``` 
JSON
{
  "type": "ticker",
  "product_id": "BTC-USD",
  "price": "64210.11",
  "time": "2026-03-09T10:23:00Z"
} 
```
             
## TOOLS
| Usage                | Tool                                                  |
| ---------------------| ------------------------------------------------------|
| Cloud provider       | ![GCP](/assets/64px-Google_Cloud_logo.svg.png)|
| Language             | ![Python](/assets/32px-Python-logo-notext.svg.png)|

## PRE-REQUISITES

1. The destintion GCP project and topic must exist.
2. Create a `.env` file in the project folder root and include the variables below:

```
PROJECT_ID=your-project-id
TOPIC_ID=your-topic-name
```

3. install the project dependencies

```
pip install -r requirements.txt
```
