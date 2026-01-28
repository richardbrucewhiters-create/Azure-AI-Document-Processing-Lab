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

