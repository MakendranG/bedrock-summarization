"""
Reusable prompt templates for document summarization
"""

from typing import List, Optional


class PromptTemplates:
    """
    Collection of prompt templates for various summarization tasks
    """
    
    @staticmethod
    def basic_summary(document: str) -> str:
        """Basic summarization prompt"""
        return f"""{document}

Summarize the above article:"""
    
    @staticmethod
    def one_sentence(document: str) -> str:
        """One-sentence summary prompt"""
        return f"""{document}

Write a one-sentence summary of the above content:"""
    
    @staticmethod
    def short_summary(document: str) -> str:
        """Short paragraph summary prompt"""
        return f"""{document}

In a couple of sentences, briefly summarize the above article:"""
    
    @staticmethod
    def structured_summary(document: str, sections: List[str]) -> str:
        """Structured summary with specific sections"""
        sections_str = ", ".join(sections)
        return f"""{document}

Summarize the above article under the following headings: {sections_str}"""
    
    @staticmethod
    def personalized_summary(document: str, role: str, 
                           focus: Optional[str] = None) -> str:
        """Role-based personalized summary"""
        focus_text = f"Focus on {focus}." if focus else ""
        return f"""{document}

Concisely summarize the above article from a {role}'s perspective. {focus_text}"""
    
    @staticmethod
    def simplified_summary(document: str, reading_level: str) -> str:
        """Simplified summary for specific reading level"""
        return f"""{document}

Summarize the above article so that a {reading_level} can understand it:"""
    
    @staticmethod
    def topic_focused(document: str, topic: str) -> str:
        """Summary focused on a specific topic"""
        return f"""{document}

In a couple of sentences, briefly summarize any information about {topic} in the article:"""
    
    @staticmethod
    def custom_prompt(document: str, instruction: str) -> str:
        """Custom summarization with user-defined instruction"""
        return f"""{document}

{instruction}"""


# Predefined role templates
class RoleTemplates:
    """Common role-based summarization templates"""
    
    FINANCIAL_ANALYST = {
        "role": "financial analyst",
        "focus": "areas that could impact profitability or growth of the company"
    }
    
    CTO = {
        "role": "Chief Technology Officer",
        "focus": "technology developments and innovations that might appeal to IT leaders"
    }
    
    MARKETING_MANAGER = {
        "role": "marketing manager",
        "focus": "customer trends, market opportunities, and brand implications"
    }
    
    OPERATIONS_MANAGER = {
        "role": "operations manager",
        "focus": "efficiency improvements, process optimizations, and operational challenges"
    }
    
    HR_DIRECTOR = {
        "role": "HR director",
        "focus": "workforce impacts, talent requirements, and organizational changes"
    }
