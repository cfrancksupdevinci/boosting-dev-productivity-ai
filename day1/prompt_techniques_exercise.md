
## 1- Zero-shot vs. Few-shot Prompting

**Task:** Create both zero-shot and few-shot versions of a prompt for the same task.

**Instructions:**
1. Choose the task: Classifying technical support questions into categories (Hardware, Software, Network, Account, Other)
2. Write a zero-shot prompt asking the AI to categorize a support question
3. Write a few-shot prompt with 3 examples showing the desired categorization pattern

**Example**:
- Zero Shot:
```
Analyze the sentiment of the following statement: ‘The movie was fantastic, and I would watch it again!'
```
- Few Shots:
```
Example 1: “I love this product! It works perfectly.” 
- Positive
Example 2: “This is terrible. I want a refund.” 
- Negative
Example 3: “The service was quick and the staff was friendly.” 
- Positive
“The product broke after one use. It’s a waste of money.” 
```

## 2- Role Prompting

**Task:** Create a prompt that uses role prompting to generate better technical documentation.

**Instructions:**
1. Develop a prompt that assigns the AI a specific role (e.g., "Senior Technical Writer with 15 years of experience in API documentation")
2. Include specific personality traits and expertise areas in your role description
3. Ask the AI to document a simple function that converts temperature between Celsius and Fahrenheit
4. Be specific about the documentation style you want (e.g., clear examples, parameter descriptions, error handling notes)


## 3-  Chain-of-Thought Prompting

**Task:** Create a prompt that encourages step-by-step reasoning for a debugging scenario.

**Instructions:**
1. Write a prompt that includes a buggy code snippet (choose a language you're familiar with)
2. Ask the AI to debug it using explicit chain-of-thought reasoning
3. Your prompt should specifically request that the AI:
   - Explain what each part of the code is trying to do
   - Trace through the execution with example inputs
   - Identify where things go wrong
   - Explain the fix before showing the corrected code
4. Test your prompt with this buggy sorting function:

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# This function has a subtle bug - can you find it?
```

- Example of Prompt:
```
Here is a Python function. Carefully analyze it step-by-step to understand what it does. Identify if there are any bugs or issues, and suggest a fix if needed. Think step-by-step and explain your reasoning clearly.
```
## 4- Structured Output Control

**Task:** Create a prompt that enforces a specific JSON output structure for an API response.

**Instructions:**
1. Write a prompt that asks the AI to generate a mock response for a weather API
2. Define a specific JSON schema including nested objects and arrays
3. Your schema should include fields for:
   - Current conditions (temperature, humidity, wind speed, etc.)
   - Forecast (array of daily forecasts)
   - Alerts (array of weather warnings if any)
   - Location information
4. Test your prompt for "New York City" weather forecast
5. Check if the AI correctly follows your schema

## 5- Task Decomposition

**Task a:** Practice breaking down a complex development task using prompt decomposition.

**Instructions:**
1. Choose this complex task: "Create a data visualization dashboard for COVID-19 statistics"
2. Write a series of connected prompts that break this down into at least 5 smaller subtasks
3. For each subtask, create a specific prompt with clear instructions
4. Make sure your subtasks follow a logical sequence and build upon each other
5. Include a final prompt that brings all the components together

---
**Task b: Tree of Thoughts:**

Try this prompt for any complex question:
```
Imagine three different experts are answering this question.
All experts will write down 1 step of their thinking,
then share it with the group.
Then all experts will go on to the next step, etc.
If any expert realises they're wrong at any point then they leave.
The question is...
```

## 6- System and User Message Design

**Task:** Design a set of system and user messages for a specialized coding assistant.

**Instructions:**
1. Write a system message that establishes:
   - The AI's role as a specialized assistant (e.g., React developer, database expert)
   - Constraints on how it should respond (e.g., always include comments, prefer certain patterns)
   - Personality traits relevant to the role
2. Create 3 different user messages that request specific help with coding tasks
3. For each user message, write the expected assistant response format


## 7- Guardrails Implementation

**Task:** Create a prompt with effective guardrails for generating code that interacts with a database.

**Instructions:**
1. Write a prompt that asks for code to create a user registration system with database storage
2. Add explicit guardrails to prevent:
   - SQL injection vulnerabilities
   - Storing passwords in plaintext
   - Excessive database calls
   - Missing input validation
3. Your guardrails should be specific and actionable, not just general warnings
4. Test your prompt and evaluate how well the AI adheres to your security requirements

---


## Project: Basic Prompt Components

**Task:** Construct a complete prompt with all core components to help an AI analyze customer reviews for a mobile app.

**Instructions:**
1. Write a prompt that includes clear instructions, relevant context, input data, output instructions, and constraints.
2. Your prompt should ask the AI to analyze 3 different customer reviews and extract sentiment, key issues, and suggestions.
3. Make sure to specify the exact format you want for the output.

**Example Customer Reviews to Include:**
- "This app is incredibly slow to load and crashes frequently. The design is nice though."
- "Love the new update! The user interface is much cleaner and I can finally find everything easily."
- "Average app at best. Does what it needs to but nothing special. Wish it had dark mode."
