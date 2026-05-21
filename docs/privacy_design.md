# Privacy Design

## Core Rule

This project does not train or fine-tune a model on personal resume data.

The system only performs local document loading, text chunking, retrieval, skill matching, and report generation.

## Data Separation

Public repository:

```text
public_docs/
```

Allowed content:

- anonymized resume samples
- synthetic job descriptions
- public GitHub project summaries
- methodology documents
- source code

Local-only folder:

```text
private_data/
```

Should contain, if needed:

- real resume
- private application notes
- real job descriptions
- personal project notes

This folder is ignored by git.

## Vector Store Warning

Even if embeddings do not directly store original text, they may still leak semantic information. Therefore, local vector indexes should not be committed.

```text
vector_store/
```

is ignored by git.

## No-Evidence-No-Claim Rule

Generated reports should not create resume claims that cannot be supported by retrieved evidence.

If the evidence base does not support a JD requirement, the system should state this as a skill gap.
