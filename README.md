# About streaming-producers

Set of scripts that produce streamming traffic.
| Script               | Usage                                                   |
| ---------------------| --------------------------------------------------------|
| crypto.py            | Provides real-time cryptocurrency prices via WebSocket. |

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
