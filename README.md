# Azure AI Document Processing Lab (Azure Functions + Document Intelligence)

This lab demonstrates how to build a production-style, event-driven document processing pipeline in Azure using:

- Azure Functions (Python)
- Azure Blob Storage
- Azure Document Intelligence (AI Service)
- Environment variables & secure configuration
- Blob Trigger architecture

## 🏗️ Architecture

When a document is uploaded to a storage container:

1. Azure Blob Trigger fires automatically
2. Azure Function sends the document to Azure Document Intelligence
3. Text is extracted from the document
4. The extracted text is written to a separate container as a `.txt` file

This simulates a real-world document ingestion and processing pipeline used in enterprise systems.

## 📦 Azure Services Used

- Azure Storage Account (Blob containers)
- Azure Function App (Python runtime)
- Azure Document Intelligence resource

## ⚙️ How It Works

### Blob Trigger
The function is triggered automatically when a file is uploaded to:



### Document Intelligence
The function sends the document to the prebuilt `prebuilt-read` model to extract all readable text.

### Output
The extracted text is saved to:



## 🔐 Configuration (Environment Variables)

Sensitive values are stored in `local.settings.json` and are not committed to GitHub.

Required settings:

- `AzureWebJobsStorage`
- `DOCINT_ENDPOINT`
- `DOCINT_KEY`

## 🧪 Testing the Lab

1. Start the function locally:


2. Upload any PDF to the `input-docs` container.
3. Watch the function run.
4. See the extracted `.txt` file appear in `processed-results`.

## 📸 Screenshots

Screenshots of the running function, storage containers, and output files are included in the `screenshots` folder.

## 💡 What This Demonstrates

This lab shows understanding of:

- Event-driven architecture in Azure
- Azure Functions blob triggers
- Integration of AI services into serverless workflows
- Secure configuration using environment variables
- Practical document processing automation

- Initial Azure AI document processing lab using Functions and Document Intelligence

