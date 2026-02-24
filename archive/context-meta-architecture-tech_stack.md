# 🛠️ Technology Stack

> **Status**: Active
> **Last Updated**: 2026-01-17

## Core Framework

### **Framework**

[Next.js 16+](https://nextjs.org) (App Router)

### **Language**

TypeScript

### **Runtime**

Node.js (LTS)

## UI & Presentation

### **Philosophy**

"UI as a Function of State" (JSON-First)

### **Engine**

[`@json-render/react`](https://github.com/vercel-labs/json-render)

- _Usage_: Renders UI components dynamically from Agent-generated JSON schemas.

### **Styling**

#### **Vanilla CSS** (CSS Modules)

- _Constraint_: No Tailwind CSS.
- _Architecture_: Standard CSS variables in `globals.css`.

## Data Architecture

### **Source of Truth**

`src/data/*.json` (Git-based CMS)

### **Validation**

[Zod](https://zod.dev)

### **Pattern**

Feature-Based MVC (ADR-002)

## Infrastructure

### **Package Manager**

npm

### **Linting**

ESLint + Prettier
