# Databricks GenAI Engineer Associate Roadmap

Goal: prepare for the Databricks Certified Generative AI Engineer Associate exam and build a governed RAG or agent application portfolio.

Official scope reference: Databricks Generative AI Engineer Associate exam guide, interim February 2026.

## Section 1: LLM Fundamentals

### Topics to Cover

- Tokens and context windows
- Prompting
- Model selection
- Inference parameters
- Latency and cost trade-offs
- Safety and responsible AI basics
- Batch vs real-time inference

### Plan

1. Compare two models for three enterprise use cases.
2. Document latency, quality, and cost considerations.
3. Build prompt variants and evaluate output quality.

## Section 2: RAG Architecture

### Topics to Cover

- Document loading
- Parsing
- Chunking
- Embeddings
- Vector indexing
- Retrieval
- Reranking
- Grounding
- Citation strategy
- Hallucination mitigation

### Plan

1. Build a small document corpus.
2. Test chunking strategies.
3. Create embeddings and retrieval.
4. Add answer generation with retrieved context.
5. Evaluate groundedness.

## Section 3: Vector Search and Retrieval

### Topics to Cover

- Vector indexes
- Metadata filters
- Sync/update strategy
- Recall and precision
- Hybrid search concepts
- Retrieval debugging

### Plan

1. Create a vector search or local equivalent.
2. Add metadata filters.
3. Compare retrieval results across chunking methods.
4. Record weak retrieval cases.

## Section 4: MLflow, Evaluation, and Monitoring

### Topics to Cover

- Experiment tracking
- Tracing
- Evaluation datasets
- Retrieval metrics
- Answer quality metrics
- LLM judges
- Ground-truth requirements
- Custom scorers
- SME feedback

### Plan

1. Create an evaluation dataset.
2. Track prompts and outputs.
3. Score retrieval and generation quality.
4. Incorporate feedback and improve the app.

## Section 5: Serving, Agents, and Governance

### Topics to Cover

- Model serving endpoints
- Inference logging
- Inference tables
- AI Gateway concepts
- Usage tracking
- Rate limits
- Agent Framework concepts
- Tool use
- Unity Catalog governance
- Permissions and lineage

### Plan

1. Design serving architecture.
2. Build or simulate a data-aware agent.
3. Define cost controls and logging.
4. Create production readiness checklist.
5. Threat-model the GenAI application.

