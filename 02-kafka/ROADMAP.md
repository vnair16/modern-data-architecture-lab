# Kafka Roadmap

Goal: build the event backbone knowledge needed for Spark Streaming, Flink, and architecture interviews.

## Section 1: Kafka Core Concepts

### Topics to Cover

- Broker, cluster, controller
- Topic and partition
- Leader and follower replicas
- Producer and consumer
- Consumer group
- Offset and committed offset
- Retention and compaction
- Delivery semantics

### Plan

1. Run Kafka locally.
2. Create single-partition and multi-partition topics.
3. Produce keyed and unkeyed events.
4. Consume with one and then multiple consumers.
5. Record partition assignment and offset behavior.

## Section 2: Producer Design

### Topics to Cover

- Key selection
- Ordering guarantees
- Batching and compression
- Retries
- Idempotent producers
- Acknowledgments
- Error handling
- Serialization

### Plan

1. Build a producer for clickstream or order events.
2. Test keys that preserve per-customer ordering.
3. Simulate retry and duplicate scenarios.
4. Write a producer design note.

## Section 3: Consumer Design

### Topics to Cover

- Poll loop
- Consumer group rebalancing
- Offset commit strategies
- At-least-once and effectively-once processing
- Lag measurement
- Backpressure
- Replay
- Poison-message handling

### Plan

1. Build a consumer that logs offset and partition.
2. Add a second consumer and observe reassignment.
3. Stop one consumer and document rebalance behavior.
4. Replay from an earlier offset.
5. Write a consumer runbook.

## Section 4: Architecture and Operations

### Topics to Cover

- Partition count planning
- Replication factor
- Retention vs compaction
- Schema Registry concepts
- Compatibility modes
- Monitoring metrics
- Lag alerts
- Disaster recovery patterns
- Event contracts

### Plan

1. Create an event contract for one business event.
2. Design partitioning and retention rules.
3. Define operational metrics and alerts.
4. Write an ADR for topic design.

## Portfolio Artifacts

- Local Kafka setup
- Producer and consumer examples
- Event contract
- Topic design ADR
- Lag and rebalance evidence

