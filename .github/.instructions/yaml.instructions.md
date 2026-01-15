---
applyTo: '**'
---

**Purpose**: Convert educational programming/tech resources into structured YAML format for MongoDB seed data, OR generate new exercises and quizzes in the specified YAML format.

**Supports**: Any programming language, framework, or technology (Kubernetes, Python, SQL, MongoDB, Pandas, React, etc.)

---

## MODES OF OPERATION

### Mode 1: CONVERSION
Convert existing learning materials into structured YAML format.

### Mode 2: GENERATION
Create new exercises and quizzes from scratch in the specified YAML format based on user requirements.

---

## INPUT SOURCES

You will receive learning content in various formats, OR requests to generate new content:

**For Conversion:**
- README files with exercise descriptions
- Existing code files (starter templates and solutions)
- Exercise requirements and verification commands
- Step-by-step instructions
- Quiz questions and conceptual content
- Tutorial documentation

**For Generation:**
- Topic/concept specifications
- Learning objectives
- Difficulty level requirements
- Technology/framework specifications
- Desired exercise type (coding vs conceptual)

---

## OUTPUT STRUCTURE

Generate **ONE YAML file per exercise/quiz** following these exact templates:

---

## TEMPLATE 1: CODING EXERCISES

```yaml
# ===== METADATA (Public - LearningUnit) =====
metadata:
  slug: "unique-url-friendly-identifier"  # lowercase, hyphens only
  title: "Exercise Title (max 50 chars)"
  topic: "TopicName"  # e.g., "Python Basics", "SQL Queries", "MongoDB Aggregation", "Kubernetes Pods"
  order_index: 1  # Sequential number
  type: "coding"  # "coding" or "conceptual"
  difficulty: "beginner"  # "beginner", "intermediate", or "advanced"
  
  description: |
    Multi-line markdown description.
    
    **Focus**: What this exercise teaches.
    
    Can include lists, code snippets, multiple paragraphs.
  
  steps:
    - "First actionable step"
    - "Second actionable step"
    - "Third actionable step"
    - "Fourth actionable step"
  
  hints:
    - "Optional hint 1 - helps without giving away solution"
    - "Optional hint 2 - progressive guidance"

# ===== PUBLIC EDITOR CONFIG =====
editor_config:
  language: "python"  # Supported: python, yaml, javascript, sql, mongodb, bash, etc.
  initial_code: |
    # Starter code with TODOs
    def calculate_total(items):
        # TODO: Implement sum calculation
        pass
    
    # Test cases
    print(calculate_total([1, 2, 3]))  # Expected: 6

# ===== PRIVATE DATA (UnitSolution - NEVER exposed) =====
_solution:
  code_solution: |
    # Complete solution
    def calculate_total(items):
        return sum(items)
    
    # Test cases
    print(calculate_total([1, 2, 3]))  # Output: 6
  
  validation_script: |
    #!/bin/bash
    # Verify solution is correct
    python3 solution.py | grep -q "6"
    if [ $? -eq 0 ]; then
      echo "✓ Correct output"
      exit 0
    else
      echo "✗ Test failed"
      exit 1
    fi
  
  quiz_answers: null
  quiz_explanations: null
```

---

## TEMPLATE 2: CONCEPTUAL/QUIZ UNITS

```yaml
# ===== METADATA (Public - LearningUnit) =====
metadata:
  slug: "dataframe-filtering-basics"
  title: "DataFrame Filtering with Pandas"
  topic: "Pandas"
  order_index: 1
  type: "conceptual"
  difficulty: "beginner"  # "beginner", "intermediate", or "advanced"
  
  description: |
    Learn fundamental concepts of filtering DataFrames in Pandas.
    
    ## Overview
    Filtering is one of the most common operations when working with DataFrames. It allows you to 
    extract subsets of data based on conditions, making data analysis more efficient and targeted.
    
    ## Key Concepts
    
    ### Boolean Indexing
    Boolean indexing uses a boolean Series to filter rows. When you apply a condition to a DataFrame 
    column, it creates a mask of True/False values.
    
    ```python
    # Example: Filter rows where age > 25
    df[df['age'] > 25]
    ```
    
    ### Query Method
    The `query()` method provides a more readable way to filter using string expressions:
    
    ```python
    df.query('age > 25 and city == "NYC"')
    ```
    
    ### Multi-Condition Filtering
    Combine multiple conditions using `&` (and), `|` (or), and `~` (not) operators:
    
    ```python
    df[(df['age'] > 25) & (df['salary'] < 50000)]
    ```
    
    **Important**: Always use parentheses around individual conditions when combining them.
    
    ## Common Patterns
    - Filtering with `.loc[]` for label-based selection
    - Filtering with `.iloc[]` for position-based selection
    - Using `.isin()` for membership tests
    - Filtering null values with `.notna()` and `.isna()`
    
    ## Real-World Applications
    - Customer segmentation in marketing data
    - Identifying outliers in financial datasets
    - Filtering time-series data for specific date ranges
  
  steps: null  # No checklist for conceptual units
  hints: null  # No hints for conceptual units

# ===== QUIZ CONFIGURATION (Public - NO answers) =====
# Quizzes must test concepts presented in the description above
quizzes:
  - id: "q1"
    question: "Which syntax correctly filters DataFrame rows where age is greater than 25?"
    options:
      - id: "a"
        text: "df.filter('age > 25')"
      - id: "b"
        text: "df[df['age'] > 25]"
      - id: "c"
        text: "df.select(age > 25)"
      - id: "d"
        text: "df.where['age' > 25]"
  
  - id: "q2"
    question: "What does the query() method return?"
    options:
      - id: "a"
        text: "A new DataFrame with filtered rows"
      - id: "b"
        text: "A boolean Series mask"
      - id: "c"
        text: "The original DataFrame modified in place"
      - id: "d"
        text: "A list of matching row indices"
  
  - id: "q3"
    question: "When combining multiple filter conditions, which operator represents AND?"
    options:
      - id: "a"
        text: "and"
      - id: "b"
        text: "&&"
      - id: "c"
        text: "&"
      - id: "d"
        text: "+"
  
  - id: "q4"
    question: "Why are parentheses required when combining conditions like (df['age'] > 25) & (df['salary'] < 50000)?"
    options:
      - id: "a"
        text: "To improve code readability only"
      - id: "b"
        text: "To ensure correct operator precedence"
      - id: "c"
        text: "Parentheses are optional in this case"
      - id: "d"
        text: "To convert conditions to boolean type"

# ===== NO EDITOR FOR QUIZZES =====
editor_config: null

# ===== PRIVATE DATA (Answer Keys - NEVER exposed) =====
_solution:
  quiz_answers:
    q1: "b"
    q2: "a"
    q3: "c"
    q4: "b"
  
  quiz_explanations:
    q1: "Boolean indexing using df[df['column'] > value] is the standard way to filter DataFrame rows. The condition df['age'] > 25 creates a boolean mask, which is then used to index the DataFrame."
    q2: "The query() method returns a new DataFrame containing only rows that match the specified query string. The original DataFrame remains unchanged."
    q3: "The & operator is used for element-wise AND operations in pandas. The 'and' keyword doesn't work with pandas Series, and && is not valid Python syntax."
    q4: "Parentheses ensure correct operator precedence because bitwise operators (&, |) have higher precedence than comparison operators (>, <, ==). Without parentheses, Python would evaluate the expression incorrectly."
  
  code_solution: null
  validation_script: null
```

---

## CONVERSION RULES

### 1. SLUG GENERATION
- Format: `{topic-keyword}-{exercise-focus}`
- Examples: `python-list-comprehension`, `sql-join-queries`, `mongodb-aggregation-pipeline`, `kubernetes-pod-multi-container`
- Lowercase with hyphens only
- Max 50 characters
- Must be unique across all exercises

### 2. TITLE EXTRACTION
- Extract from exercise heading (remove "Exercise 1:", "Part A:", etc.)
- If no title, create descriptive one
- Max 50 characters
- Examples: "List Comprehensions", "JOIN Queries", "Aggregation Pipeline", "Multi-Container Pods"

### 3. TOPIC DERIVATION
- Extract from folder name or section context
- Examples: `python-basics` → "Python Basics", `sql-queries` → "SQL Queries", `pandas-dataframes` → "Pandas DataFrames", `kubernetes-pods` → "Kubernetes Pods"
- Capitalize properly and use full names (not abbreviations)

### 4. ORDER INDEX
- Use filename prefix if numbered: `01-app.yaml` → `order_index: 1`
- Or sequential based on appearance in README
- Start from 1 for each topic

### 5. DIFFICULTY LEVEL
- **beginner**: Basic concepts, simple operations, clear instructions
- **intermediate**: Multiple concepts, requires problem-solving, some ambiguity
- **advanced**: Complex scenarios, optimization, debugging, production considerations
- Assess based on: prerequisite knowledge, concept complexity, problem-solving required

### 6. DESCRIPTION CRAFTING

**For Coding Exercises:**
- Use existing exercise README descriptions as primary source
- Combine: Overview + Learning objectives + Key concepts from README
- Preserve markdown formatting (bold, lists, code blocks)
- Include "**Focus:**" line if mentioned in source
- Add real-world context if available in README
- Target: 300-600 characters for coding exercises

**For Conceptual Units (COMPREHENSIVE):**

Conceptual units require rich, educational content extracted from ALL available sources:

**Content Sources (prioritize in order):**
1. Dedicated concept README/documentation files
2. Introduction sections from exercise READMEs
3. Related markdown files (e.g., Blue-Green.md, Canary.md)
4. Code comments explaining patterns/concepts
5. Official documentation links (if provided)
6. Generated explanatory content based on the topic

**Required Structure:**
```markdown
Brief overview paragraph explaining what this concept is and why it matters.

## Overview
Detailed introduction to the concept with context.

## Key Concepts

### Concept 1 Name
Explanation of first major concept with examples.

```language
# Code example demonstrating the concept
```

### Concept 2 Name
Explanation of second major concept.

**Important**: Highlight critical gotchas or best practices.

## Common Patterns
- Pattern 1: Description
- Pattern 2: Description
- Pattern 3: Description

## Real-World Applications
- Use case 1
- Use case 2
- Use case 3

## Common Pitfalls
- Mistake 1 and how to avoid it
- Mistake 2 and how to avoid it
```

**Content Guidelines:**
- Target: 1500-3000 characters for conceptual units (much longer than coding exercises)
- Include 2-4 code examples showing the concept in action
- Use proper markdown headers (##, ###) for organization
- Include **Important**, **Note**, or **Warning** callouts
- Add comparisons ("Unlike X, Y does...")
- Explain WHY, not just HOW
- Link concepts to real-world scenarios

**For Generation:**
- Research the topic thoroughly
- Structure content with clear sections
- Include practical code examples
- Add best practices and common pitfalls
- Target 1500-3000 characters

### 7. STEPS EXTRACTION
**For Conversion:**
- Extract requirements from exercise README
- Convert requirements to action-oriented checklist
- ❌ Bad: "Pod Name: app-cache"
- ✅ Good: "Create Pod named 'app-cache'"
- Target 4-6 steps
- Each step must be verifiable
- Use imperative voice (Create, Add, Configure, Verify)

**For Generation:**
- Break down the exercise into logical, actionable steps
- Each step should represent a specific task
- Ensure steps build upon each other
- Target 4-6 steps
- Use imperative voice

### 8. HINTS CRAFTING (Optional)
**For Conversion:**
- Use hints from exercise README if available
- If README doesn't provide hints, create progressive guidance
- Target 2-4 hints maximum
- Each hint should unlock a specific concept or approach
- Examples:
  - "Remember to check the API version for this resource"
  - "Consider what happens when the container port doesn't match the service target port"
  - "Use `kubectl explain pod.spec.containers` to see available fields"
- Set to `null` or omit if no hints needed/available

**For Generation:**
- Provide progressive guidance without revealing solution
- Target 2-4 hints maximum
- Each hint should help learners think through the problem
- Start with conceptual hints, then more specific ones
- Never reveal the complete solution in hints

### 9. INITIAL CODE (Coding Exercises)
- Use existing starter template if available
- If only solution exists: Simplify and add TODOs
- Can include intentional mistakes for learning
- Must be valid code for specified language
- Add helpful comments
- Include test cases or usage examples

**Language-Specific Considerations**:
- **Python**: Include `if __name__ == "__main__":` for runnable code
- **SQL**: Include schema creation if needed
- **MongoDB**: Include collection context
- **YAML/K8s**: Must be valid YAML structure
- **JavaScript**: Include module context if applicable

### 10. SOLUTION CODE (Coding Exercises)
- Use provided solution or create complete version
- Must be fully functional
- Follow language/framework best practices
- Remove TODO comments
- Include all required elements (imports, schemas, etc.)
- Add comments explaining key concepts

### 11. VALIDATION SCRIPT (Coding Exercises)
Extract from "Verification Command" or "Expected Output" sections.

**Script must**:
- Start with `#!/bin/bash`
- Add comments explaining checks
- Exit 0 on success, non-zero on failure
- Echo ✓/✗ messages for pass/fail

**Technology-Specific Examples**:

**Python**:
```bash
#!/bin/bash
# Run tests and check output
python3 solution.py > output.txt
if grep -q "Expected result" output.txt; then
  echo "✓ Test passed"
  exit 0
else
  echo "✗ Test failed"
  exit 1
fi
```

**SQL**:
```bash
#!/bin/bash
# Execute query and verify results
mysql -e "SOURCE solution.sql" | grep -q "expected_value"
if [ $? -eq 0 ]; then
  echo "✓ Query returned correct results"
  exit 0
fi
```

**MongoDB**:
```bash
#!/bin/bash
# Run aggregation and check output
mongosh --quiet < solution.js | grep -q "expected_count"
if [ $? -eq 0 ]; then
  echo "✓ Aggregation successful"
  exit 0
fi
```

**Kubernetes**:
```bash
#!/bin/bash
# Apply manifest and verify
kubectl apply -f solution.yaml
kubectl get pod app -o jsonpath='{.status.phase}' | grep -q "Running"
if [ $? -eq 0 ]; then
  echo "✓ Pod is running"
  exit 0
fi
```

### 12. QUIZ GENERATION (Conceptual Units)

**Purpose**: Quizzes MUST test concepts explicitly covered in the description. Every quiz question should directly relate to material presented above.

**Quiz IDs**: Use `q1`, `q2`, `q3`, etc. (unique within unit)

**Option IDs**: Use `a`, `b`, `c`, `d` (standard 4 options)

**Quantity**: Create 3-6 quiz questions per conceptual unit
- 3-4 questions for beginner concepts
- 4-5 questions for intermediate concepts
- 5-6 questions for advanced concepts

**Question Crafting**:
- Test understanding of concepts from the description, not memorization
- Each question must reference material explicitly covered above
- ONE clearly correct answer
- Avoid "all of the above" or "none of the above"
- Be specific and unambiguous
- Include scenario-based questions ("What happens if...")
- Test practical application, not just definitions

**Question Types to Include**:
1. **Conceptual**: "What is the purpose of X?"
2. **Comparison**: "What's the difference between X and Y?"
3. **Application**: "When should you use X?"
4. **Troubleshooting**: "Why would X fail?"
5. **Best Practice**: "What's the recommended way to do X?"

**Option Crafting**:
- Make distractors plausible (use common misconceptions)
- Similar length and format across all options
- Don't make correct answer obvious (avoid "always/never")
- Randomize correct position (don't always use 'a' or 'b')
- Base incorrect options on actual mistakes learners make

**Explanations** (in `_solution`):
- Explain WHY the correct answer is right
- Reference specific concepts from the description
- Explain why common wrong answers are incorrect
- 2-5 sentences with relevant technical details
- Include best practices or additional insights

**SECURITY**: Never put answers or explanations in public `quizzes` array!

### 13. LANGUAGE-SPECIFIC EXAMPLES

**Python**:
```yaml
editor_config:
  language: "python"
  initial_code: |
    def fibonacci(n):
        # TODO: Implement Fibonacci sequence
        pass
```

**SQL**:
```yaml
editor_config:
  language: "sql"
  initial_code: |
    -- TODO: Write a query to find all users
    SELECT * FROM users;
```

**MongoDB**:
```yaml
editor_config:
  language: "mongodb"
  initial_code: |
    // TODO: Aggregate total sales by category
    db.sales.aggregate([
      // Add your pipeline stages here
    ])
```

**JavaScript/React**:
```yaml
editor_config:
  language: "javascript"
  initial_code: |
    function MyComponent() {
      // TODO: Implement state management
      return <div>Hello</div>;
    }
```

**YAML/Kubernetes**:
```yaml
editor_config:
  language: "yaml"
  initial_code: |
    apiVersion: v1
    kind: Pod
    metadata:
      name: example
    spec:
      # TODO: Add containers
```

---

## QUALITY CHECKLIST

Before submitting YAML, verify:

**Metadata**:
- [ ] slug is unique and descriptive
- [ ] title is clear (max 50 chars)
- [ ] topic is capitalized properly
- [ ] order_index is correct number
- [ ] type is "coding" or "conceptual"
- [ ] difficulty is "beginner", "intermediate", or "advanced"
- [ ] description explains learning objective
- [ ] steps are actionable (4-6 items for coding, null for quiz)
- [ ] hints are helpful without revealing solution (optional)

**Coding Exercises**:
- [ ] initial_code is valid code for specified language
- [ ] code_solution is complete and correct
- [ ] validation_script has proper bash syntax and technology commands
- [ ] validation_script exits 0 on success
- [ ] quiz fields are null
- [ ] Language field matches code syntax (python, sql, yaml, javascript, etc.)

**Conceptual/Quiz Units**:
- [ ] Description is comprehensive (1500-3000 characters)
- [ ] Includes multiple sections (Overview, Key Concepts, Common Patterns, etc.)
- [ ] Contains 2-4 code examples demonstrating concepts
- [ ] Uses proper markdown formatting (##, ###, code blocks)
- [ ] Includes callouts (Important, Note, Warning)
- [ ] Explains WHY concepts matter, not just HOW
- [ ] 3-6 quiz questions that test concepts from description
- [ ] Each quiz has unique id (q1, q2, etc.)
- [ ] Each option has id (a, b, c, d)
- [ ] NO answers in public quiz objects
- [ ] quiz_answers maps quiz_id → option_id
- [ ] quiz_explanations reference concepts from description
- [ ] editor_config is null
- [ ] code fields are null
- [ ] steps and hints are null

**General**:
- [ ] No sensitive data anywhere
- [ ] Markdown formatting preserved
- [ ] YAML indentation is 2 spaces
- [ ] Comments are helpful, not redundant

---

## FILE NAMING

Save as: `{order_index:02d}-{short-slug}.yaml`

Examples:
- `01-list-comprehension.yaml` (Python)
- `02-inner-join.yaml` (SQL)
- `03-aggregation-pipeline.yaml` (MongoDB)
- `04-multi-container-pod.yaml` (Kubernetes)
- `05-usestate-hook.yaml` (React)

---

## EXAMPLE CONVERSIONS

### Example 1: Kubernetes Exercise

**INPUT** (README excerpt):
```markdown
## Exercise 1: The "Dual-Stack" App

Create a Pod with nginx frontend and redis cache.

Requirements:
1. Pod Name: app-cache
2. Container 1: frontend (nginx:alpine, port 80)
3. Container 2: cache (redis:alpine, port 6379)

Verification:
kubectl get pod app-cache -o jsonpath='{.spec.containers[*].ports[*].containerPort}'
# Expected: 80 6379
```

**OUTPUT** (`01-app-cache.yaml`):
```yaml
metadata:
  slug: "kubernetes-pod-multi-container"
  title: "Multi-Container Pod: App + Cache"
  topic: "Kubernetes Pods"
  order_index: 1
  type: "coding"
  difficulty: "beginner"
  description: |
    Create a single Pod with two containers: a frontend web server and a Redis cache.
    
    **Focus**: Understanding `spec.containers` list syntax and exposing multiple ports.
  steps:
    - "Create Pod named 'app-cache'"
    - "Add frontend container using nginx:alpine image"
    - "Expose container port 80 for frontend"
    - "Add cache container using redis:alpine image"
    - "Expose container port 6379 for Redis"
    - "Verify both ports are correctly configured"
  hints:
    - "The spec.containers field is an array - you can add multiple containers"
    - "Each container needs a unique name within the Pod"

editor_config:
  language: "yaml"
  initial_code: |
    apiVersion: v1
    kind: Pod
    metadata:
      name: app-cache
    spec:
      containers:
      - name: frontend
        image: nginx:latest  # TODO: Use nginx:alpine
        ports:
        - containerPort: 80
      # TODO: Add cache container

_solution:
  code_solution: |
    apiVersion: v1
    kind: Pod
    metadata:
      name: app-cache
    spec:
      containers:
      - name: frontend
        image: nginx:alpine
        ports:
        - containerPort: 80
      - name: cache
        image: redis:alpine
        ports:
        - containerPort: 6379
  
  validation_script: |
    #!/bin/bash
    # Check if both ports are exposed
    ports=$(kubectl get pod app-cache -o jsonpath='{.spec.containers[*].ports[*].containerPort}')
    
    if [[ "$ports" == *"80"* ]] && [[ "$ports" == *"6379"* ]]; then
      echo "✓ Both ports (80, 6379) correctly exposed"
      exit 0
    else
      echo "✗ Expected ports: 80 6379, Got: $ports"
      exit 1
    fi
  
  quiz_answers: null
  quiz_explanations: null
```

---

### Example 2: Python Exercise

**INPUT**:
```markdown
## Exercise: Sum of List

Write a function that calculates the sum of all numbers in a list.

Requirements:
- Function name: calculate_sum
- Input: List of numbers
- Output: Integer (sum)
- Handle empty lists (return 0)

Test: [1, 2, 3, 4, 5] should return 15
```

**OUTPUT** (`01-sum-list.yaml`):
```yaml
metadata:
  slug: "python-sum-list-function"
  title: "Calculate Sum of List"
  topic: "Python Basics"
  order_index: 1
  type: "coding"
  difficulty: "beginner"
  description: |
    Write a function to calculate the sum of all numbers in a list.
    
    **Focus**: Using built-in functions and handling edge cases.
  steps:
    - "Define function calculate_sum that takes a list parameter"
    - "Use sum() built-in function to calculate total"
    - "Handle empty list case (return 0)"
    - "Test with sample input [1, 2, 3, 4, 5]"
  hints:
    - "Python has a built-in sum() function for iterables"
    - "Consider what happens with an empty list"

editor_config:
  language: "python"
  initial_code: |
    def calculate_sum(numbers):
        # TODO: Implement sum calculation
        pass
    
    # Test cases
    if __name__ == "__main__":
        result = calculate_sum([1, 2, 3, 4, 5])
        print(f"Sum: {result}")

_solution:
  code_solution: |
    def calculate_sum(numbers):
        """Calculate sum of all numbers in a list."""
        if not numbers:
            return 0
        return sum(numbers)
    
    # Test cases
    if __name__ == "__main__":
        result = calculate_sum([1, 2, 3, 4, 5])
        print(f"Sum: {result}")  # Output: 15
  
  validation_script: |
    #!/bin/bash
    # Run solution and check output
    output=$(python3 solution.py)
    
    if echo "$output" | grep -q "Sum: 15"; then
      echo "✓ Correct sum calculated"
      exit 0
    else
      echo "✗ Expected Sum: 15, Got: $output"
      exit 1
    fi
  
  quiz_answers: null
  quiz_explanations: null
```

---

### Example 3: MongoDB Query Exercise

**INPUT**:
```markdown
## Exercise: Find Top Selling Products

Write a MongoDB aggregation query to find the top 5 products by sales.

Requirements:
- Collection: sales
- Group by product_id
- Calculate total quantity sold
- Sort descending
- Limit to top 5
```

**OUTPUT** (`01-top-products.yaml`):
```yaml
metadata:
  slug: "mongodb-aggregation-top-products"
  title: "Find Top Selling Products"
  topic: "MongoDB Aggregation"
  order_index: 1
  type: "coding"
  difficulty: "intermediate"
  description: |
    Use MongoDB aggregation pipeline to find the top 5 best-selling products.
    
    **Focus**: $group, $sum, $sort, and $limit stages.
  steps:
    - "Use $group stage to group by product_id"
    - "Calculate total quantity with $sum"
    - "Sort by total_quantity in descending order"
    - "Limit results to top 5"
  hints:
    - "Aggregation pipeline stages execute in order - group first, then sort"
    - "Use -1 for descending sort order"

editor_config:
  language: "mongodb"
  initial_code: |
    // Find top 5 products by sales quantity
    db.sales.aggregate([
      // TODO: Add your aggregation pipeline stages
    ])

_solution:
  code_solution: |
    // Find top 5 products by sales quantity
    db.sales.aggregate([
      {
        $group: {
          _id: "$product_id",
          total_quantity: { $sum: "$quantity" }
        }
      },
      {
        $sort: { total_quantity: -1 }
      },
      {
        $limit: 5
      }
    ])
  
  validation_script: |
    #!/bin/bash
    # Run aggregation and verify it returns results
    mongosh test --quiet --eval "$(cat solution.js)" > output.txt
    
    if grep -q "total_quantity" output.txt; then
      echo "✓ Aggregation pipeline executed successfully"
      exit 0
    else
      echo "✗ Aggregation failed or returned no results"
      exit 1
    fi
  
  quiz_answers: null
  quiz_explanations: null
```

---

### Example 4: Kubernetes Conceptual Unit (Comprehensive)

**INPUT** (from Blue-Green.md):
```markdown
# Blue-Green Deployment Strategy

Blue-green deployment is a release strategy that reduces downtime and risk by running two identical production environments.

## How It Works
Only one environment (blue or green) serves production traffic at any time. When deploying a new version, you deploy to the idle environment, test it, then switch traffic.

## Benefits
- Zero-downtime deployments
- Instant rollback capability
- Full testing in production-like environment
```

**OUTPUT** (`01-bluegreen-strategy.yaml`):
```yaml
metadata:
  slug: "kubernetes-deployment-bluegreen-strategy"
  title: "Blue-Green Deployment Strategy"
  topic: "Kubernetes Deployments"
  order_index: 1
  type: "conceptual"
  difficulty: "intermediate"
  
  description: |
    Learn the blue-green deployment strategy for zero-downtime releases in Kubernetes.
    
    ## Overview
    Blue-green deployment is a release strategy that reduces downtime and risk by maintaining 
    two identical production environments ("blue" and "green"). Only one environment serves 
    live traffic at any time, while the other remains idle for staging the next release.
    
    ## Key Concepts
    
    ### Dual Environment Architecture
    The strategy requires two complete, identical production environments:
    - **Blue**: The current production version serving live traffic
    - **Green**: The staging environment for the new version
    
    These environments must be identical in configuration, resources, and infrastructure.
    
    ### Traffic Switching
    Traffic cutover happens at the Service level using label selectors:
    
    ```yaml
    # Before deployment - Service points to blue
    apiVersion: v1
    kind: Service
    metadata:
      name: myapp
    spec:
      selector:
        app: myapp
        version: blue  # Currently serving traffic
      ports:
      - port: 80
    ```
    
    After deploying to green and validating, update the Service selector:
    
    ```yaml
    spec:
      selector:
        app: myapp
        version: green  # Switch traffic to new version
    ```
    
    ### Deployment Process
    1. Deploy new version to the idle environment (green)
    2. Test thoroughly in green environment
    3. Switch Service selector from blue to green
    4. Monitor for issues
    5. Keep blue environment running for quick rollback
    6. After stability confirmed, blue becomes the new staging environment
    
    **Important**: Always verify the green deployment is healthy before switching traffic.
    
    ## Benefits
    - **Zero Downtime**: Traffic switches instantly between environments
    - **Instant Rollback**: Revert Service selector to previous version if issues arise
    - **Production Testing**: Test new version in production-like environment before cutover
    - **Reduced Risk**: New version is fully deployed and validated before receiving traffic
    
    ## Common Patterns
    - Use Deployments with different version labels (blue/green)
    - Single Service that switches between versions
    - Database migrations must be backward compatible
    - Use health checks before switching traffic
    
    ## Real-World Applications
    - Financial services requiring zero downtime
    - E-commerce platforms during high-traffic periods
    - API services with strict SLA requirements
    
    ## Common Pitfalls
    - **Database compatibility**: Schema changes must work with both versions
    - **Resource cost**: Requires 2x infrastructure during deployment
    - **Session handling**: Existing user sessions may break if not handled properly
    - **Stateful applications**: Require careful state management during cutover
  
  steps: null
  hints: null

quizzes:
  - id: "q1"
    question: "What is the primary advantage of blue-green deployment over rolling updates?"
    options:
      - id: "a"
        text: "It uses fewer resources"
      - id: "b"
        text: "It allows instant rollback by switching Service selector"
      - id: "c"
        text: "It's easier to configure"
      - id: "d"
        text: "It works better with stateful applications"
  
  - id: "q2"
    question: "In Kubernetes, how is traffic switched from blue to green environment?"
    options:
      - id: "a"
        text: "By deleting the blue Deployment"
      - id: "b"
        text: "By updating the Service selector labels"
      - id: "c"
        text: "By changing the Ingress rules"
      - id: "d"
        text: "By restarting all pods"
  
  - id: "q3"
    question: "Why must database schema changes be backward compatible in blue-green deployments?"
    options:
      - id: "a"
        text: "To reduce migration time"
      - id: "b"
        text: "To improve database performance"
      - id: "c"
        text: "Because both versions may need to access the database during cutover"
      - id: "d"
        text: "To avoid database locks"
  
  - id: "q4"
    question: "What is the main infrastructure cost consideration with blue-green deployments?"
    options:
      - id: "a"
        text: "Requires additional load balancers"
      - id: "b"
        text: "Needs twice the production resources during deployment"
      - id: "c"
        text: "Requires more storage for logs"
      - id: "d"
        text: "Increases network bandwidth costs"
  
  - id: "q5"
    question: "When should you keep the blue environment running after switching to green?"
    options:
      - id: "a"
        text: "Never, delete it immediately to save costs"
      - id: "b"
        text: "Only during business hours"
      - id: "c"
        text: "Until the green deployment is confirmed stable for quick rollback"
      - id: "d"
        text: "Only if the deployment has database changes"

editor_config: null

_solution:
  quiz_answers:
    q1: "b"
    q2: "b"
    q3: "c"
    q4: "b"
    q5: "c"
  
  quiz_explanations:
    q1: "The primary advantage of blue-green deployment is instant rollback capability. By simply switching the Service selector back to the blue version, you can immediately revert to the previous working version without waiting for pods to roll back."
    q2: "Traffic switching is accomplished by updating the Service's selector labels. When you change the selector from 'version: blue' to 'version: green', the Service immediately starts routing traffic to the green pods. This is a simple, atomic operation."
    q3: "Both the blue and green environments may access the same database during the transition period. If the new schema is incompatible with the old application version, the blue environment would break. Backward compatibility ensures both versions can operate during cutover and enables safe rollback."
    q4: "Blue-green deployment requires running two complete production environments simultaneously during the deployment process. This effectively doubles the infrastructure cost until the old environment is decommissioned. This is the main tradeoff for the safety and instant rollback capability."
    q5: "The blue environment should remain running until you've confirmed the green deployment is stable. This allows for instant rollback if issues are discovered. Only after a monitoring period confirms stability should the blue environment be repurposed for the next deployment cycle."
  
  code_solution: null
  validation_script: null
```

---

## READY TO CONVERT OR GENERATE

**For Conversion:**
Provide the learning content in any format (README, code files, documentation, tutorials) and specify the technology/programming language. I will convert it to the unified YAML format following these instructions. Exercise READMEs will be used as the primary source for descriptions, steps, and hints when available.

**For Generation:**
Specify the topic, learning objectives, difficulty level, and technology/framework. I will generate complete exercises or quizzes in the unified YAML format following these instructions.

**Supported Technologies**: Python, JavaScript, SQL, MongoDB, Kubernetes, React, Pandas, SQLAlchemy, Docker, and any other programming language or framework.
