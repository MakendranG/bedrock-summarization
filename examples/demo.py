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

---

### File: `examples/sample.txt`
```
Amazon Reports Strong Q3 2024 Results Driven by AWS Growth

Seattle, WA - Amazon.com, Inc. announced its financial results for the third quarter of 2024, showing robust performance across key business segments. The company reported net sales of $143.1 billion, representing a 13% year-over-year increase.

Amazon Web Services (AWS), the company's cloud computing division, continued to be a major growth driver with revenue reaching $23.1 billion, up 12% from the same period last year. AWS operating income grew to $7.0 billion, demonstrating strong operational efficiency and customer demand for cloud services.

"We're seeing continued momentum in our AWS business as customers of all sizes turn to the cloud to drive innovation and reduce costs," said Andy Jassy, Amazon CEO. "Our investments in generative AI capabilities, including Amazon Bedrock, are resonating strongly with enterprise customers."

The retail segment also showed positive trends, with North American sales growing 9% to $87.9 billion and International sales increasing 12% to $32.1 billion. The company attributed this growth to improved delivery speeds, expanded product selection, and enhanced customer experience through AI-powered recommendations.

However, Amazon faces ongoing challenges including increased competition in the cloud space from Microsoft Azure and Google Cloud Platform, regulatory scrutiny in multiple jurisdictions, and pressure to improve labor conditions in fulfillment centers. The company also announced plans to invest $10 billion in expanding its logistics network and AI infrastructure over the next two years.

Looking ahead, Amazon provided guidance for Q4 2024, expecting net sales between $160 billion and $167 billion, reflecting the traditional holiday shopping season boost. The company remains optimistic about long-term growth opportunities in cloud computing, artificial intelligence, and e-commerce innovation.
