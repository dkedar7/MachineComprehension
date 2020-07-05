# Machine Comprehension (under development)

Web application to demonstrate ability of some state-of-the-art machine learning models at the questions answering task. The models chosen for the first deployment of the app are:

1. BiDAF - ONNX pre-trained model
2. DistilBERT - HuggingF ace implementation
3. RoBERTa - Deepset implementation (on Hugging face model zoo)
4. ALBERT - twmkn9 implmentation (on Hugging face model zoo)

# Deployment (work in progress)

The demo deployment will likely utilize Google Build to containerize the application, Google Container Registry for storing and managing a container and Google Cloud Run to deploy it as a web endpoint.

![Cloud Run Architecture](https://github.com/dkedar7/Data-Analyzer/blob/master/Analyzer/assets/architecture.png?raw=true)

[More about Google Cloud Run](https://cloud.google.com/run/docs/)

# How to install (work in progress)

# Dependencies (work in progress)
You need [Python 3](https://python3statement.org/) to run this application. Other dependencies can be found in the [requirements.txt](https://github.com/dkedar7/MachineComprehension/blob/master/Analyzer/requirements.txt) file.

# License
Machine Comprehension uses the [MIT license](https://github.com/dkedar7/MachineComprehension/blob/master/LICENSE).




