# Streaming Architecture Roadmap

Goal: convert hands-on Kafka, Spark Streaming, and Flink work into architecture artifacts.

## Section 1: Requirements Modeling

### Topics to Cover

- Business events
- Event contracts
- Latency requirements
- Throughput requirements
- Ordering requirements
- Retention requirements
- Replay requirements
- Data quality expectations

### Plan

1. Define three realistic enterprise use cases.
2. Capture functional and non-functional requirements.
3. Map each use case to event contracts.
4. Document assumptions and constraints.

## Section 2: Platform Patterns

### Topics to Cover

- Event backbone
- Stream ingestion
- Stream enrichment
- Stateful processing
- Lakehouse ingestion
- Lambda vs Kappa thinking
- Medallion streaming
- Operational boundaries

### Plan

1. Draw a Kafka to lakehouse architecture.
2. Add a low-latency Flink path.
3. Add replay and dead-letter flows.
4. Define observability and ownership.

## Section 3: Spark vs Flink Decisioning

### Topics to Cover

- Micro-batch vs event-at-a-time processing
- Latency
- Stateful processing complexity
- Checkpointing
- Backpressure
- Ecosystem fit
- Databricks integration
- Operational skill requirements

### Plan

1. Create a comparison matrix.
2. Score Spark and Flink against three enterprise use cases.
3. Write an ADR with consequences and risks.

## Section 4: Reliability and Governance

### Topics to Cover

- Schema evolution
- Event versioning
- Exactly-once claims
- Idempotency
- Replay safety
- Data contracts
- Monitoring
- Alerting
- Runbooks
- Access control

### Plan

1. Create a streaming data contract template.
2. Define failure modes and runbook actions.
3. Add governance checkpoints.
4. Link designs to Databricks and cloud architecture sections.

## Capstone

Publish a streaming architecture package with architecture diagram, event contracts, Spark and Flink comparison ADR, operational runbook, failure-mode table, and cost/complexity notes.

