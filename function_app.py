import os
import logging
import azure.functions as func

from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.core.credentials import AzureKeyCredential
from azure.storage.blob import BlobServiceClient


app = func.FunctionApp()


@app.function_name(name="ProcessDocument")
@app.blob_trigger(
    arg_name="myblob",
    path="input-docs/{name}",
    connection="AzureWebJobsStorage"
)
def ProcessDocument(myblob: func.InputStream):
    logging.info(f"Processing blob: {myblob.name}")

    # --- Document Intelligence setup ---
    endpoint = os.environ["DOCINT_ENDPOINT"]
    key = os.environ["DOCINT_KEY"]

    client = DocumentIntelligenceClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(key)
    )

    # --- Send document to Azure AI ---
    poller = client.begin_analyze_document(
        model_id="prebuilt-read",
        body=myblob.read()
    )

    result = poller.result()

    extracted_text = ""
    for page in result.pages:
        for line in page.lines:
            extracted_text += line.content + "\n"

    # --- Save results back to storage ---
    logging.info("Saving extracted text to processed-results container")

    connection_string = os.environ["AzureWebJobsStorage"]
    blob_service = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service.get_container_client("processed-results")

    output_blob_name = myblob.name.replace("input-docs/", "").replace(".pdf", ".txt")

    container_client.upload_blob(
        name=output_blob_name,
        data=extracted_text,
        overwrite=True
    )

    logging.info(f"Saved result as: {output_blob_name}")

