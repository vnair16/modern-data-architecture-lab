# Claude Certified Architect Roadmap

Goal: prepare for Anthropic's Claude Certified Architect - Foundations certification and build practical evidence that you can design Claude-powered systems responsibly.

Official scope reference: Anthropic Academy Claude Certified Architect - Foundations certification page. Current domains are:

| Domain | Weight |
| --- | ---: |
| Agentic Architecture and Orchestration | 27% |
| Claude Code Configuration and Workflows | 20% |
| Prompt Engineering and Structured Output | 20% |
| Tool Design and MCP Integration | 18% |
| Context Management and Reliability | 15% |

## Section 1: Agentic Architecture and Orchestration

### Topics to Cover

- When to use a single prompt, workflow, agent, or multi-agent design
- Agent loop concepts
- Planning and execution separation
- Human-in-the-loop checkpoints
- Tool selection and delegation
- Long-running task design
- State management across turns
- Failure modes in agentic systems
- Cost, latency, and reliability trade-offs
- Production boundaries for autonomy

### Plan

1. Design three Claude-powered solutions: a Q&A assistant, a workflow assistant, and an agentic automation.
2. For each design, decide whether it should be single-shot, workflow-based, or agentic.
3. Add a human approval point for high-risk actions.
4. Document agent failure modes and mitigations.
5. Create an ADR comparing agentic and deterministic workflow approaches.

### Portfolio Artifact

- `agentic-architecture/agentic-vs-workflow-adr.md`
- `agentic-architecture/solution-patterns.md`
- `evidence/agent-design-review.md`

## Section 2: Claude Code Configuration and Workflows

### Topics to Cover

- Claude Code project setup
- `CLAUDE.md` or project instruction files
- Planning workflows
- Codebase navigation
- Tool permissions and safety boundaries
- Test-driven iteration
- Refactoring workflows
- Debugging workflows
- CI/CD-assisted development
- Handling large repositories
- Prompting Claude Code with clear task boundaries

### Plan

1. Create a sample repo workflow using Claude Code-style project instructions.
2. Define coding standards, test expectations, and safety rules.
3. Practice a bug-fix loop: inspect, patch, test, summarize.
4. Practice a feature loop: understand code, plan, implement, verify.
5. Create a Claude Code operating checklist.

### Portfolio Artifact

- `claude-code/claude-code-workflow.md`
- `claude-code/project-instructions-template.md`
- `practice/bugfix-simulation.md`

## Section 3: Prompt Engineering and Structured Output

### Topics to Cover

- System, developer, and user instruction separation
- Clear task framing
- Examples and counterexamples
- Role and audience constraints
- Structured outputs
- JSON schema-style output thinking
- Tool-call prompting
- Refusal and safety-aware prompting
- Prompt evaluation
- Prompt versioning
- Reducing ambiguity and over-constraint

### Plan

1. Build prompts for summarization, extraction, classification, and decision support.
2. Add structured output requirements for each prompt.
3. Test prompts against edge cases and ambiguous inputs.
4. Create a prompt evaluation checklist.
5. Version prompt changes and record why they improved reliability.

### Portfolio Artifact

- `prompting-structured-output/prompt-patterns.md`
- `prompting-structured-output/structured-output-examples.md`
- `prompting-structured-output/prompt-evaluation-checklist.md`

## Section 4: Tool Design and MCP Integration

### Topics to Cover

- Tool use architecture
- Tool descriptions and input schemas
- Tool selection behavior
- Tool result design
- Error handling
- Idempotency
- Permission boundaries
- MCP server and client concepts
- MCP tool design
- Secure tool integration
- Observability for tool calls

### Plan

1. Design three tools for a Claude-powered data architecture assistant.
2. Write tool schemas with clear names, descriptions, and inputs.
3. Define success, retryable error, and non-retryable error responses.
4. Add permission and idempotency rules.
5. Draft an MCP integration design note.

### Portfolio Artifact

- `mcp-tools/tool-design-guide.md`
- `mcp-tools/mcp-integration-design.md`
- `mcp-tools/tool-error-handling.md`

## Section 5: Context Management and Reliability

### Topics to Cover

- Context window limits
- Retrieval vs prompt stuffing
- Memory and summarization patterns
- Session state
- Source grounding
- Long task continuity
- Evaluation datasets
- Regression testing
- Monitoring model behavior
- Reliability trade-offs
- Cost and latency controls

### Plan

1. Design a context strategy for a document-heavy architecture assistant.
2. Compare summarization, retrieval, and explicit state files.
3. Create a reliability checklist for long-running Claude tasks.
4. Build a small evaluation set with expected outcomes.
5. Document monitoring signals for production use.

### Portfolio Artifact

- `context-reliability/context-strategy.md`
- `context-reliability/reliability-checklist.md`
- `practice/evaluation-set.md`

## Four-Week Study Plan

| Week | Focus | Output |
| --- | --- | --- |
| 1 | Agentic architecture and Claude Code workflows | Agent pattern ADR and Claude Code workflow checklist |
| 2 | Prompting, structured outputs, and evaluation | Prompt pattern library and evaluation checklist |
| 3 | Tool design, MCP, and context management | Tool design guide and MCP integration note |
| 4 | Reliability, practice scenarios, and review | Mock scenario notes and weak-area remediation |

## Databricks/Data Architect Tie-In

Use Claude certification prep to strengthen your data architect portfolio:

- Design a Claude assistant for Databricks architecture review.
- Add tools for reading pipeline metadata, checking ADRs, or generating runbooks.
- Build prompts for architecture decision analysis.
- Create evaluation cases for hallucination, unsafe tool use, and poor source grounding.
- Document how Claude agents should interact with governed data platforms.

## Readiness Checklist

- I can decide when agentic architecture is appropriate.
- I can design Claude Code workflows with clear project instructions and verification steps.
- I can produce structured, testable prompt outputs.
- I can design safe, observable tools and MCP integrations.
- I can manage context for long-running and document-heavy Claude tasks.
- I can discuss reliability, evaluation, safety, latency, and cost trade-offs.

