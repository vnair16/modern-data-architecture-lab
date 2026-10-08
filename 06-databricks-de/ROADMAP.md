# Databricks Data Engineer Professional Roadmap

Goal: prepare for the Databricks Certified Data Engineer Professional exam and build production-style lakehouse artifacts.

Official scope reference: Databricks Data Engineer Professional exam guide, November 30, 2025.

## Section 1: Developing Code for Data Processing

### Topics to Cover

- Batch ingestion
- Streaming ingestion
- Auto Loader concepts
- Delta reads and writes
- MERGE, UPDATE, DELETE
- Lakeflow Spark Declarative Pipelines concepts
- Lakeflow Jobs concepts
- Parameters and task orchestration
- Incremental processing

### Plan

1. Build a Bronze to Silver to Gold pipeline.
2. Add incremental ingestion.
3. Use MERGE for upserts.
4. Add a streaming variant.
5. Document which features were implemented directly in CE and which were simulated.

## Section 2: Cost and Performance Optimization

### Topics to Cover

- File sizing
- Partitioning
- ZORDER concepts
- Liquid clustering
- Photon concepts
- Compute sizing
- Spark plans
- Join optimization
- Skew mitigation
- Caching decisions

### Plan

1. Benchmark small files vs compacted files.
2. Compare partitioning strategies.
3. Study liquid clustering and document when it replaces partition/ZORDER decisions.
4. Tune one Spark workload and capture before/after plans.

## Section 3: Transformation, Cleansing, and Data Quality

### Topics to Cover

- Deduplication
- Constraints and expectations
- CDC
- SCD Type 1 and Type 2
- Quarantine tables
- Data validation rules
- Idempotent transformations

### Plan

1. Build SCD1 and SCD2 examples.
2. Add data quality checks.
3. Create rejected-record handling.
4. Document CDC edge cases.

## Section 4: Monitoring and Alerting

### Topics to Cover

- System tables
- Query profiles
- Spark UI
- Lakeflow event logs
- Job run history
- Streaming query progress
- SLA and SLO design
- Alert routing

### Plan

1. Create a monitoring checklist.
2. Capture Spark UI and query profile evidence.
3. Create a failed-run investigation runbook.
4. Define SLOs for one pipeline.

## Section 5: Security and Compliance

### Topics to Cover

- Unity Catalog concepts
- Catalog, schema, table hierarchy
- Permission inheritance
- Secrets
- Service principals
- Audit logs
- Lineage
- Least privilege
- Network security concepts

### Plan

1. Design a Unity Catalog hierarchy for domains.
2. Create a least-privilege access matrix.
3. Threat-model one data product.
4. Document CE limitations and production design.

## Section 6: Data Sharing and Federation

### Topics to Cover

- Delta Sharing concepts
- Lakehouse Federation concepts
- Cross-platform data access
- Sharing governance
- Data product boundaries

### Plan

1. Create a conceptual data-sharing design.
2. Define producer and consumer responsibilities.
3. Add security and lineage considerations.

## Section 7: Data Governance

### Topics to Cover

- Metadata
- Discovery
- Ownership
- Classification
- Lineage
- Quality ownership
- Access reviews
- Domain-oriented data products

### Plan

1. Create a governance operating model.
2. Define metadata fields for a data product.
3. Add stewardship and access review workflow.

## Section 8: Debugging and Deploying

### Topics to Cover

- Spark UI troubleshooting
- Cluster logs
- Query profiles
- Job repair
- Parameter overrides
- Databricks Asset Bundles
- Git folders
- CI/CD workflows
- Unit testing
- CLI and REST API concepts

### Plan

1. Create a broken pipeline scenario.
2. Debug it using logs and plan evidence.
3. Write a deployment design using Asset Bundles.
4. Add a simple CI workflow for local checks.

## Section 9: Data Modeling

### Topics to Cover

- Medallion architecture
- Dimensional modeling
- Facts and dimensions
- SCD1 and SCD2
- Data products
- Delta table layout
- Liquid clustering vs partitioning

### Plan

1. Model one enterprise domain.
2. Build dimensions and facts.
3. Add SCD2 history.
4. Document table layout choices.

## Readiness Checklist

- I can design and implement an incremental lakehouse pipeline.
- I can explain Delta operations and table layout choices.
- I can debug Spark and pipeline failures.
- I can design Unity Catalog governance.
- I can explain Databricks CI/CD and deployment patterns.
- I can model analytical data products.

