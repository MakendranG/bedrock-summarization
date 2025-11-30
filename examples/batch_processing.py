"""
Example: Batch processing multiple documents
"""

from summarizer import DocumentSummarizer
from pathlib import Path
import json


def batch_process_documents(input_dir, output_dir, summary_type='short'):
    """
    Process multiple documents in a directory
    
    Args:
        input_dir: Directory containing input documents
        output_dir: Directory for output summaries
        summary_type: Type of summary to generate
    """
    summarizer = DocumentSummarizer()
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    
    results = []
    
    # Process all .txt files
    for file_path in input_path.glob('*.txt'):
        print(f"Processing: {file_path.name}")
        
        try:
            # Read document
            with open(file_path, 'r', encoding='utf-8') as f:
                document = f.read()
            
            # Generate summary
            if summary_type == 'one-sentence':
                summary = summarizer.one_sentence_summary(document)
            elif summary_type == 'structured':
                summary = summarizer.structured_summary(
                    document,
                    ["Key Points", "Challenges", "Opportunities"]
                )
            else:
                summary = summarizer.short_summary(document)
            
            # Save summary
            output_file = output_path / f"{file_path.stem}_summary.txt"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(summary)
            
            results.append({
                'file': file_path.name,
                'status': 'success',
                'output': str(output_file)
            })
            
        except Exception as e:
            print(f"Error processing {file_path.name}: {str(e)}")
            results.append({
                'file': file_path.name,
                'status': 'error',
                'error': str(e)
            })
    
    # Save processing report
    report_file = output_path / 'batch_report.json'
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n✓ Processed {len(results)} documents")
    print(f"✓ Report saved to {report_file}")


if __name__ == "__main__":
    batch_process_documents(
        input_dir='./documents',
        output_dir='./summaries',
        summary_type='short'
    )
