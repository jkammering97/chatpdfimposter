# ChatPdfAPIUser

## Overview
`ChatPDF` is a Python class for uploading PDFs to an API and managing the `source_id` for subsequent API interactions.

## Setup

### Prerequisites
- Python 3.6+
- `requests` library

### Installation
Install the required package using pip:
   ```bash
   pip install -r requirements.txt
   ```
## Quick Start

**Initialize the uploader**:
   Replace placeholders with your values.

* set your api key in a .env file
``` python
api_key = os.getenv('chatpdfkey')
pdf_path = 'path'
pdf = ChatPDF(api_key)
pdf.add_file(pdf_path)
pdf.ask_question(question)
```

