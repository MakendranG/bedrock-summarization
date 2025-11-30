"""
Example: Creating custom prompt templates
"""

from summarizer import DocumentSummarizer
from prompt_templates import PromptTemplates


class CustomPrompts(PromptTemplates):
    """Extended prompt templates with custom patterns"""
    
    @staticmethod
    def executive_summary(document: str) -> str:
        """Executive summary with business focus"""
        return f"""{document}

Create an executive summary focusing on:
1. Key business metrics and performance indicators
2. Strategic implications and decisions
3. Risk factors and opportunities
4. Action items and recommendations

Keep it concise and actionable."""
    
    @staticmethod
    def technical_summary(document: str) -> str:
        """Technical summary for developers"""
        return f"""{document}

Provide a technical summary covering:
- Architecture and design decisions
- Technologies and tools used
- Implementation challenges
- Performance considerations
- Code examples or patterns mentioned"""
    
    @staticmethod
    def comparison_summary(doc1: str, doc2: str) -> str:
        """Compare two documents"""
        return f"""Document 1:
{doc1}

Document 2:
{doc2}

Compare these documents and highlight:
1. Key similarities
2. Major differences
3. Unique points in each document
4. Overall takeaway"""


def demo_custom_prompts():
    """Demonstrate custom prompt usage"""
    summarizer = DocumentSummarizer()
    custom = CustomPrompts()
    
    article = """
    Our new microservices architecture uses Docker and Kubernetes 
    for container orchestration. We've implemented API Gateway for 
    routing and authentication. Performance improved by 40% with 
    caching strategies. Main challenge was managing distributed 
    transactions across services. Investment: $2M over 6 months.
    """
    
    # Use custom prompt
    prompt = custom.technical_summary(article)
    summary = summarizer._invoke_model(prompt)
    
    print("TECHNICAL SUMMARY:")
    print(summary)


if __name__ == "__main__":
    demo_custom_prompts()
