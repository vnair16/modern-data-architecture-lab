# Spark Structured Streaming Roadmap

Goal: build reliable streaming pipelines and understand Spark's micro-batch execution model.

## Section 1: Structured Streaming Foundations

### Topics to Cover

- Streaming DataFrame model
- Micro-batch execution
- Sources and sinks
- Triggers
- Output modes: append, update, complete
- Query progress
- Checkpoint directory structure
- Exactly-once considerations

### Plan

1. Build a file-based streaming pipeline in Databricks Community Edition.
2. Add query progress logging.
3. Restart from checkpoint and verify no duplicate output.
4. Document what checkpointing stores.

## Section 2: Kafka Integration

### Topics to Cover

- Kafka source options
- Kafka sink options
- Starting offsets
- Ending offsets
- Checkpointed offsets
- Key/value deserialization
- Event schema parsing
- Dead-letter patterns

### Plan

1. Use local Kafka for integration if Databricks CE networking is limited.
2. Read Kafka events into Spark.
3. Parse JSON payloads with an explicit schema.
4. Write valid records and rejected records separately.
5. Document offset behavior across restarts.

## Section 3: Event Time and State

### Topics to Cover

- Event time vs processing time
- Watermarks
- Late data
- Windowed aggregations
- Deduplication
- Stream-static joins
- Stream-stream joins
- State store and state cleanup

### Plan

1. Generate out-of-order events.
2. Build tumbling and sliding window aggregations.
3. Add watermarking and compare late-event outcomes.
4. Demonstrate deduplication by event ID.
5. Capture stateful query progress.

## Section 4: Reliability and Operations

### Topics to Cover

- Restart behavior
- Idempotent writes
- Failed batch recovery
- Schema changes
- Backpressure
- Trigger intervals
- Monitoring and alerting
- Runbook design

### Plan

1. Force a stream failure.
2. Repair the bad input or code.
3. Restart and prove recovery.
4. Create an operator runbook.
5. Add evidence to portfolio index.

## Capstone

Build a Kafka to Spark Structured Streaming to Delta-style medallion pipeline with Bronze raw ingestion, Silver parsed and deduplicated stream, Gold windowed aggregate, checkpoint recovery, watermark testing, architecture diagram, and runbook.

