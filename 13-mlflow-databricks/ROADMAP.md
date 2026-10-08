# MLflow on Databricks Roadmap

Goal: learn the practical MLflow workflow on Databricks so you can train lightweight ML models, track experiments, register models, deploy them with Databricks Model Serving, and call them through a REST API.

Official scope references: Databricks MLflow documentation and Databricks Model Serving documentation. Current Databricks flow: MLflow Tracking, Unity Catalog Model Registry, Databricks Model Serving, REST API endpoint.

## Section 1: MLflow Fundamentals

### Topics to Cover

- What MLflow is used for
- Experiments
- Runs
- Parameters
- Metrics
- Artifacts
- Models
- Model flavors
- Autologging vs manual logging
- Reproducibility basics

### Plan

1. Create an MLflow experiment in Databricks.
2. Train a small scikit-learn model such as logistic regression, random forest, or linear regression.
3. Log parameters, metrics, artifacts, and the model.
4. Compare two or three runs in the MLflow experiment UI.
5. Write notes explaining experiments vs runs vs registered models.

### Suggested Artifacts

- `notebooks/01-mlflow-tracking-basics.py`
- `notes/experiments-runs-models.md`
- `evidence/mlflow-run-comparison.png`

## Section 2: Lightweight Model Training

### Topics to Cover

- Feature and label preparation
- Train/test split
- Baseline model selection
- Metrics for classification and regression
- Overfitting checks
- Data leakage
- Model input schema
- Model signature
- Input examples

### Plan

1. Use a small public or synthetic dataset.
2. Train a simple model that is fast enough for Databricks Community Edition or Free Edition.
3. Log the model with signature and input example.
4. Save preprocessing assumptions beside the notebook.
5. Add a small inference test inside the notebook.

### Suggested Artifacts

- `notebooks/02-lightweight-model-training.py`
- `src/train_model.py`
- `notes/model-input-contract.md`

## Section 3: Model Registry with Unity Catalog

### Topics to Cover

- Model Registry purpose
- Registered model
- Model version
- Unity Catalog model naming
- Model aliases
- Governance and lineage concepts
- Promotion from experiment to reusable model
- Champion/challenger pattern

### Plan

1. Register the best logged model.
2. Add description and tags.
3. Create or document a model alias strategy such as `Champion`.
4. Record what metadata is useful before serving.
5. Document Community Edition or workspace limitations if Unity Catalog registry is unavailable.

### Suggested Artifacts

- `notebooks/03-register-model.py`
- `notes/model-registry-and-aliases.md`
- `evidence/registered-model.png`

## Section 4: Databricks Model Serving

### Topics to Cover

- Serving endpoint purpose
- Endpoint configuration
- Served model entity
- Scale-to-zero and lightweight serving considerations
- Dependency management
- Environment compatibility
- Request and response schema
- Endpoint permissions
- Inference logging concepts
- Monitoring request and response behavior

### Plan

1. Deploy the registered model to a Databricks Model Serving endpoint if your workspace supports it.
2. If serving is unavailable in Community Edition, document the exact production steps and test local MLflow serving instead.
3. Capture endpoint name, input schema, and expected payload format.
4. Send a test request from the Databricks UI or notebook.
5. Save evidence of a successful prediction.

### Suggested Artifacts

- `model-serving/serving-endpoint-notes.md`
- `model-serving/request-response-schema.md`
- `evidence/model-serving-prediction.png`

## Section 5: Calling the Model Through an API

### Topics to Cover

- REST API endpoint URL
- Authentication with Databricks token or service principal pattern
- JSON payload structure
- `dataframe_records` style payloads
- Response parsing
- Error handling
- Timeout handling
- Input validation
- API client packaging

### Plan

1. Create a minimal Python API client.
2. Read endpoint URL and token from environment variables.
3. Send a prediction request using `requests`.
4. Parse and print predictions.
5. Add error handling for 400, 401, 403, 404, and 5xx responses.

### Suggested Artifacts

- `api-client/invoke_endpoint.py`
- `api-client/sample_payload.json`
- `notes/api-calling-pattern.md`

### Example Client Shape

```python
import os
import requests

endpoint_url = os.environ["DATABRICKS_MODEL_ENDPOINT_URL"]
token = os.environ["DATABRICKS_TOKEN"]

payload = {
    "dataframe_records": [
        {"feature_1": 1.0, "feature_2": 2.0}
    ]
}

response = requests.post(
    endpoint_url,
    headers={"Authorization": f"Bearer {token}"},
    json=payload,
    timeout=30,
)
response.raise_for_status()
print(response.json())
```

## Section 6: Production Readiness Basics

### Topics to Cover

- Data contract
- Model contract
- Input validation
- Model versioning
- Rollback
- Champion/challenger
- Monitoring
- Drift concepts
- Latency and cost
- Security and secret handling
- Batch vs real-time scoring decision

### Plan

1. Create a production-readiness checklist for small models.
2. Define model input and output contracts.
3. Document rollback strategy.
4. Compare batch scoring vs REST API serving for two use cases.
5. Link production model governance to Databricks DE and Platform Architecture sections.

### Suggested Artifacts

- `notes/production-readiness-checklist.md`
- `notes/batch-vs-real-time-scoring.md`
- `model-serving/rollback-strategy.md`

## Capstone

Build a small end-to-end MLflow deployment package:

- Train a lightweight model in Databricks.
- Track runs in MLflow.
- Register the best model.
- Deploy to a serving endpoint or document production serving steps if unavailable.
- Call the model using a Python API client.
- Save payload, response, and lessons learned.

## Readiness Checklist

- I can explain experiments, runs, artifacts, logged models, and registered models.
- I can log a simple model with metrics, signature, and input example.
- I can register a model and explain versioning and aliases.
- I can describe Databricks Model Serving and when to use it.
- I can call a served model through a REST API.
- I can explain basic production concerns for lightweight ML model APIs.

