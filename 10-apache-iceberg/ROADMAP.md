# Apache Iceberg Roadmap

Goal: build Apache Iceberg table-format knowledge for open lakehouse architecture and multi-engine interoperability.

Official scope references: Apache Iceberg documentation and specification.

## Section 1: Iceberg Foundations

### Topics to Cover

- Open table format purpose
- Tables over object storage
- Metadata files
- Manifest lists
- Manifest files
- Data files
- Snapshots
- Snapshot isolation
- Atomic commits
- Hidden partitioning

### Plan

1. Draw the Iceberg metadata hierarchy.
2. Create a small Iceberg table locally or in Spark if available.
3. Inspect metadata files.
4. Write `notes/iceberg-metadata-model.md`.

## Section 2: Schema and Partition Evolution

### Topics to Cover

- Add column
- Drop column
- Rename column
- Widen type
- Nested schema evolution
- Partition spec evolution
- Hidden partition transforms
- Query correctness during evolution

### Plan

1. Create a table and evolve schema.
2. Change partition strategy.
3. Compare old and new snapshots.
4. Document why partition evolution matters.

## Section 3: Reads, Writes, and Deletes

### Topics to Cover

- Append
- Overwrite
- Row-level deletes
- Position deletes
- Equality deletes
- Merge-on-read concepts
- Copy-on-write concepts
- Snapshot expiration
- Rollback

### Plan

1. Run append and overwrite operations.
2. Test delete semantics where engine support exists.
3. Roll back to an earlier snapshot.
4. Document engine-specific limitations.

## Section 4: Catalogs and Engine Interoperability

### Topics to Cover

- Catalog role
- Hive Metastore
- REST catalog
- Glue catalog concepts
- Spark integration
- Flink integration
- Trino/Presto concepts
- Multi-engine read/write considerations
- Locking and commit conflicts

### Plan

1. Document catalog options.
2. Test Spark reads and writes if local dependencies allow.
3. Design a multi-engine lakehouse pattern.
4. Compare Delta and Iceberg architecture choices.

## Section 5: Operations and Governance

### Topics to Cover

- Metadata cleanup
- Snapshot expiration
- Orphan file removal
- Compaction
- File sizing
- Branching and tagging concepts
- Auditability
- Access control via catalog/platform
- Observability using metadata

### Plan

1. Create an operations checklist.
2. Design retention and cleanup rules.
3. Create an Iceberg vs Delta decision ADR.
4. Link evidence to portfolio index.

## Portfolio Artifacts

- Iceberg metadata diagram
- Schema and partition evolution lab
- Snapshot rollback lab
- Catalog comparison note
- Delta vs Iceberg ADR
- Operations checklist

