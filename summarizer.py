"""
AWS Bedrock Document Summarizer
Provides intelligent document summarization using Claude 3 via Amazon Bedrock
"""

import boto3
import json
from typing import Optional, List
from prompt_templates import PromptTemplates


class DocumentSummarizer:
    """
    Main class for document summarization using Amazon Bedrock
    """
    
    def __init__(self, region: str = 'us-east-1', model_id: str = None):
        """
        Initialize the summarizer with AWS Bedrock client
        
        Args:
            region: AWS region for Bedrock service
            model_id: Specific model ID to use (defaults to Claude 3 Sonnet)
        """
        self.bedrock = boto3.client('bedrock-runtime', region_name=region)
        self.model_id = model_id or 'anthropic.claude-3-sonnet-20240229-v1:0'
        self.templates = PromptTemplates()
    
    def _invoke_model(self, prompt: str, max_tokens: int = 1024, 
                     temperature: float = 0.7) -> str:
        """
        Internal method to invoke the Bedrock model
        
        Args:
            prompt: The prompt to send to the model
            max_tokens: Maximum tokens in response
            temperature: Sampling temperature (0-1)
            
        Returns:
            Model response as string
        """
        body = json.dumps({
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": max_tokens,
            "temperature": temperature,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        })
        
        try:
            response = self.bedrock.invoke_model(
                modelId=self.model_id,
                body=body
            )
            
            response_body = json.loads(response['body'].read())
            return response_body['content'][0]['text']
            
        except Exception as e:
            raise Exception(f"Error invoking Bedrock model: {str(e)}")
    
    def basic_summary(self, document: str) -> str:
        """
        Generate a basic summary of the document
        
        Args:
            document: Text content to summarize
            
        Returns:
            Summary text
        """
        prompt = self.templates.basic_summary(document)
        return self._invoke_model(prompt)
    
    def one_sentence_summary(self, document: str) -> str:
        """
        Generate a one-sentence summary
        
        Args:
            document: Text content to summarize
            
        Returns:
            One-sentence summary
        """
        prompt = self.templates.one_sentence(document)
        return self._invoke_model(prompt, max_tokens=256)
    
    def short_summary(self, document: str) -> str:
        """
        Generate a short paragraph summary (2-3 sentences)
        
        Args:
            document: Text content to summarize
            
        Returns:
            Short summary
        """
        prompt = self.templates.short_summary(document)
        return self._invoke_model(prompt, max_tokens=512)
    
    def structured_summary(self, document: str, 
                          sections: List[str]) -> str:
        """
        Generate a structured summary with specific sections
        
        Args:
            document: Text content to summarize
            sections: List of section headings to organize summary
            
        Returns:
            Structured summary with sections
        """
        prompt = self.templates.structured_summary(document, sections)
        return self._invoke_model(prompt)
    
    def personalized_summary(self, document: str, role: str, 
                           focus: Optional[str] = None) -> str:
        """
        Generate a summary personalized for a specific role
        
        Args:
            document: Text content to summarize
            role: Target role (e.g., "financial analyst", "CTO")
            focus: Specific areas to focus on (optional)
            
        Returns:
            Role-specific summary
        """
        prompt = self.templates.personalized_summary(document, role, focus)
        return self._invoke_model(prompt)
    
    def simplified_summary(self, document: str, 
                          reading_level: str = "third-grader") -> str:
        """
        Generate a simplified summary for a specific reading level
        
        Args:
            document: Text content to summarize
            reading_level: Target reading level (e.g., "third-grader", "high school student")
            
        Returns:
            Simplified summary
        """
        prompt = self.templates.simplified_summary(document, reading_level)
        return self._invoke_model(prompt)
    
    def topic_focused_summary(self, document: str, topic: str) -> str:
        """
        Generate a summary focused on a specific topic
        
        Args:
            document: Text content to summarize
            topic: Specific topic to focus on
            
        Returns:
            Topic-focused summary
        """
        prompt = self.templates.topic_focused(document, topic)
        return self._invoke_model(prompt)


# Example usage
if __name__ == "__main__":
    # Initialize summarizer
    summarizer = DocumentSummarizer()
    
    # Sample document
    sample_doc = """
    Amazon Web Services (AWS) continues to lead the cloud computing market 
    with innovative services and strong customer adoption. In the latest quarter, 
    AWS revenue grew 12% year-over-year, reaching $23.1 billion. The company 
    launched several new machine learning and AI services, including enhanced 
    capabilities for Amazon Bedrock, which provides access to foundation models 
    from leading AI companies. AWS also expanded its infrastructure footprint 
    with new regions in Asia and Europe. Customer demand remains strong across 
    all segments, from startups to enterprise clients. However, the company 
    faces increasing competition from Microsoft Azure and Google Cloud Platform.
    """
    
    # Generate different types of summaries
    print("=== ONE-SENTENCE SUMMARY ===")
    print(summarizer.one_sentence_summary(sample_doc))
    print("\n=== SHORT SUMMARY ===")
    print(summarizer.short_summary(sample_doc))
    print("\n=== STRUCTURED SUMMARY ===")
    print(summarizer.structured_summary(
        sample_doc, 
        ["Business Performance", "New Developments", "Challenges"]
    ))
    print("\n=== FINANCIAL ANALYST SUMMARY ===")
    print(summarizer.personalized_summary(
        sample_doc, 
        "financial analyst",
        "profitability and growth metrics"
    ))
