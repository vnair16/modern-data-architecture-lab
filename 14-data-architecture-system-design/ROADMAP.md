# Data Architecture System Design Roadmap

Goal: build architecture judgment for designing data platforms and data products, including reusable patterns, integration styles, anti-patterns, trade-offs, and case-study practice.

This section is not certification-specific. It is the reference layer for interview preparation, architecture reviews, solution design, and real-world decision-making.

## Section 1: Data Architecture Foundations

### Topics to Cover

- OLTP vs OLAP
- Operational systems vs analytical systems
- Batch vs streaming
- Data warehouse, data lake, and lakehouse
- Medallion architecture
- Data mesh
- Data fabric
- Data product thinking
- Domain ownership
- Source-of-truth design
- Data contracts
- Data quality dimensions
- Metadata, lineage, and discoverability

### Plan

1. Write a one-page comparison of warehouse, lake, and lakehouse.
2. Create a glossary of core architecture terms.
3. Draw a generic enterprise data platform.
4. Define what makes a data product usable and trustworthy.

### Suggested Artifacts

- `notes/data-architecture-foundations.md`
- `diagrams/generic-enterprise-data-platform.md`
- `patterns/data-product-pattern.md`

## Section 2: Core Data Architecture Patterns

### Topics to Cover

- Medallion architecture
- Raw, curated, and serving layers
- Hub-and-spoke data platform
- Domain-oriented data products
- Lambda architecture
- Kappa architecture
- Event-driven architecture
- CQRS for analytical workloads
- CDC-based ingestion
- ELT vs ETL
- Data virtualization
- Semantic layer
- Feature store pattern
- Lakehouse sharing pattern

### Plan

1. Create one note per major pattern.
2. For each pattern, document context, when to use it, when not to use it, and trade-offs.
3. Link each pattern to one practical lab or diagram elsewhere in the repo.
4. Create a pattern comparison matrix.

### Suggested Artifacts

- `patterns/medallion-architecture.md`
- `patterns/event-driven-data-platform.md`
- `patterns/data-product-pattern.md`
- `patterns/lambda-vs-kappa.md`

## Section 3: Integration Patterns

### Topics to Cover

- File-based ingestion
- API-based ingestion
- Database replication
- Change data capture
- Event streaming
- Message queues vs event logs
- Webhooks
- Reverse ETL
- Data sharing
- Federation
- Data virtualization
- Bulk load vs incremental load
- Push vs pull integration
- Synchronous vs asynchronous integration
- Idempotent ingestion
- Replay and backfill

### Plan

1. Build an integration pattern catalog.
2. For each pattern, define latency, reliability, replay, schema, ownership, and operational concerns.
3. Create a decision tree for selecting ingestion and integration patterns.
4. Add examples using Kafka, Delta, Iceberg, Databricks, and cloud services where relevant.

### Suggested Artifacts

- `integration-patterns/cdc-ingestion.md`
- `integration-patterns/event-streaming.md`
- `integration-patterns/api-ingestion.md`
- `decision-frameworks/integration-pattern-decision-tree.md`

## Section 4: Modeling and Serving Patterns

### Topics to Cover

- Star schema
- Snowflake schema
- Data vault basics
- Wide analytical tables
- One big table pattern
- Aggregate tables
- Slowly changing dimensions
- Snapshot facts
- Event fact modeling
- Semantic layer
- Metrics layer
- Serving for BI
- Serving for ML
- Serving for APIs and applications

### Plan

1. Model the same domain using dimensional and data product approaches.
2. Document when wide tables are useful and when they become harmful.
3. Create SCD1, SCD2, and snapshot fact notes.
4. Design serving patterns for BI, ML, and API consumers.

### Suggested Artifacts

- `patterns/dimensional-modeling.md`
- `patterns/semantic-layer.md`
- `patterns/serving-patterns-bi-ml-api.md`

## Section 5: Reliability, Governance, and Operations Patterns

### Topics to Cover

- Data quality gates
- Quarantine pattern
- Dead-letter queue
- Retry and backoff
- Idempotency
- Exactly-once vs effectively-once
- Reprocessing and backfill
- Schema evolution
- Data contract versioning
- Observability
- SLA and SLO design
- Incident runbooks
- Access control
- Audit and lineage
- Cost governance

### Plan

1. Create reliability pattern notes for retries, idempotency, replay, and quarantine.
2. Build a failure-mode table for a lakehouse pipeline.
3. Define observability signals for batch and streaming workloads.
4. Create a governance checklist for new data products.

### Suggested Artifacts

- `patterns/data-quality-gates.md`
- `patterns/replay-and-backfill.md`
- `patterns/observability-for-data-platforms.md`
- `decision-frameworks/data-product-governance-checklist.md`

## Section 6: Data Architecture Anti-Patterns

### Topics to Cover

- Everything in one table
- Unowned shared tables
- Spreadsheet as integration layer
- Point-to-point pipeline sprawl
- No source-of-truth definition
- Data lake as dumping ground
- Over-partitioning
- Small-file explosion
- Reprocessing without idempotency
- Streaming used where batch is enough
- Premature real-time architecture
- Business logic duplicated across tools
- Unversioned data contracts
- Silent schema drift
- Dashboard-only validation
- PII copied everywhere
- No lineage or ownership
- Cost-blind architecture

### Plan

1. Create an anti-pattern catalog.
2. For each anti-pattern, document symptoms, root causes, consequences, and better patterns.
3. Add examples connected to Databricks, Spark, Kafka, Delta, Iceberg, and cloud architecture.
4. Build a review checklist that can be used during architecture design.

### Suggested Artifacts

- `anti-patterns/pipeline-sprawl.md`
- `anti-patterns/data-lake-dumping-ground.md`
- `anti-patterns/premature-real-time.md`
- `anti-patterns/silent-schema-drift.md`

## Section 7: Trade-Off and Decision Frameworks

### Topics to Cover

- Batch vs streaming
- ETL vs ELT
- Delta vs Iceberg
- Warehouse vs lakehouse
- Kafka vs queue
- Spark Structured Streaming vs Flink
- Denormalized vs dimensional model
- Build vs buy
- Centralized vs domain-oriented platform
- Real-time API vs batch scoring
- Managed service vs self-managed platform
- Cost vs latency
- Governance vs autonomy

### Plan

1. Create decision records for common architecture choices.
2. Use a consistent template: context, forces, options, decision, consequences.
3. Link decisions to experiments and roadmaps in other sections.
4. Keep examples grounded in realistic enterprise constraints.

### Suggested Artifacts

- `decision-frameworks/batch-vs-streaming.md`
- `decision-frameworks/delta-vs-iceberg.md`
- `decision-frameworks/kafka-vs-queue.md`
- `decision-frameworks/centralized-vs-domain-oriented.md`

## Section 8: Case Study Practice

### Topics to Cover

- Requirements discovery
- Functional requirements
- Non-functional requirements
- Data volume and velocity
- Latency and freshness
- Consumers and personas
- Security and compliance
- Cost constraints
- Migration constraints
- Operational model
- Rollout strategy

### Plan

1. Create 5-7 realistic case studies.
2. For each case, write requirements, architecture, trade-offs, risks, and rollout plan.
3. Include at least one batch platform, one streaming platform, one governed lakehouse, one ML serving design, and one GenAI/RAG data architecture.
4. Add diagrams and ADRs.

### Suggested Case Studies

- Retail clickstream analytics platform
- Banking CDC-based customer 360 platform
- Healthcare governed lakehouse
- IoT streaming anomaly detection
- Lightweight ML model serving for churn prediction
- Enterprise RAG over governed documents
- Multi-domain data product platform

## Reusable Design Template

Use this outline for every system design note:

```markdown
# Design Title

## Problem

## Requirements

## Constraints

## Architecture

## Data Flow

## Integration Pattern

## Storage and Table Design

## Processing Pattern

## Serving Pattern

## Governance and Security

## Reliability and Operations

## Cost Considerations

## Trade-Offs

## Anti-Patterns Avoided

## Open Questions
```

## Readiness Checklist

- I can choose appropriate ingestion and integration patterns.
- I can explain when batch, streaming, CDC, API, or file ingestion fits.
- I can identify common data architecture anti-patterns early.
- I can defend table format, modeling, and serving decisions.
- I can design for ownership, governance, observability, and reprocessing.
- I can turn vague business requirements into a practical data platform design.

