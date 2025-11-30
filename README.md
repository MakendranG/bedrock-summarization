# AWS Bedrock Document Summarization

An intelligent document summarization system built with Amazon Bedrock and Claude, demonstrating advanced prompt engineering techniques for generating customized summaries.

## Features

- 📝 **Multiple Summary Types**: One-sentence, short, structured, and personalized summaries
- 🎯 **Role-Based Personalization**: Generate summaries tailored to specific roles (Financial Analyst, CTO, etc.)
- 📊 **Structured Output**: Organize summaries by custom categories
- 👶 **Reading Level Adaptation**: Simplify content for different audiences
- ⚡ **Fast Processing**: Generate summaries in seconds
- 🔧 **Easy Configuration**: Simple JSON-based configuration

## Architecture

The system uses Amazon Bedrock with Claude 3 Sonnet to generate summaries through carefully engineered prompts.
```
User Document → Prompt Templates → Amazon Bedrock → Formatted Summary
```

## Prerequisites

- Python 3.8+
- AWS Account with Bedrock access
- AWS CLI configured with appropriate credentials
- Amazon Bedrock model access (Claude 3 Sonnet)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/bedrock-summarization.git
cd bedrock-summarization
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure AWS credentials:
```bash
aws configure
```

4. Request Amazon Bedrock model access:
   - Go to AWS Console → Amazon Bedrock → Model Access
   - Request access to Claude 3 Sonnet

## Usage

### Basic Summary
```bash
python summarizer.py --input sample.txt --type basic
```

### One-Sentence Summary
```bash
python summarizer.py --input sample.txt --type one-sentence
```

### Structured Summary
```bash
python summarizer.py --input sample.txt --type structured --sections "Pain Points,Positive Results,Growth Opportunities"
```

### Role-Based Summary
```bash
python summarizer.py --input sample.txt --type personalized --role "financial analyst"
```

### Simplified for Reading Level
```bash
python summarizer.py --input sample.txt --type simplified --level "third-grader"
```

## Python API Usage
```python
from summarizer import DocumentSummarizer

# Initialize summarizer
summarizer = DocumentSummarizer(region='us-east-1')

# Load document
with open('article.txt', 'r') as f:
    document = f.read()

# Generate basic summary
summary = summarizer.basic_summary(document)
print(summary)

# Generate structured summary
structured = summarizer.structured_summary(
    document,
    sections=["Key Points", "Challenges", "Solutions"]
)
print(structured)

# Generate role-based summary
personalized = summarizer.personalized_summary(
    document,
    role="CTO",
    focus="technology innovations and developments"
)
print(personalized)
```

## Configuration

Edit `config.json` to customize:
```json
{
  "model_id": "anthropic.claude-3-sonnet-20240229-v1:0",
  "region": "us-east-1",
  "max_tokens": 1024,
  "temperature": 0.7,
  "default_summary_type": "short"
}
```

## Project Structure
```
bedrock-summarization/
├── README.md
├── requirements.txt
├── config.json
├── summarizer.py          # Main summarization class
├── prompt_templates.py    # Reusable prompt templates
├── cli.py                 # Command-line interface
├── examples/
│   ├── sample.txt         # Sample document
│   └── demo.py            # Usage examples
├── tests/
│   └── test_summarizer.py
└── docs/
    └── prompt_engineering_guide.md
```

## Examples

See the `examples/` directory for complete working examples:
- `basic_usage.py` - Simple summarization
- `batch_processing.py` - Process multiple documents
- `custom_prompts.py` - Create your own prompt templates
- `web_integration.py` - Flask API wrapper

## Cost Estimation

Amazon Bedrock pricing (Claude 3 Sonnet):
- Input: $0.003 per 1K tokens
- Output: $0.015 per 1K tokens

Typical costs:
- 1,000-word document summary: ~$0.01-0.02
- 10,000 summaries/month: ~$100-200

## Best Practices

1. **Keep prompts clear and specific** - Well-defined instructions produce better results
2. **Test different temperatures** - Lower (0.3-0.5) for consistency, higher (0.7-0.9) for creativity
3. **Use structured formats** - Helps organize information and improves readability
4. **Validate output** - Implement checks for summary quality and relevance
5. **Monitor costs** - Track token usage to optimize spending

## Troubleshooting

**Issue**: `AccessDeniedException` when calling Bedrock
- **Solution**: Ensure you've requested model access in the Bedrock console

**Issue**: Summaries are too long/short
- **Solution**: Adjust `max_tokens` in config or be more specific in prompts

**Issue**: Poor quality summaries
- **Solution**: Refine your prompts with more specific instructions and examples

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License - see LICENSE file for details

## Resources

- [Amazon Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)
- [Claude Prompt Engineering Guide](https://docs.anthropic.com/claude/docs/intro-to-prompting)
- [AWS Builder Center Blog Post](https://community.aws/content/your-article-link)

## Support

For questions or issues:
- Open a GitHub issue
- Contact: your.email@example.com
- AWS Support for Bedrock-specific issues

## Acknowledgments

Built as part of the AWS Prompt Engineering Workshop series.
```

---

### File: `requirements.txt`
```
boto3>=1.34.0
python-dotenv>=1.0.0
click>=8.1.0
