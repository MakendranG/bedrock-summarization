"""
Unit tests for DocumentSummarizer
"""

import unittest
from unittest.mock import Mock, patch, MagicMock
import json
from summarizer import DocumentSummarizer


class TestDocumentSummarizer(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures"""
        self.sample_document = """
        Amazon Web Services continues to grow with strong Q3 results.
        AWS revenue increased by 12% year-over-year reaching $23.1 billion.
        The company launched new AI services and expanded infrastructure.
        """
        
    @patch('boto3.client')
    def test_initialization(self, mock_boto_client):
        """Test summarizer initialization"""
        summarizer = DocumentSummarizer(region='us-east-1')
        self.assertIsNotNone(summarizer.bedrock)
        self.assertEqual(summarizer.model_id, 'anthropic.claude-3-sonnet-20240229-v1:0')
        
    @patch('boto3.client')
    def test_basic_summary(self, mock_boto_client):
        """Test basic summary generation"""
        # Mock the Bedrock response
        mock_response = {
            'body': MagicMock()
        }
        mock_response['body'].read.return_value = json.dumps({
            'content': [{'text': 'AWS showed strong growth in Q3.'}]
        }).encode()
        
        mock_client = Mock()
        mock_client.invoke_model.return_value = mock_response
        mock_boto_client.return_value = mock_client
        
        summarizer = DocumentSummarizer()
        result = summarizer.basic_summary(self.sample_document)
        
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        
    @patch('boto3.client')
    def test_one_sentence_summary(self, mock_boto_client):
        """Test one-sentence summary"""
        mock_response = {
            'body': MagicMock()
        }
        mock_response['body'].read.return_value = json.dumps({
            'content': [{'text': 'AWS revenue grew 12% to $23.1B in Q3.'}]
        }).encode()
        
        mock_client = Mock()
        mock_client.invoke_model.return_value = mock_response
        mock_boto_client.return_value = mock_client
        
        summarizer = DocumentSummarizer()
        result = summarizer.one_sentence_summary(self.sample_document)
        
        self.assertIsInstance(result, str)
        # Check if it's reasonably short
        self.assertTrue(len(result.split('.')) <= 2)
        
    @patch('boto3.client')
    def test_structured_summary(self, mock_boto_client):
        """Test structured summary with sections"""
        mock_response = {
            'body': MagicMock()
        }
        mock_response['body'].read.return_value = json.dumps({
            'content': [{'text': 'Growth: 12% increase\nChallenges: Competition'}]
        }).encode()
        
        mock_client = Mock()
        mock_client.invoke_model.return_value = mock_response
        mock_boto_client.return_value = mock_client
        
        summarizer = DocumentSummarizer()
        sections = ["Growth", "Challenges"]
        result = summarizer.structured_summary(self.sample_document, sections)
        
        self.assertIsInstance(result, str)
        
    @patch('boto3.client')
    def test_personalized_summary(self, mock_boto_client):
        """Test role-based personalized summary"""
        mock_response = {
            'body': MagicMock()
        }
        mock_response['body'].read.return_value = json.dumps({
            'content': [{'text': 'Strong revenue growth indicates solid investment opportunity.'}]
        }).encode()
        
        mock_client = Mock()
        mock_client.invoke_model.return_value = mock_response
        mock_boto_client.return_value = mock_client
        
        summarizer = DocumentSummarizer()
        result = summarizer.personalized_summary(
            self.sample_document,
            role="financial analyst",
            focus="profitability"
        )
        
        self.assertIsInstance(result, str)
        
    @patch('boto3.client')
    def test_error_handling(self, mock_boto_client):
        """Test error handling for API failures"""
        mock_client = Mock()
        mock_client.invoke_model.side_effect = Exception("API Error")
        mock_boto_client.return_value = mock_client
        
        summarizer = DocumentSummarizer()
        
        with self.assertRaises(Exception) as context:
            summarizer.basic_summary(self.sample_document)
        
        self.assertIn("Error invoking Bedrock model", str(context.exception))


if __name__ == '__main__':
    unittest.main()
