# Databricks Platform Architect Roadmap

Goal: prepare for Databricks platform architecture accreditation-style topics and build enterprise-grade platform architecture artifacts.

## Section 1: Account and Workspace Architecture

### Topics to Cover

- Databricks account model
- Workspace topology
- Region strategy
- Dev, test, prod isolation
- Environment promotion
- Account-level administration
- Workspace-level administration

### Plan

1. Draw a multi-workspace enterprise topology.
2. Define environment boundaries.
3. Describe deployment and promotion flow.
4. Add assumptions for Azure, AWS, or GCP.

## Section 2: Identity and Access

### Topics to Cover

- SSO
- SCIM
- Groups
- Service principals
- Identity federation
- RBAC
- Permission inheritance
- Privileged access

### Plan

1. Create group and role model.
2. Map users, engineers, analysts, service principals, and admins.
3. Define break-glass and access-review processes.
4. Link to Unity Catalog design.

## Section 3: Unity Catalog Architecture

### Topics to Cover

- Metastore
- Catalogs
- Schemas
- Tables and views
- Storage credentials
- External locations
- Grants
- Lineage
- Data domains

### Plan

1. Design catalog hierarchy by domain and environment.
2. Define external location strategy.
3. Create grants matrix.
4. Document lineage and discovery flow.

## Section 4: Network Architecture

### Topics to Cover

- VPC/VNet injection concepts
- Private connectivity
- Private endpoints
- DNS
- Egress controls
- Firewalls
- Hub-spoke patterns
- Hybrid connectivity

### Plan

1. Draw secure network architecture.
2. Define ingress and egress paths.
3. Add DNS and private endpoint requirements.
4. Document risks and controls.

## Section 5: Security Architecture

### Topics to Cover

- Encryption at rest
- Encryption in transit
- Secrets
- Key management
- Least privilege
- Audit logs
- Data classification
- Threat modeling

### Plan

1. Create a security controls checklist.
2. Threat-model one lakehouse workload.
3. Define audit and retention requirements.
4. Link controls to cloud-native services.

## Section 6: Compute Governance

### Topics to Cover

- Cluster policies
- SQL warehouses
- Serverless vs classic compute
- Job compute vs interactive compute
- Isolation modes
- Runtime strategy
- Library management

### Plan

1. Define compute standards by persona.
2. Create cost and security guardrails.
3. Document approved runtimes and libraries.
4. Add exceptions process.

## Section 7: Cost, Monitoring, and DR

### Topics to Cover

- Tagging
- Budgets
- Cost attribution
- System tables
- Audit logs
- Platform monitoring
- Backup and recovery
- Multi-region design
- RTO and RPO

### Plan

1. Create cost governance framework.
2. Design audit and observability flow.
3. Draft DR architecture.
4. Produce runbook for platform incidents.

