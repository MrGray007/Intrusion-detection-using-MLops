# Intrusion Detection for Securing IoT Networks

* IoT networks are increasingly susceptible to cyber threats due to limited built-in security features in many devices, making them vulnerable to intrusions and attacks.


# DataSet

## How Data collected?? What does it trying??

* Go through this (https://www.unb.ca/cic/datasets/ids-2018.html) 

* From above link 

## DataSet Links
* Dataset available in Kaggle
https://www.kaggle.com/datasets/solarmainframe/ids-intrusion-csv

## My contribution 
* I have done some cleaning and combined the dataset for training purpose, available in Kaggle and do explore

Link (https://www.kaggle.com/datasets/maheshlee/ids-2018)

## Future Improvements
 * Our approach is DataCentric and some dimenstionaly reduction should be done and not used full data to train ,some improvements will be done in short period

 ## About Dataset
### List of Features 
| Feature Name           | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| Dst Port               | Destination port number                                                     |
| Protocol               | Protocol used (e.g., TCP, UDP, ICMP)                                       |
| Flow Duration          | Duration of the flow in microseconds                                       |
| Tot Fwd Pkts           | Total number of packets sent in the forward direction                      |
| Tot Bwd Pkts           | Total number of packets sent in the backward direction                     |
| TotLen Fwd Pkts        | Total length of all forward packets                                        |
| TotLen Bwd Pkts        | Total length of all backward packets                                       |
| Fwd Pkt Len Max        | Maximum length of packet in the forward direction                          |
| Fwd Pkt Len Min        | Minimum length of packet in the forward direction                          |
| Fwd Pkt Len Mean       | Mean length of packets in the forward direction                            |
| Fwd Pkt Len Std        | Standard deviation of forward packet lengths                               |
| Bwd Pkt Len Max        | Maximum length of packet in the backward direction                         |
| Bwd Pkt Len Min        | Minimum length of packet in the backward direction                         |
| Bwd Pkt Len Mean       | Mean length of packets in the backward direction                           |
| Bwd Pkt Len Std        | Standard deviation of backward packet lengths                              |
| Flow Byts/s            | Flow bytes per second                                                       |
| Flow Pkts/s            | Flow packets per second                                                     |
| Flow IAT Mean          | Mean time between two packets in a flow                                    |
| Flow IAT Std           | Standard deviation of inter-arrival time between packets                   |
| Flow IAT Max           | Maximum inter-arrival time in the flow                                     |
| Flow IAT Min           | Minimum inter-arrival time in the flow                                     |
| Fwd IAT Tot            | Total time between forward packets                                         |
| Fwd IAT Mean           | Mean time between forward packets                                          |
| Fwd IAT Std            | Standard deviation time between forward packets                            |
| Fwd IAT Max            | Maximum time between two forward packets                                   |
| Fwd IAT Min            | Minimum time between two forward packets                                   |
| Bwd IAT Tot            | Total time between backward packets                                        |
| Bwd IAT Mean           | Mean time between backward packets                                         |
| Bwd IAT Std            | Standard deviation time between backward packets                           |
| Bwd IAT Max            | Maximum time between two backward packets                                  |
| Bwd IAT Min            | Minimum time between two backward packets                                  |
| Fwd PSH Flags          | Number of times the PSH flag was set in the forward direction              |
| Fwd Header Len         | Total bytes used for headers in the forward direction                      |
| Bwd Header Len         | Total bytes used for headers in the backward direction                     |
| Fwd Pkts/s             | Number of forward packets per second                                       |
| Bwd Pkts/s             | Number of backward packets per second                                      |
| Pkt Len Min            | Minimum packet length in the flow                                          |
| Pkt Len Max            | Maximum packet length in the flow                                          |
| Pkt Len Mean           | Mean packet length in the flow                                             |
| Pkt Len Std            | Standard deviation of packet lengths in the flow                           |
| Pkt Len Var            | Variance of packet lengths in the flow                                     |
| FIN Flag Cnt           | Number of packets with FIN flag                                             |
| SYN Flag Cnt           | Number of packets with SYN flag                                             |
| RST Flag Cnt           | Number of packets with RST flag                                             |
| PSH Flag Cnt           | Number of packets with PSH flag                                             |
| ACK Flag Cnt           | Number of packets with ACK flag                                             |
| URG Flag Cnt           | Number of packets with URG flag                                             |
| ECE Flag Cnt           | Number of packets with ECE flag                                             |
| Down/Up Ratio          | Ratio of bytes transferred from destination to source                      |
| Pkt Size Avg           | Average size of all packets in the flow                                    |
| Fwd Seg Size Avg       | Average segment size in the forward direction                              |
| Bwd Seg Size Avg       | Average segment size in the backward direction                             |
| Subflow Fwd Pkts       | Total packets in a forward subflow                                         |
| Subflow Fwd Byts       | Total bytes in a forward subflow                                           |
| Subflow Bwd Pkts       | Total packets in a backward subflow                                        |
| Subflow Bwd Byts       | Total bytes in a backward subflow                                          |
| Init Fwd Win Byts      | Number of bytes sent in the initial window in the forward direction        |
| Init Bwd Win Byts      | Number of bytes sent in the initial window in the backward direction       |
| Fwd Act Data Pkts      | Number of forward packets with data payload                                |
| Fwd Seg Size Min       | Minimum segment size in the forward direction                              |
| Active Mean            | Mean time the flow was active before going idle                            |
| Active Std             | Standard deviation of time flow was active before going idle               |
| Active Max             | Maximum time the flow was active before going idle                         |
| Active Min             | Minimum time the flow was active before going idle                         |
| Idle Mean              | Mean time the flow was idle before becoming active                         |
| Idle Std               | Standard deviation of idle time                                            |
| Idle Max               | Maximum idle time                                                          |
| Idle Min               | Minimum idle time                                                          |

### Important and Correlation features based on Individual Attacks

1) Benign 
* Normal, non-malicious activity.


![corr_benign](images%2fcorr_benign.png)

 2) DoS (Denial of Service) Attack
* Goal: Make a service unavailable by overwhelming it with traffic.

* Typically launched from a single source.

![corr_dos](images%2fcorr_dos.png)

3) DDoS (Distributed Denial of Service) Attack
* Goal: Same as DoS, but on a larger scale.

* Comes from multiple sources (often a botnet).

![corr_ddos](images%2fcorr_ddos.png)

3) Brute Force Attack
* Goal: Gain unauthorized access by trying all possible combinations (usually for passwords).

![corr_bf](images%2fcorr_bf.png)


# Now Lets get into MLops
## Download Requirement modules
* ```bash
  pip install -r requirement.txt
  ```
## zenML server Set-Up
*  ```bash
    pip install zenml["server"]
   ```

* ```bash
    zenml init
  ```
  To login into ZenmlDashboard
* ```bash
   zenml login --local --blocking
  ```

After setting up zenml server and run pipeline(run_pipeline python file)
* Model Training Pipeline :
![model_training_pipeline.png](images%2FScreenshot%202025-03-14%20161120.png)
## Integration of ZenML with MlFlow
Installing MLFlow
* ```bash
   zenml integration install mlflow -y
  ```
Registering Experiment tracker 

* ```bash
  zenml experiment-tracker register mlflow_threats_track --flavor=mlflow
  ```
Registering Model deployer

* ```bash
  zenml model-deployer register mlflow_threat --flavor=mlflow    
  ```
Display Stack
* ```bash
  zenml stack describe  
  ```
Now Adding and setting ***Model deployer(-d) as mlflow_threat and Experiment_tracker(-e) as mlflow_threats_track and Artifact(-a) and Orchestrator(-o) are default***
* ```bash
   zenml stack register mlglow_stack_threat -a default -o default -d mlflow_threat -e mlflow_threats_track --set
   ```
To get Mlflow link type below url in run_pipeline to get Link
* ```bash
    Client().active_stack.experiment_tracker.get_tracking_uri()
  ```
# 👍The Solution


* Used MLflow_model_deployer to deploy the model:

🔧 mlflow_model_deployer_step – What is it?
A pipeline step that:

* Takes a trained model artifact.

* Uses MLflow to deploy that model (e.g., as a REST API).

* Registers the model in MLflow's model registry (optional but common).

* Allows interaction with the model via HTTP or gRPC endpoints.

In the deployment pipeline, ZenML's MLflow tracking integration is used for logging the hyperparameter values and the trained model itself and the model evaluation metrics -- as MLflow experiment tracking artifacts -- into the local MLflow backend. This pipeline also launches a local MLflow deployment server to serve the latest MLflow model if its accuracy is above a configured threshold.

The MLflow deployment server runs locally as a daemon process that will continue to run in the background after the example execution is complete. When a new pipeline is run which produces a model that passes the accuracy threshold validation, the pipeline automatically updates the currently running MLflow deployment server to serve the new model instead of the old one.

To round it off, we deploy a Streamlit application that consumes the latest model service asynchronously from the pipeline logic. This can be done easily with ZenML within the Streamlit code:

```bash
  service=predictor_loader(pipeline_name=pipeline_name,step_name=pipeline_step_name,running=True)
  ......
  service.predict(..)
  ```

# 📓 Diving into the code
You can run two pipelines as follows:

Training pipeline:
```bash
python run_pipeline.py
```

Continous Deployment:
```bash
python run_deployment.py
```

# 🕹 Streamlit Demo:

```bash
streamlit run streamlit.py
```

**In Future Changes will be done**

## ❓ FAQ
* When running the continuous deployment pipeline, I get an error stating: No Step found for the name mlflow_deployer.

  Solution: It happens because your artifact store is overridden after running the continuous deployment pipeline. So, you need to delete the artifact store and rerun the pipeline. You can get the location of the artifact store by running the following command:

  ```bash
  zenml artifact-store describe
  ```
  and then you can delete the artifact store with the following command:

  Note: This is a dangerous / destructive command! Please enter your path carefully, otherwise it may delete other folders from your computer.

  ```bash
  rm -rf PATH
  ```
* When running the continuous deployment pipeline, I get the following error: No Environment component with name mlflow is currently registered.

  Solution: You forgot to install the MLflow integration in your ZenML environment. So, you need to install the MLflow integration by running the following command:

  ```bash
  zenml integration install mlflow -y
  ```
