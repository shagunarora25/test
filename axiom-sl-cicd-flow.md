# Axiom SL CI/CD Flow Diagram

This diagram captures the current process for exporting and importing XML/ZIP objects across environments for Axiom SL.

```mermaid
flowchart TD
    A[Axiom SL object selection]
    A -->|JIRA sub-task ID in notes| B[Filter by JIRA status, labels, components]
    B --> C[Trigger Git build pipeline]
    C --> D[Export objects as XML / ZIP]
    D --> E[Import objects into target environment]
    E --> F[Higher environment promotion link]
    F --> G[Create artifact package]
    G --> H[Artifact approval step]
    H --> I[Generate Nexus link]
    I --> J[Deploy to Production]
    C --> K[Build failure occurs]
    K --> L[Open logs portal by build ID]

    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#ffeb99,stroke:#333,stroke-width:1px
    style C fill:#9fe5e5,stroke:#333,stroke-width:1px
    style D fill:#d5f5e3,stroke:#333,stroke-width:1px
    style E fill:#d5f5e3,stroke:#333,stroke-width:1px
    style F fill:#f0c27b,stroke:#333,stroke-width:1px
    style G fill:#f0c27b,stroke:#333,stroke-width:1px
    style H fill:#f7a1a1,stroke:#333,stroke-width:1px
    style I fill:#b3d9ff,stroke:#333,stroke-width:1px
    style J fill:#c2ffd8,stroke:#333,stroke-width:1px
    style K fill:#ff9999,stroke:#333,stroke-width:1px
    style L fill:#cccccc,stroke:#333,stroke-width:1px

    classDef process fill:#ffffff,stroke:#333,stroke-width:1px;
```

## Current problem flow

1. Objects in Axiom SL are selected using metadata from JIRA:
   - JIRA sub-task number in notes
   - JIRA status
   - Specific labels and components
2. A Git build pipeline exports/imports the selected objects as XML or zipped files.
3. To move items to a higher environment, a separate link is used to create artifacts.
4. Created artifacts require approval before deployment.
5. Once approved, a Nexus link is issued.
6. The Nexus package is deployed into Production.
7. If a pipeline fails, logs are reviewed in a separate portal keyed by build ID.
