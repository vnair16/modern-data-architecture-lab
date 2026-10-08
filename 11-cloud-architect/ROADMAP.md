# Cloud Architect Certification Roadmap

Goal: prepare for a cloud architect certification while keeping the work relevant to data architecture and Databricks platform architecture.

If your target is Azure, use AZ-305 first. If your target is AWS or GCP, use the matching path below. Keep the shared architecture artifacts cloud-neutral where possible.

## Path A: Microsoft Azure Solutions Architect Expert, AZ-305

Official scope reference: Microsoft AZ-305 study guide, skills measured as of April 17, 2026.

### Domain 1: Design Identity, Governance, and Monitoring Solutions

Topics:

- Logging and monitoring
- Log routing
- Azure Monitor and Log Analytics concepts
- Authentication and authorization
- Microsoft Entra ID
- Managed identities
- RBAC
- Secrets, certificates, and keys
- Management groups, subscriptions, resource groups
- Tagging, Azure Policy, compliance, identity governance

Plan:

1. Design an Azure landing zone for a data platform.
2. Create a management group and subscription model.
3. Define monitoring and log-routing architecture.
4. Create an identity and access model for Databricks plus data services.

### Domain 2: Design Data Storage Solutions

Topics:

- Relational data stores
- Azure SQL options
- Database service tiers
- Scalability
- Data protection
- Semi-structured and unstructured data
- Storage accounts
- Redundancy
- Lifecycle management
- Data integration and analysis services

Plan:

1. Create a storage decision matrix.
2. Design a lakehouse storage architecture.
3. Compare SQL, Cosmos DB, Blob/ADLS, and analytical options.
4. Document backup and durability choices.

### Domain 3: Design Business Continuity Solutions

Topics:

- Backup
- Disaster recovery
- RTO and RPO
- High availability
- Regional failover
- Azure Site Recovery concepts
- Backup vaults
- Data replication
- Application resilience

Plan:

1. Define RTO/RPO for three workloads.
2. Design DR for a lakehouse and operational app.
3. Compare backup, replication, and failover options.
4. Create a DR runbook.

### Domain 4: Design Infrastructure Solutions

Topics:

- Compute
- Containers
- Serverless
- Networking
- Load balancing
- Application Gateway
- Azure Front Door
- Private endpoints
- DNS
- Hybrid connectivity
- Migration
- DevOps and automation

Plan:

1. Draw a hub-spoke network.
2. Design private connectivity for Databricks and storage.
3. Create compute hosting decision matrix.
4. Add migration and modernization plan.

## Path B: AWS Certified Solutions Architect Professional, SAP-C02

Official scope reference: AWS SAP-C02 exam guide.

### Domain 1: Design Solutions for Organizational Complexity

Topics:

- Multi-account strategy
- AWS Organizations and Control Tower concepts
- Identity federation
- Hybrid connectivity
- Multi-region patterns
- Shared services
- Governance at scale

Plan:

1. Design a multi-account data platform.
2. Define networking and shared services.
3. Create identity and governance model.

### Domain 2: Design for New Solutions

Topics:

- Compute selection
- Storage selection
- Database selection
- Network architecture
- Security controls
- Reliability
- Performance
- Cost optimization

Plan:

1. Build architecture decisions for three workloads.
2. Map each decision to Well-Architected pillars.
3. Create a cost and resilience trade-off note.

### Domain 3: Continuous Improvement for Existing Solutions

Topics:

- Operational excellence
- Security improvement
- Reliability improvement
- Performance improvement
- Cost control
- Observability
- Migration from legacy patterns

Plan:

1. Take an intentionally weak architecture.
2. Improve it across security, cost, reliability, and performance.
3. Document before/after decisions.

### Domain 4: Accelerate Workload Migration and Modernization

Topics:

- Migration strategies
- Application discovery
- Database migration
- Hybrid architecture
- Modernization
- Containerization
- Serverless modernization
- Data migration

Plan:

1. Create migration wave plan.
2. Define rehost, replatform, refactor decisions.
3. Add rollback and validation plan.

## Path C: Google Professional Cloud Architect

Official scope reference: Google Professional Cloud Architect exam guide.

### Domain 1: Design and Plan a Cloud Solution Architecture

Topics:

- Business requirements
- Technical requirements
- Cost optimization
- Application design
- Integration
- Data movement
- Build, buy, modify, or deprecate decisions
- Compliance and observability

Plan:

1. Read official case studies.
2. Extract business and technical requirements.
3. Create architecture options and trade-offs.

### Domain 2: Manage and Provision Solution Infrastructure

Topics:

- Resource hierarchy
- IAM
- Networking
- Compute
- Storage
- Deployment
- Infrastructure automation

Plan:

1. Design resource hierarchy.
2. Define IAM and network controls.
3. Create deployment model.

### Domain 3: Design for Security and Compliance

Topics:

- IAM
- Network security
- Encryption
- Data protection
- Compliance
- Audit logging
- Least privilege

Plan:

1. Create security architecture.
2. Add audit and compliance flow.
3. Threat-model a data platform.

### Domain 4: Analyze and Optimize Technical and Business Processes

Topics:

- Process improvement
- Cost optimization
- Operational improvement
- Technical debt
- Automation

Plan:

1. Analyze an existing architecture.
2. Propose improvements.
3. Tie improvements to business metrics.

### Domain 5: Manage Implementation

Topics:

- Deployment planning
- Team coordination
- Testing
- Migration execution
- Change management

Plan:

1. Create an implementation plan.
2. Define validation and rollback.
3. Build stakeholder communication notes.

### Domain 6: Ensure Solution and Operations Reliability

Topics:

- Monitoring
- Logging
- Incident response
- SRE concepts
- Resilience
- DR
- Performance

Plan:

1. Define SLOs.
2. Create monitoring architecture.
3. Build incident response runbook.

## Shared Cloud Architect Portfolio Artifacts

- Cloud landing zone design
- Data platform network architecture
- Identity and governance model
- Storage decision matrix
- Business continuity and DR plan
- Cost optimization review
- Migration and modernization plan
- Case-study architecture review

