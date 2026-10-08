# Modern Data Architecture Learning Lab

This repository is a self-learning reference library and experiment workspace for Databricks, Spark, streaming, lakehouse table formats, cloud architecture, Claude architecture, and GenAI.

The guiding rule is simple: every topic should have a place for reusable notes and hands-on experiments:

- Code or notebook
- README or design note
- Reproducible example
- Evidence such as logs, screenshots, diagrams, benchmark notes, or an ADR

## Learning Tracks

| Folder | Focus | Mapped credential |
| --- | --- | --- |
| [00-roadmap](00-roadmap/ROADMAP.md) | Topic map and repository navigation | Entire roadmap |
| [01-spark](01-spark/ROADMAP.md) | Spark internals, PySpark, tuning, Structured Streaming basics | Spark Developer Associate |
| [02-kafka](02-kafka/ROADMAP.md) | Kafka fundamentals and event backbone design | Streaming extension |
| [03-spark-streaming](03-spark-streaming/ROADMAP.md) | Kafka to Spark Structured Streaming to Delta | Spark + DE Professional |
| [04-flink](04-flink/ROADMAP.md) | Flink stateful and event-time processing | Streaming self-learning |
| [05-streaming-architecture](05-streaming-architecture/ROADMAP.md) | Spark vs Flink decisions and enterprise patterns | Architect portfolio |
| [06-databricks-de](06-databricks-de/ROADMAP.md) | Delta, Lakeflow concepts, CI/CD, monitoring, data modeling | Data Engineer Professional |
| [07-platform-architecture](07-platform-architecture/ROADMAP.md) | Databricks platform, governance, security, cloud architecture | Platform Architect |
| [08-genai](08-genai/ROADMAP.md) | RAG, vector search, MLflow evaluation, serving architecture | GenAI Engineer Associate |
| [09-delta-lake](09-delta-lake/ROADMAP.md) | Delta Lake internals, CDC, optimization, governance, reliability | Delta Lake specialization |
| [10-apache-iceberg](10-apache-iceberg/ROADMAP.md) | Iceberg table format, metadata, evolution, catalogs, interoperability | Iceberg lakehouse specialization |
| [11-cloud-architect](11-cloud-architect/ROADMAP.md) | Azure AZ-305, AWS SAP-C02, and Google PCA certification prep | Cloud Architect certification |
| [12-claude-certified-architect](12-claude-certified-architect/ROADMAP.md) | Claude agent architecture, Claude Code, MCP, prompting, context, reliability | Anthropic Claude Certified Architect |
| [13-mlflow-databricks](13-mlflow-databricks/ROADMAP.md) | MLflow tracking, model registry, Databricks Model Serving, REST API calls | MLflow and lightweight model deployment |
| [14-data-architecture-system-design](14-data-architecture-system-design/ROADMAP.md) | Data architecture patterns, integration patterns, anti-patterns, trade-off design | Data architecture system design |

## Common Workspace Areas

- [docs/adr](docs/adr/README.md): architecture decision records.
- [docs/diagrams](docs/diagrams/README.md): platform, streaming, data flow, and security diagrams.
- [docs/runbooks](docs/runbooks/README.md): operational procedures and troubleshooting notes.
- [experiments/databricks-ce](experiments/databricks-ce/README.md): Databricks Community Edition notebook exports and run notes.
- [experiments/local](experiments/local/README.md): local Docker, Kafka, Flink, and command-line experiments.
- [assets/sample-data](assets/sample-data/README.md): small synthetic datasets used by exercises.
- [assets/screenshots](assets/screenshots/README.md): screenshots that prove runs, plans, lineage, dashboards, or failures.

## Suggested Workflow

1. Pick a topic from the relevant `ROADMAP.md`.
2. Add notes under the module's `notes/` folder or create a new note beside the topic.
3. Create a small experiment, notebook, diagram, ADR, or runbook in the matching folder.
4. Record setup, commands, assumptions, results, and lessons learned.
5. Export Databricks Community Edition notebooks as source files and place them under the relevant module.
