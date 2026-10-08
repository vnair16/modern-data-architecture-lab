# Delta Lake Roadmap

Goal: build deep Delta Lake skill for Databricks data engineering, table design, CDC, governance, and performance optimization.

Official scope references: Delta Lake documentation and Databricks Delta optimization documentation.

## Section 1: Delta Lake Foundations

### Topics to Cover

- Delta Lake purpose
- ACID transactions
- Transaction log
- Parquet data files
- Snapshot isolation
- Batch and streaming unification
- Time travel
- Schema enforcement
- Schema evolution
- Table protocol and feature compatibility

### Plan

1. Create a Delta table in Databricks CE if available.
2. Inspect table files and transaction log behavior.
3. Run time-travel queries.
4. Document transaction-log concepts in `notes/delta-log.md`.

## Section 2: Writes, Updates, and CDC

### Topics to Cover

- Append and overwrite
- UPDATE
- DELETE
- MERGE
- Upserts
- Change data capture
- Change data feed
- SCD Type 1
- SCD Type 2
- Idempotent loads

### Plan

1. Build a customer dimension with SCD1 and SCD2 variants.
2. Simulate CDC input records.
3. Use MERGE to apply changes.
4. Capture before/after state and edge cases.
5. Write a CDC design note.

## Section 3: Table Layout and Performance

### Topics to Cover

- Small-file problem
- Compaction
- OPTIMIZE concepts
- Data skipping
- Partitioning
- ZORDER concepts
- Liquid clustering
- Clustering columns
- File statistics
- Query plan impact

### Plan

1. Create a small-file scenario.
2. Compare query behavior before and after compaction or simulated compaction.
3. Evaluate partitioning vs clustering choices.
4. Document when liquid clustering is preferred.

## Section 4: Reliability and Maintenance

### Topics to Cover

- VACUUM
- Retention
- Restore
- Time travel retention implications
- Concurrent writes
- Streaming reads and writes
- Checkpoints
- Schema changes in streaming
- Data quality checks

### Plan

1. Test table version history.
2. Simulate rollback or restore.
3. Document retention trade-offs.
4. Create a maintenance runbook.

## Section 5: Governance and Architecture

### Topics to Cover

- Unity Catalog with Delta
- Managed vs external tables
- Data sharing concepts
- Lineage
- Access control
- Auditability
- Medallion architecture
- Data product design

### Plan

1. Design a Delta-based medallion architecture.
2. Define table ownership and access.
3. Create governance matrix.
4. Link to Databricks DE and Platform Architecture roadmaps.

## Portfolio Artifacts

- Delta transaction log notes
- SCD2 MERGE example
- Time travel and restore example
- Table layout decision note
- Delta maintenance runbook
- Medallion architecture diagram

