# Prompts 

These are templates of prompts that can be used as starting point.

- [A. Prompt for generating the Software Requirements Document ]
- [B. Prompt for generating the User Stories]
- [C. Prompt for generating the Use Cases]

## A. Prompt for generating the Software Requirements Document 

````xml
<context>
You will act as a software project specialist with an emphasis on requirements development. Your role is to assist in generating analysis artifacts to guide the modelling and construction of the technical solution. Based on the {{SYSTEM DESCRIPTION}} listed in <attachment>, prepare the Software Requirements Document (SRD). To do this, follow the instructions defined in <instructions>.
<context>

<attachment>
- system-description.md
</attachment>

<instructions>
1. Generate the Software Requirements Document (SRD) following the <template> markdown and save it with the name `requirements-document.md`.
</instructions>

<template>
# Software Requirements Document (SRD)

## 1. Project Identification

- **Project Name:**
- **Document Version:**
- **Date:**
- **Author(s):**

---

## 2. Document Purpose

This document aims to describe, in a clear and organized manner, the functional and non-functional requirements necessary for the development of the proposed system, in addition to presenting the business rules, and constraints associated with the project.

---

## 3. System Overview

- **System Description:**
Brief overview of what the system will accomplish. 
- **System Objectives:**
What problems does the system solve or what value does it deliver?
- **Target Audience/End Users:**
Who will use the system and for what purpose?
- **General Functional Scope:**
What areas or processes will the system cover?

---

## 4. Functional Requirements

List of functionalities that the system must perform.

| Code | Name | Description | Acceptance Criteria | Priority |
|--------|------------------------|------------------------------------------------------|--------------------------------------------|------------|
| RF01 | | | | High |
| RF02 | | | | Medium |

---

## 5. Non-Functional Requirements

System quality aspects (performance, security, usability, etc.).

| Code | Type | Description | Priority |
|--------|------------------------|------------------------------------------------------|------------|
| RNF01 | | | High |
| RNF02 | | | Medium |

---

## 6. Business Rules

Set of rules that define the logical behaviour of the system.

| Code | Description |
|---------|-----|
| RN01 | |
| RN02 | |

---

## 7. Integration Requirements

Integrations with other systems, services, APIs, or databases.

-
-

---

## 8. Technical Restrictions

Required technologies, supported platforms, architectural standards, or limitations imposed by the project context.

-
-

---

## 9. General Acceptance Criteria

Objective criteria that must be met for the system to be considered ready for delivery.

-
-

---

## 10. Annexes/References

Links, diagrams, external documents, or supplementary materials used in the preparation of this Software Requirements Document.

</template>

````

## B. Prompt for generating the User Stories

````xml
<context>
You will act as a software project specialist with an emphasis on requirements development. Your role is to assist in generating analysis artifacts to guide the modelling and construction of the technical solution. Based on the {{SYSTEM DESCRIPTION}} and {{REQUIREMENTS DOCUMENT}} listed in <attachment>, develop the User Stories document. To do this, follow the instructions defined in <instructions>.
<context>

<attachment>
- system-description.md
- requirements-document.md
</attachment>

<instructions>
1. Generate the User Stories document following the <template> markdown and save it with the name `requirements-user-stories.md`. 
</instructions>

<template>
# User Stories

User stories to guide product development.

---

# Product Backlog

Backlog with a summary of the prioritized user stories to guide product development.

---

## Column Legend
- **ID**: Story identifier code (e.g., US001)
- **User Story**: Desire described from the user's perspective
- **Priority**: High / Medium / Low
- **Status**: To Do / In Progress / Completed / In Validation

---

## Backlog

| ID | User Story | Priority | Status |
|-------|-----|-----|-------|---------|
| US001 | As a [user], I want [action/function] for [benefit/value] | High | In Progress |
| US002 | As a [user], I want [action/function] for [benefit/value] | Medium | To Do |
| US003 | As a [user], I want [action/function] for [benefit/value] | Low | To Do |

---

## Template for New Story

### ID: USXXX

**User Story:**
As a [user type], I want [desired functionality] for [expected value/benefit].

**Priority:** High | Medium | Low

**Acceptance Criteria:**
- [Criterion 1] Given [a context] when [some action is carried out] then [a set of observable consequences]
- [Criterion 2] Given [a context] when [some action is carried out] then [a set of observable consequences]
- [Criterion 3] Given [a context] when [some action is carried out] then [a set of observable consequences]

---

## General Observations

- Stories must be understandable to all stakeholders.
- Acceptance criteria help align development and testing.
- The backlog is alive: it can (and should) be adjusted as the project evolves.
</template>
````

## C. Prompt for generating the Use Cases

````xml
<context>
You will act as a software project specialist with an emphasis on requirements development. Your role is to assist in generating analysis artifacts to guide the modelling and construction of the technical solution. Based on the {{SYSTEM DESCRIPTION}}, {{REQUIREMENTS DOCUMENT}} and {{USER STORIES}} listed in <attachment>, prepare the Use Cases. To do this, follow the instructions defined in <instructions>.
<context>

<attachment>
- system-description.md
- requirements-document.md
- requirements-user-stories.md
</attachment>

<instructions>
1. Generate Use Cases following the <template> markdown and save it with the name `requirements-use-cases.md`.
</instructions>

<template>
# Use Cases

## 1. Use Cases

Interactions between users and the system, described in a narrative or structured manner.

### Example Use Case
- **Identifier:** UC001
- **Name:**
- **Main Actor:**
- **Description:**
- **Main Flow:**
1.
2.
- **Alternative Flows / Exceptions:**

---
</template>

````
