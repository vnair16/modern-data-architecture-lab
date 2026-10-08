# Master Roadmap

This is the topic map for the learning path. Use it to decide what to study and where to place notes, experiments, diagrams, notebooks, and runbooks.

## Target Outcome

Build a certification-backed data architecture portfolio that proves practical skill in Spark, Databricks, Delta Lake, Apache Iceberg, streaming, cloud architecture, and GenAI.

## Certification Sequence

| Phase | Certification or specialization | Primary folder | Outcome |
| --- | --- | --- | --- |
| 0 | Git and GitHub repository foundation | `00-roadmap`, `.github` | Clean repo, CI, reusable note and experiment structure |
| 1 | Databricks Certified Associate Developer for Apache Spark | `01-spark` | Spark internals and PySpark practice artifacts |
| 2 | Delta Lake specialization | `09-delta-lake` | CDC, SCD, optimization, time travel, reliability examples |
| 3 | Databricks Certified Data Engineer Professional | `06-databricks-de` | End-to-end lakehouse engineering roadmap |
| 4 | Kafka, Spark Streaming, Flink | `02-kafka`, `03-spark-streaming`, `04-flink`, `05-streaming-architecture` | Streaming architecture capstone |
| 5 | Databricks Platform Architect | `07-platform-architecture` | Platform topology, governance, security, cost, DR design |
| 6 | MLflow on Databricks | `13-mlflow-databricks` | Lightweight ML model tracking, registry, serving, and API calls |
| 7 | Data Architecture System Design | `14-data-architecture-system-design` | Patterns, integration styles, anti-patterns, and design trade-offs |
| 8 | Cloud Architect certification | `11-cloud-architect` | Azure, AWS, or GCP architect certification roadmap |
| 9 | Apache Iceberg specialization | `10-apache-iceberg` | Table format and interoperability portfolio |
| 10 | Databricks GenAI Engineer Associate | `08-genai` | Governed RAG and agent evaluation artifacts |

## Suggested Study Sequence

| Sequence | Focus | Reference output |
| --- | --- | --- |
| 1 | Git, Spark, Delta fundamentals | Spark execution plan lab, join lab, partitioning lab |
| 2 | Databricks DE and Delta engineering | Bronze/Silver/Gold pipeline with Delta patterns |
| 3 | Streaming engineering | Kafka to Spark Streaming pipeline and recovery test |
| 4 | Flink and streaming architecture | Spark vs Flink ADR and capstone design |
| 5 | Platform and cloud architecture | Databricks platform and cloud architecture case studies |
| 6 | MLflow on Databricks | Lightweight model training, registry, serving endpoint, and API client |
| 7 | Data architecture system design | Pattern notes, anti-pattern catalog, integration decision records |
| 8 | Claude Certified Architect | Claude agent, MCP, Claude Code, prompting, and reliability notes |
| 9 | GenAI engineering | Governed RAG prototype and evaluation report |

## Reference-Building Rhythm

| Activity type | Activity | Output |
| --- | --- | --- |
| Theory | Read official docs and exam objectives | Topic notes |
| Lab | Build a focused experiment | Notebook, script, or config |
| Architecture | Create a design note or ADR | Decision record or diagram |
| Review | Summarize what was learned and what remains unclear | Updated topic notes |
| Reference cleanup | Normalize file names, examples, and diagrams | Reusable knowledge base |

## Evidence Standard

Each topic can include any useful combination of these: working notebook or script, architecture diagram, ADR or design note, runbook, screenshot or logs, performance comparison, failure/recovery test, or exam notes.

The repo does not need status columns or progress logs. The structure itself is the checklist: if a topic matters, it gets a clear section and a place for notes or experiments.

## Source Notes

The detailed section roadmaps are aligned to official exam guides and documentation current as of October 8, 2026. Re-check official guides before booking any exam because certification outlines can change.
