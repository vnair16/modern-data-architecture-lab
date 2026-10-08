# Spark Developer Associate Roadmap

Goal: prepare for the Databricks Certified Associate Developer for Apache Spark exam and build interview-ready Spark artifacts.

Official scope reference: Databricks exam guide for Associate Developer for Apache Spark, October 2025.

## Section 1: Spark Architecture and Components

### Topics to Cover

- Spark advantages and limitations
- Driver, executor, cluster manager, worker node, CPU core, memory
- SparkSession lifecycle
- DataFrame and Dataset concepts
- Job, stage, task, partition, executor slot
- Transformations vs actions
- Lazy evaluation
- Narrow vs wide dependencies
- Caching and storage levels
- Garbage collection basics
- Spark modules: Core, SQL, DataFrames, Pandas API on Spark, Structured Streaming, MLlib

### Plan

1. Draw the execution hierarchy from application to task.
2. Run a simple PySpark job and identify jobs, stages, and tasks in Spark UI.
3. Create examples of narrow and wide transformations.
4. Cache a DataFrame with different storage levels and observe behavior.
5. Write a one-page explanation in `notes/architecture.md`.

### Lab Artifact

- `notebooks/01-spark-architecture.py`
- `evidence/spark-ui-jobs-stages-tasks.png`

## Section 2: Spark SQL

### Topics to Cover

- Reading and writing CSV, JSON, ORC, Parquet, Delta files
- Querying files directly with SQL
- Temporary views and global temporary views
- Managed vs external tables
- Save modes: append, overwrite, ignore, error
- Partitioned writes
- Sorting and table layout basics
- SQL functions and expressions

### Plan

1. Load the same dataset using DataFrame API and SQL.
2. Register a temporary view and run SQL transformations.
3. Write partitioned output and inspect folders.
4. Compare save modes with a small table.
5. Document when SQL is clearer than DataFrame API.

## Section 3: DataFrame and Dataset API Applications

### Topics to Cover

- `select`, `filter`, `where`, `withColumn`, `drop`, `withColumnRenamed`
- Type casting and column expressions
- `groupBy`, aggregations, approximate distinct counts
- `summary`, `describe`
- Deduplication
- Null handling
- Array, map, struct, explode
- Window functions
- User-defined functions vs built-in functions

### Plan

1. Build a data cleaning pipeline over nested sample data.
2. Add checks for row counts and null handling.
3. Implement a UDF and then replace it with native Spark functions.
4. Create a window-function example for ranking or deduplication.
5. Capture before/after physical plans.

## Section 4: Query Planning and Optimization

### Topics to Cover

- Logical plan, analyzed plan, optimized plan, physical plan
- Catalyst optimizer
- Predicate pushdown and column pruning
- Adaptive Query Execution
- Broadcast joins
- Sort-merge joins
- Shuffle hash joins
- Skew handling
- Partition count decisions
- `repartition` vs `coalesce`

### Plan

1. Use `explain("extended")` on representative queries.
2. Compare joins with and without broadcast hints.
3. Create skewed data and test mitigation.
4. Benchmark different partition counts.
5. Write an optimization note with evidence.

## Section 5: Structured Streaming Basics

### Topics to Cover

- Streaming DataFrames
- File stream source
- Kafka source concepts
- Triggers
- Output modes
- Checkpoints
- Watermarks
- Stateful aggregation
- Late data
- Streaming query progress

### Plan

1. Use file streaming in Databricks Community Edition.
2. Build a windowed aggregation with watermarking.
3. Stop and restart the stream from a checkpoint.
4. Record query progress and recovery behavior.
5. Link advanced streaming work to `03-spark-streaming`.

## Readiness Checklist

- I can explain a Spark job from code to tasks.
- I can interpret an extended physical plan.
- I can choose between broadcast and shuffle joins.
- I can explain partitioning, shuffles, and skew.
- I can use core PySpark DataFrame APIs without lookup.
- I can build and restart a simple streaming query.

