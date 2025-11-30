"""
Command-line interface for document summarization
"""

import click
import json
from pathlib import Path
from summarizer import DocumentSummarizer


@click.group()
def cli():
    """AWS Bedrock Document Summarization CLI"""
    pass


@cli.command()
@click.option('--input', '-i', required=True, type=click.Path(exists=True),
              help='Input document file path')
@click.option('--type', '-t', default='short',
              type=click.Choice(['basic', 'one-sentence', 'short', 'structured', 
                               'personalized', 'simplified']),
              help='Type of summary to generate')
@click.option('--sections', '-s', default=None,
              help='Comma-separated sections for structured summary')
@click.option('--role', '-r', default='analyst',
              help='Role for personalized summary')
@click.option('--level', '-l', default='third-grader',
              help='Reading level for simplified summary')
@click.option('--output', '-o', default=None, type=click.Path(),
              help='Output file path (optional)')
@click.option('--config', '-c', default='config.json', type=click.Path(exists=True),
              help='Configuration file path')
def summarize(input, type, sections, role, level, output, config):
    """Generate a summary of the input document"""
    
    # Load configuration
    with open(config, 'r') as f:
        cfg = json.load(f)
    
    # Initialize summarizer
    summarizer = DocumentSummarizer(
        region=cfg.get('region', 'us-east-1'),
        model_id=cfg.get('model_id')
    )
    
    # Read input document
    with open(input, 'r', encoding='utf-8') as f:
        document = f.read()
    
    # Generate summary based on type
    click.echo(f"Generating {type} summary...")
    
    if type == 'basic':
        summary = summarizer.basic_summary(document)
    elif type == 'one-sentence':
        summary = summarizer.one_sentence_summary(document)
    elif type == 'short':
        summary = summarizer.short_summary(document)
    elif type == 'structured':
        if not sections:
            sections = "Pain Points,Positive Results,Growth Opportunities"
        section_list = [s.strip() for s in sections.split(',')]
        summary = summarizer.structured_summary(document, section_list)
    elif type == 'personalized':
        summary = summarizer.personalized_summary(document, role)
    elif type == 'simplified':
        summary = summarizer.simplified_summary(document, level)
    
    # Output results
    click.echo("\n" + "="*80)
    click.echo("SUMMARY")
    click.echo("="*80 + "\n")
    click.echo(summary)
    
    # Save to file if specified
    if output:
        with open(output, 'w', encoding='utf-8') as f:
            f.write(summary)
        click.echo(f"\n✓ Summary saved to {output}")


@cli.command()
@click.option('--input-dir', '-i', required=True, type=click.Path(exists=True),
              help='Directory containing documents to summarize')
@click.option('--output-dir', '-o', required=True, type=click.Path(),
              help='Output directory for summaries')
@click.option('--type', '-t', default='short',
              type=click.Choice(['basic', 'one-sentence', 'short']),
              help='Type of summary to generate')
def batch(input_dir, output_dir, type):
    """Process multiple documents in batch"""
    
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    
    summarizer = DocumentSummarizer()
    
    # Process all text files
    text_files = list(input_path.glob('*.txt'))
    
    with click.progressbar(text_files, label='Processing documents') as files:
        for file_path in files:
            with open(file_path, 'r', encoding='utf-8') as f:
                document = f.read()
            
            # Generate summary
            if type == 'basic':
                summary = summarizer.basic_summary(document)
            elif type == 'one-sentence':
                summary = summarizer.one_sentence_summary(document)
            else:
                summary = summarizer.short_summary(document)
            
            # Save summary
            output_file = output_path / f"{file_path.stem}_summary.txt"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(summary)
    
    click.echo(f"\n✓ Processed {len(text_files)} documents")


if __name__ == '__main__':
    cli()
