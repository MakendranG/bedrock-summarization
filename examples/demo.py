"""
Demo script showing various summarization capabilities
"""

from summarizer import DocumentSummarizer


def main():
    # Initialize summarizer
    summarizer = DocumentSummarizer()
    
    # Sample article about technology trends
    article = """
    The artificial intelligence industry experienced remarkable growth in 2024, 
    with generative AI applications becoming mainstream across enterprises. 
    Large language models like GPT-4 and Claude demonstrated unprecedented 
    capabilities in natural language understanding and generation. Companies 
    invested heavily in AI infrastructure, with cloud providers reporting 
    significant increases in GPU capacity. However, concerns about AI safety, 
    bias, and job displacement remained prominent. Regulatory frameworks 
    began emerging globally, with the EU leading with comprehensive AI 
    legislation. The technology sector also faced challenges including 
    supply chain constraints for AI chips and rising energy costs for 
    model training. Despite these hurdles, venture capital funding for 
    AI startups reached record levels, indicating strong confidence in 
    the technology's future potential.
    """
    
    print("="*80)
    print("DOCUMENT SUMMARIZATION DEMO")
    print("="*80)
    
    # Demo 1: One-sentence summary
    print("\n1. ONE-SENTENCE SUMMARY")
    print("-" * 40)
    result = summarizer.one_sentence_summary(article)
    print(result)
    
    # Demo 2: Short summary
    print("\n2. SHORT SUMMARY (2-3 sentences)")
    print("-" * 40)
    result = summarizer.short_summary(article)
    print(result)
    
    # Demo 3: Structured summary
    print("\n3. STRUCTURED SUMMARY")
    print("-" * 40)
    sections = ["Key Developments", "Challenges", "Market Outlook"]
    result = summarizer.structured_summary(article, sections)
    print(result)
    
    # Demo 4: Financial analyst perspective
    print("\n4. FINANCIAL ANALYST PERSPECTIVE")
    print("-" * 40)
    result = summarizer.personalized_summary(
        article,
        role="financial analyst",
        focus="investment opportunities and market risks"
    )
    print(result)
    
    # Demo 5: CTO perspective
    print("\n5. CTO PERSPECTIVE")
    print("-" * 40)
    result = summarizer.personalized_summary(
        article,
        role="Chief Technology Officer",
        focus="technical innovations and infrastructure requirements"
    )
    print(result)
    
    # Demo 6: Simplified for younger audience
    print("\n6. SIMPLIFIED VERSION")
    print("-" * 40)
    result = summarizer.simplified_summary(article, "middle school student")
    print(result)
    
    # Demo 7: Topic-focused summary
    print("\n7. TOPIC-FOCUSED: AI Safety")
    print("-" * 40)
    result = summarizer.topic_focused_summary(article, "AI safety and regulation")
    print(result)
    
    print("\n" + "="*80)
    print("Demo complete!")


if __name__ == "__main__":
    main()
```

