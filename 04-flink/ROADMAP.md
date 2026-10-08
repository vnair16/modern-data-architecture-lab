# Flink Roadmap

Goal: understand Flink deeply enough to compare it with Spark Structured Streaming from a data architect perspective.

## Section 1: Flink Runtime

### Topics to Cover

- JobManager
- TaskManager
- Task slots
- Parallelism
- Operators
- Sources and sinks
- DataStream API
- Checkpoints and savepoints

### Plan

1. Run a local Flink cluster.
2. Execute a simple DataStream job.
3. Change parallelism and observe task execution.
4. Capture job UI evidence.

## Section 2: Stateful Processing

### Topics to Cover

- Keyed streams
- Keyed state
- Operator state
- State backends
- Timers
- Checkpoint barriers
- Recovery

### Plan

1. Build a keyed aggregation.
2. Store per-key state.
3. Trigger a controlled failure.
4. Recover from checkpoint or savepoint.
5. Document the state model.

## Section 3: Event Time

### Topics to Cover

- Event time vs processing time
- Watermark strategies
- Out-of-order events
- Late data handling
- Tumbling, sliding, and session windows
- Timers

### Plan

1. Reuse Kafka events from the Spark Streaming section.
2. Implement event-time windows.
3. Send late and out-of-order events.
4. Compare outputs with Spark.

## Section 4: Kafka and Architecture Fit

### Topics to Cover

- Kafka source and sink
- Exactly-once state consistency
- Low-latency use cases
- Operational complexity
- Backpressure
- Scaling
- Spark vs Flink decision criteria

### Plan

1. Build Kafka to Flink to file or console output.
2. Measure approximate latency.
3. Compare state, checkpointing, and recovery with Spark.
4. Write ADR: Spark Structured Streaming vs Flink.

## Portfolio Artifacts

- Flink job
- Kafka integration evidence
- Failure recovery proof
- Spark vs Flink ADR
- Use-case decision matrix

