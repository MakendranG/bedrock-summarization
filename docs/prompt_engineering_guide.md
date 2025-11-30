# Prompt Engineering Guide for Document Summarization

## Best Practices

### 1. Be Specific and Clear
❌ Bad: "Summarize this"
✅ Good: "Write a one-sentence summary focusing on financial metrics"

### 2. Provide Context
Include information about:
- Target audience
- Desired length
- Key topics to focus on
- Format preferences

### 3. Use Examples (Few-Shot Learning)
```
Here's an example of the format I want:
Input: [long article]
Output: "Company X reported Y% growth in Q3..."

Now summarize this article in the same format:
[your article]
```

### 4. Structure Your Prompts
```
{document}

Task: Summarize the above article
Audience: Technical managers
Focus: Infrastructure and scalability
Length: 2-3 sentences
Format: Bullet points
```

## Prompt Patterns

### Pattern 1: Length-Controlled
```python
# Ultra-short
"In 10 words or less, summarize: {document}"

# One sentence
"Write a single sentence summary of: {document}"

# Paragraph
"In 3-4 sentences, summarize: {document}"
```

### Pattern 2: Structured Output
```python
"Summarize under these headings:
- Executive Summary (2 sentences)
- Key Findings (3 bullet points)
- Recommendations (2 bullet points)

Document: {document}"
```

### Pattern 3: Role-Based
```python
"You are a {role}. Summarize this document from your perspective:
{document}"

# Examples:
- financial analyst
- software architect
- marketing manager
- compliance officer
```

### Pattern 4: Comparative
```python
"Compare these two documents and summarize:
1. What they agree on
2. Where they differ
3. Unique insights from each

Document 1: {doc1}
Document 2: {doc2}"
```

### Pattern 5: Question-Focused
```python
"Read this document and answer:
- What problem does it address?
- What solution is proposed?
- What are the results?

Document: {document}"
```

## Temperature Settings

- **0.0-0.3**: Deterministic, factual summaries
- **0.4-0.7**: Balanced creativity and consistency
- **0.8-1.0**: More creative, varied outputs

## Token Management

### Input Optimization
- Remove unnecessary formatting
- Strip extra whitespace
- Focus on content-rich sections

### Output Control
```python
max_tokens = {
    'one-sentence': 100,
    'short': 300,
    'medium': 500,
    'detailed': 1000
}
```

## Common Issues and Solutions

### Issue: Summary is too generic
**Solution**: Add specific focus areas
```python
"Summarize focusing specifically on financial performance and growth metrics"
```

### Issue: Missing key information
**Solution**: Use structured prompts
```python
"Summarize including:
1. Main topic
2. Key statistics
3. Conclusions"
```

### Issue: Inconsistent format
**Solution**: Provide format examples
```python
"Format: 'Company X achieved Y by doing Z'
Now summarize: {document}"
```

## Testing Your Prompts

1. Test with different document lengths
2. Try with various content types
3. Compare multiple temperature settings
4. Validate output consistency
5. Measure quality metrics

## Advanced Techniques

### Chain-of-Thought
```python
"First, identify the main topics in this document.
Then, for each topic, extract the key point.
Finally, combine into a coherent summary.

Document: {document}"
```

### Self-Critique
```python
"Summarize: {document}

Now review your summary and improve it to ensure:
- Accuracy
- Completeness
- Clarity"
```

## Resources

- [Anthropic Prompt Engineering Guide](https://docs.anthropic.com/claude/docs/intro-to-prompting)
- [AWS Bedrock Best Practices](https://docs.aws.amazon.com/bedrock/)


