from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="bedrock-summarization",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="AI-powered document summarization using Amazon Bedrock and Claude 3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/bedrock-summarization",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "boto3>=1.34.0",
        "python-dotenv>=1.0.0",
        "click>=8.1.0",
    ],
    entry_points={
        "console_scripts": [
            "bedrock-summarize=cli:cli",
        ],
    },
)
