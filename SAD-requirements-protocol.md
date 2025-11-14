# 📌 LLM Adoption Protocol – Helping with requirements

## 🎯 Objective

The main objective is to use Copilot to help in expanding the problem system description into user stories and user cases that can be used as input for the several design activities to be performed in the module.

## 📘 Activities and Interactions with LLMs

| Activity | LLM Role | Artifact(s) |
|---|---|---|
| Requirements Document Development | Assistance in structuring and detailing requirements based on initial description | Software Requirements Document (SRD) (`requirements-document.md`) |
| User stories development | Support for the creation and refinement of user stories with acceptance criteria and product backlog | Product Backlog (`requirements-user-stories.md`) |
| Use cases development | Support for the creation of use cases | Use Cases (`requirements-use-cases.md`) |

````mermaid
flowchart TD
A[Requirements Document Development]
B[User Stories and Backlog Development]
C[Use Case Development]

A --> B --> C
````

## 🔗 Prompts

- [A. Prompt for generating the Software Requirements Document](./SAD-requirements-prompt.md)
- [B. Prompt for generating the User Stories](./SAD-requirements-prompt.md)
- [C. Prompt for generating the Use Cases](./SAD-requirements-prompt.md)

## 📂 Artifact Models

- [Software Requirements Document (SRD)](./artifact/analysis-document.md)
- [Product Backlog](./artifact/analysis-backlog.md)

## 🛠️ Recommended Instrumentation

- Recording of prompts and outputs
- Logging of interactions with LLMs (acceptance/rejection of suggestions)
- Version control of artifacts (e.g., Git)
- Recording of time per activity
