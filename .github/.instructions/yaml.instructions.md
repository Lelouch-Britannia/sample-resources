---
applyTo: '**'
---

**Purpose**: Generate or convert Kubernetes learning content into structured JSON files for KubePlayground. Focus on real-world use cases and common pitfalls.

---

## CONTENT SOURCES

Always consult these sources when generating or converting content. Prioritize in order listed.

### 1. Official Kubernetes Documentation
Base URL: `https://kubernetes.io/docs`

### 2. Notion — K8s Mastery
Internal workspace. Filter: **Status = Done**. Use for curated explanations and exercise ideas.

### 3. KubeLabs Reference
Located at `references/` in this repo (git submodule of https://collabnix.github.io/kubelabs/).

### Topic Source Map
Full mapping of topics → KubeLabs dirs, K8s docs URLs, and Notion page URLs is in:
**`.github/.instructions/topic-sources.json`**

Each topic entry has:
- `kubelabs` — path relative to repo root
- `k8s_docs` — exact documentation URLs (not just base URL)
- `notion` — direct page URLs from K8s Mastery DB (Status = Done only)
- `notion_subpages` — child pages of DB entries that contain relevant content

**Scope**: Only generate content for topics listed in `topic-sources.json`. Do not add other topics without explicit instruction.

---

## WORKING WITH VISUAL SOURCES

### KubeLabs Slides

Slide decks in `references/` are HTML + PNG backgrounds. Read slide PNGs directly as images to extract diagram content, architecture flows, and visual explanations.

Slide dirs per topic:
- Pods: `references/Pods101_slides/` → `bg1.png` … `bgN.png`
- ReplicaSet: `references/SlidesReplicaSet101/` → `bg1.png` … `bgN.png`
- Deployment: `references/Deployment101_slides/` → `bg1.png` … `bgN.png`
- Services: `references/Slides_Services101/` → `bg1.png` … `bgN.png`

Read each PNG in order (bg1 → bgN). Extract: diagrams, architecture flows, key bullet points, code examples visible in slides.

### Notion Page Images

Notion pages contain embedded diagrams as S3 presigned URLs. These **expire in ~1 hour** after fetching the page.

Workflow:
1. Fetch Notion page via MCP tool to get current page content
2. Extract image URLs from the page content immediately
3. Fetch each image URL right away — do not save URLs for later use
4. Extract visual content: architecture diagrams, flow charts, timing diagrams, comparison tables

Images in Notion pages are primary sources for architecture diagrams and visual explanations. Prioritize fetching them before writing description content.

---

## CONTENT PHILOSOPHY

### Source priority

| Source | Role |
|---|---|
| K8s official docs + KubeLabs | Primary — theory content, diagrams, accurate spec |
| Notion K8s Mastery (Done only) | Gap-fill only — check for anything not covered in docs/kubelabs |

Theory units are a **recap of K8s docs + KubeLabs**. Notion is a cross-check, not the source.

### Theory units (conceptual)

- **Description = recap/summary of K8s docs + KubeLabs** — consolidate all key concepts from those sources into one readable unit. Do NOT duplicate Notion notes.
- Must cover everything a reader needs to understand the concept without opening the docs.
- Lead with the "why this exists" in one sentence.
- Cover all key mechanics, sub-concepts, and spec fields with concise explanations + code examples.
- Mandatory sections: **When to Use**, **Common Pitfalls** (with fixes).
- Target 1500–3000 chars — enough to be a complete standalone recap.
- Quizzes test practical judgment, not memorization.

### Practice units (coding)

Real-world scenarios over toy examples. Every exercise should map to something an SRE or platform engineer actually does:

- Deploy a web app with X replicas and verify self-healing
- Expose a service internally vs externally and explain why
- Reproduce a real failure (wrong image, missing label, port mismatch) and fix it
- Configure resource limits and observe OOMKill behavior
- Roll out an update, break it, roll back

Steps should mirror real workflow: write manifest → apply → verify → debug.

**One concept per exercise.** Don't combine unrelated things.

### Topic ratio

Each topic should have: **2–3 conceptual units** + **4–6 coding units**. Heavy on practice.

---

## FILE FORMAT

One `.json` file per unit. No separate files.

### Directory Structure

```
k8s/
  <course-slug>/
    course.json          ← course metadata (one per course)
    <topic-slug>/
      topic.json         ← topic metadata (one per topic)
      01-unit-name.json  ← unit file
      02-unit-name.json
```

### course.json

```json
{
  "slug": "kubernetes-fundamentals",
  "name": "Kubernetes Fundamentals",
  "description": "One sentence describing the course."
}
```

### topic.json

```json
{
  "slug": "pods101",
  "name": "Pods 101",
  "order": 1,
  "icon": "📦",
  "course_slug": "kubernetes-fundamentals"
}
```

---

## UNIT TEMPLATES

### Coding Unit

```json
{
  "slug": "kubernetes-pod-basic-nginx",
  "title": "Create Your First Nginx Pod",
  "order_index": 4,
  "type": "coding",
  "difficulty": "beginner",
  "description": "Markdown string. Focus on WHY and WHEN, not just HOW.\n\n## Overview\n...\n\n## Common Pitfalls\n- Pitfall 1\n- Pitfall 2",
  "steps": [
    "Imperative action step 1",
    "Imperative action step 2"
  ],
  "hints": [
    "Hint that guides without revealing solution"
  ],
  "editor_config": {
    "language": "yaml",
    "initial_code": "apiVersion: # TODO\nkind: # TODO"
  },
  "_solution": {
    "code_solution": "apiVersion: v1\nkind: Pod\n...",
    "validation_script": "#!/bin/bash\nkubectl apply -f solution.yaml\n..."
  }
}
```

### Conceptual Unit

```json
{
  "slug": "kubernetes-pods-fundamentals",
  "title": "Kubernetes Pods: Core Concepts",
  "order_index": 1,
  "type": "conceptual",
  "difficulty": "beginner",
  "description": "Comprehensive markdown. Must include use cases and pitfalls sections.",
  "quizzes": [
    {
      "id": "q1",
      "question": "Question text?",
      "options": [
        { "id": "a", "text": "Option A" },
        { "id": "b", "text": "Option B" },
        { "id": "c", "text": "Option C" },
        { "id": "d", "text": "Option D" }
      ]
    }
  ],
  "_solution": {
    "quiz_answers": { "q1": "b" },
    "quiz_explanations": { "q1": "Why b is correct and others are wrong." }
  }
}
```

---

## FIELD RULES

### Required for all units
| Field | Rule |
|---|---|
| `slug` | lowercase-hyphens, unique across all units |
| `title` | max 50 chars, no "Exercise N:" prefix |
| `order_index` | sequential integer, unique within topic |
| `type` | `"coding"` or `"conceptual"` |
| `difficulty` | `"beginner"` / `"intermediate"` / `"advanced"` |
| `description` | markdown string (see below) |

### Coding-only required
- `steps` — 4-6 imperative action items
- `editor_config` — language + initial_code with TODOs
- `_solution.code_solution` — complete working solution
- `_solution.validation_script` — bash script, exits 0 on pass

### Conceptual-only required
- `quizzes` — 3-6 questions (even if quiz UI is disabled — content is preserved)
- `_solution.quiz_answers` + `_solution.quiz_explanations`

### Optional for all
- `hints` — 2-4 items max, never reveal the solution
- `difficulty` — omit if not applicable

---

## DESCRIPTION WRITING

### Coding units (300–600 chars)
```markdown
One sentence: what you're building and the core concept being practiced.

**Focus**: The specific skill this exercise develops.

Brief context: when this pattern appears in real Kubernetes work.

## Common Pitfalls
- Pitfall with fix
- Pitfall with fix
```

### Conceptual units (1500–3000 chars — full recap of K8s docs + KubeLabs)
```markdown
One sentence overview: what this is and why Kubernetes has it.

## Overview
Explain the concept with real motivation — what problem it solves.

## Key Concepts

### Concept Name
Explanation + code example.

```yaml
# concrete example
```

### Another Concept
Explanation.

## When to Use
- Production scenario 1
- Production scenario 2
- Production scenario 3

## Common Pitfalls
- **Pitfall**: Description. **Fix**: How to resolve.
- **Pitfall**: Description. **Fix**: How to resolve.
- **Pitfall**: Description. **Fix**: How to resolve.

## Real-World Applications
- Use case 1
- Use case 2
```

**Rules:**
- Explain WHY, not just HOW
- Include 2–4 code examples for conceptual units
- "Common Pitfalls" section is mandatory — this is the most valuable part
- "When to Use" (or "Real-World Applications") is mandatory
- Use `**Important**`, `**Note**`, `**Warning**` callouts for critical info

---

## QUIZ RULES

- 3–4 questions for beginner, 4–5 intermediate, 5–6 advanced
- Every question tests something explicitly in the description
- ONE clearly correct answer — no "all of the above"
- Distractors must be plausible (based on real misconceptions)
- Randomize correct option position — don't cluster at `b`
- Question types: conceptual, comparison, troubleshooting, application, best-practice
- Explanations: 2–5 sentences, explain why wrong answers fail

**NEVER put answers in the public `quizzes` array.**

---

## VALIDATION SCRIPT RULES

```bash
#!/bin/bash
# Apply the manifest
kubectl apply -f solution.yaml

# Check specific condition
result=$(kubectl get <resource> <name> -o jsonpath='...' 2>/dev/null)
if [ "$result" = "expected" ]; then
  echo "✓ Description of what passed"
  exit 0
fi

echo "✗ Description of what failed"
kubectl describe <resource> <name> | tail -20
exit 1
```

- Always `exit 0` on pass, non-zero on fail
- Echo `✓`/`✗` messages for each check
- Include diagnostic output on failure (`kubectl describe`)
- Check the actual requirement — not just "pod exists"
- Use `timeout` for resources that may take time

---

## SLUG RULES

Format: `{tech}-{resource}-{specific-concept}`

Examples:
- `kubernetes-pod-basic-nginx`
- `kubernetes-deployment-rolling-update`
- `kubernetes-replicaset-scaling`

- Lowercase, hyphens only
- Max 50 chars
- Must be globally unique across all topics/courses

---

## FILE NAMING

`{order_index:02d}-{short-description}.json`

Examples: `01-pods-fundamentals.json`, `04-first-nginx-pod.json`

---

## QUALITY CHECKLIST

**All units:**
- [ ] slug is unique and follows `tech-resource-concept` pattern
- [ ] title ≤ 50 chars
- [ ] description includes "Common Pitfalls" section
- [ ] difficulty matches actual complexity

**Coding units:**
- [ ] steps are imperative (Create, Add, Configure, Expose)
- [ ] initial_code has TODOs at every blank
- [ ] validation_script checks the actual requirement
- [ ] validation_script exits 0 on success
- [ ] `_solution` has both `code_solution` and `validation_script`

**Conceptual units:**
- [ ] description 1500–3000 chars (complete recap of K8s docs + KubeLabs)
- [ ] includes "When to Use" or "Real-World Applications"
- [ ] includes "Common Pitfalls" with fixes
- [ ] 2–4 code examples in description
- [ ] 3–6 quiz questions
- [ ] no answers in public `quizzes` array
- [ ] quiz explanations reference description content
