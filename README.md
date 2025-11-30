# AWS Bedrock Document Summarization

An intelligent document summarization system built with Amazon Bedrock and Claude 3.

## Features

- 📝 Multiple summary types (one-sentence, short, structured, personalized)
- 🎯 Role-based summaries for different audiences
- 📊 Structured output with custom categories
- ⚡ Fast processing (summaries in seconds)
- 💻 Both CLI and Python API

## Prerequisites

- Python 3.8+
- AWS Account with Bedrock access
- AWS CLI configured
- Claude 3 Sonnet model access in Bedrock

## Installation

```bash
# Clone repository
git clone https://github.com/MakendranG/bedrock-summarization.git
cd bedrock-summarization

# Install dependencies
pip install -r requirements.txt

# Configure AWS
aws configure
```

## Quick Start

```python
from summarizer import DocumentSummarizer

# Initialize
summarizer = DocumentSummarizer()

# Summarize
document = "Your long document text here..."
summary = summarizer.short_summary(document)
print(summary)
```

## Usage

### Command Line

```bash
# Basic summary
python cli.py summarize --input article.txt --type short

# One-sentence summary
python cli.py summarize --input article.txt --type one-sentence

# Structured summary
python cli.py summarize --input article.txt --type structured --sections "Key Points,Challenges,Solutions"

# Role-based summary
python cli.py summarize --input article.txt --type personalized --role "financial analyst"

# Save to file
python cli.py summarize --input article.txt --type short --output summary.txt

# Batch processing
python cli.py batch --input-dir ./documents --output-dir ./summaries
```

### Python API

```python
from summarizer import DocumentSummarizer

summarizer = DocumentSummarizer()

# Load document
with open('article.txt', 'r') as f:
    document = f.read()

# Different summary types
basic = summarizer.basic_summary(document)
one_liner = summarizer.one_sentence_summary(document)
short = summarizer.short_summary(document)

# Structured summary
structured = summarizer.structured_summary(
    document,
    sections=["Key Points", "Challenges", "Opportunities"]
)

# Role-based summary
financial = summarizer.personalized_summary(
    document,
    role="financial analyst",
    focus="profitability and growth"
)

# Simplified for reading level
simple = summarizer.simplified_summary(document, "third-grader")
```

## Configuration

Edit `config.json`:

```json
{
  "model_id": "anthropic.claude-3-sonnet-20240229-v1:0",
  "region": "us-east-1",
  "max_tokens": 1024,
  "temperature": 0.7
}
```

## Project Structure

```
bedrock-summarization/
├── summarizer.py           # Main summarization class
├── prompt_templates.py     # Prompt templates
├── cli.py                  # Command-line interface
├── config.json             # Configuration
├── requirements.txt        # Dependencies
├── examples/
│   ├── demo.py            # Demo script
│   ├── sample.txt         # Sample document
│   └── batch_processing.py
└── tests/
    └── test_summarizer.py
```

## Examples

### Financial Report

```python
report = "Q3 results show 15% revenue growth..."

# For executives
exec_summary = summarizer.personalized_summary(
    report,
    role="executive",
    focus="key metrics"
)

# For investors
investor_summary = summarizer.personalized_summary(
    report,
    role="investor",
    focus="profitability trends"
)
```

### Batch Processing

```python
from pathlib import Path

def process_documents(input_dir, output_dir):
    summarizer = DocumentSummarizer()
    
    for file in Path(input_dir).glob('*.txt'):
        with open(file) as f:
            doc = f.read()
        
        summary = summarizer.short_summary(doc)
        
        output = Path(output_dir) / f"{file.stem}_summary.txt"
        output.write_text(summary)

process_documents('./docs', './summaries')
```

## Cost Estimation

Amazon Bedrock Pricing (Claude 3 Sonnet):
- Input: $0.003 per 1K tokens
- Output: $0.015 per 1K tokens

Typical costs:
- 1,000-word document: ~$0.006
- 10,000 summaries/month: ~$60

## Troubleshooting

### AccessDeniedException

**Solution**: 
1. Check AWS credentials: `aws sts get-caller-identity`
2. Verify Bedrock model access in AWS Console
3. Ensure IAM permissions include `bedrock:InvokeModel`

### Summaries too long/short

**Solution**: Adjust `max_tokens` or be more specific:
```python
"In exactly 2 sentences, summarize: {document}"
```

### Slow responses

**Solution**:
- Reduce document length
- Lower `max_tokens`
- Check network latency

## Best Practices

1. **Document Preparation**: Remove formatting, clean whitespace
2. **Prompt Engineering**: Start simple, then refine
3. **Performance**: Cache summaries, use batch processing
4. **Security**: Never commit credentials, use IAM roles

## Resources

- [Amazon Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)
- [Claude Documentation](https://docs.anthropic.com/)
- [Building an AI-Powered Document Summarization System with Amazon Bedrock Blog]([https://community.aws/](https://builder.aws.com/content/36ClCWN67QPEjgbGXnkFvDuZHFY/building-an-ai-powered-document-summarization-system-with-amazon-bedrock))

---

⭐ Star this repo if you find it helpful!
