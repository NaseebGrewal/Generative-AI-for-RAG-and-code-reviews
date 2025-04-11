# # code to create an index with specific fields
# import os
# import uuid

# from azure.core.credentials import AzureKeyCredential
# from azure.search.documents import SearchClient

# # from azure.search.documents.models import Vector
# from azure.search.documents.indexes import SearchIndexClient
# from azure.search.documents.indexes.models import (
#     SearchableField,
#     SearchFieldDataType,
#     SearchIndex,
#     SemanticConfiguration,
#     SemanticField,
#     SemanticPrioritizedFields,
#     SemanticSearch,
#     SimpleField,
# )
# from dotenv import load_dotenv

# load_dotenv()  # This loads the variables from .env into the environment


# def generate_random_id():
#     random_id = str(uuid.uuid4()).replace("-", "")
#     return random_id


# def create_index(index_name):
#     # Set the service endpoint and API key from the environment

#     service_name = os.environ["service_name"]
#     admin_key = os.environ["admin_key"]

#     index_name = index_name

#     # Create an SDK client
#     endpoint = "https://{}.search.windows.net/".format(service_name)
#     admin_client = SearchIndexClient(
#         endpoint=endpoint,
#         index_name=index_name,
#         credential=AzureKeyCredential(admin_key),
#     )

#     # Deleting Index : Check if the index exists before deleting
#     index_client = admin_client
#     try:
#         # List all indexes
#         index_names = [index.name for index in index_client.list_indexes()]

#         # Check if the index name is in the list of index names
#         if index_name in index_names:
#             index_client.delete_index(index_name)
#             print(f"Index '{index_name}' has been deleted.")
#         else:
#             print(f"Index '{index_name}' does not exist and cannot be deleted.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

#     # Specify the index schema
#     fields = [
#         SimpleField(
#             name="DocId", type=SearchFieldDataType.String, key=True, sortable=True
#         ),
#         SearchableField(
#             name="filename", type=SearchFieldDataType.String, sortable=True
#         ),
#         SearchableField(
#             name="content", type=SearchFieldDataType.String, analyzer_name="en.lucene"
#         ),
#         SearchableField(
#             name="extension",
#             type=SearchFieldDataType.String,
#             facetable=True,
#             filterable=True,
#             sortable=True,
#         ),
#         SimpleField(
#             name="page_para_slide",
#             type=SearchFieldDataType.Int64,
#             filterable=False,
#         ),
#     ]

#     semantic_config = SemanticConfiguration(
#         name="my-semantic-config",
#         prioritized_fields=SemanticPrioritizedFields(
#             title_field=SemanticField(field_name="filename"),
#             keywords_fields=[SemanticField(field_name="extension")],
#             content_fields=[SemanticField(field_name="content")],
#         ),
#     )

#     # Create the semantic settings with the configuration
#     semantic_search = SemanticSearch(configurations=[semantic_config])

#     index = SearchIndex(name=index_name, fields=fields, semantic_search=semantic_search)
#     try:
#         result = admin_client.create_index(index)
#         print("Index", result.name, "created")
#         print(result)
#     except Exception as ex:
#         print(ex)

#     res = index_client.list_indexes()
#     ls = [i.name for i in res]
#     print(ls, index_name)
#     if index_name in ls:
#         return True
#     else:
#         return False


# def upload_to_index(index_name, chunks, file_name, extension):
#     # Extract the content from the PDF
#     service_name = os.environ["service_name"]
#     admin_key = os.environ["admin_key"]

#     index_name = index_name
#     endpoint = "https://{}.search.windows.net/".format(service_name)
#     # chunks = extract_text_from_pdf(file_path)

#     search_client = SearchClient(
#         endpoint=endpoint,
#         index_name=index_name,
#         credential=AzureKeyCredential(admin_key),
#     )
#     # Split content into chunks if necessary
#     # chunks = split_into_chunks(content)

#     # rand_id =
#     # Create a list of documents to index
#     documents = [
#         {
#             "DocId": generate_random_id(),
#             "filename": file_name,
#             "extension": extension,
#             "content": chunk,
#             "page_para_slide": i + 1,
#         }
#         for i, chunk in enumerate(chunks)
#     ]

#     # Index the documents
#     result = search_client.upload_documents(documents=documents)
#     return result


# def delete_index(index_name):
#     # this code deletes an existing index from azure cognitive search

#     # Replace with your Azure Cognitive Search service name and admin key
#     # service_name = os.environ["AZURE_COGNITIVE_SEARCH_SERVICE_NAME_LAB"]
#     # admin_key = os.environ["AZURE_COGNITIVE_SEARCH_API_KEY_LAB"]

#     service_name = os.environ["service_name"]
#     admin_key = os.environ["admin_key"]

#     # Create an instance of the SearchIndexClient
#     credential = AzureKeyCredential(admin_key)
#     endpoint = f"https://{service_name}.search.windows.net/"
#     index_client = SearchIndexClient(endpoint, credential)

#     # Name of the index to delete
#     index_name = index_name

#     # Check if the index exists before deleting
#     try:
#         # List all indexes
#         index_names = [index.name for index in index_client.list_indexes()]

#         # Check if the index name is in the list of index names
#         if index_name in index_names:
#             index_client.delete_index(index_name)
#             print(f"Index '{index_name}' has been deleted.")
#             return True
#         else:
#             print(f"Index '{index_name}' does not exist and cannot be deleted.")
#             return True
#     except Exception as e:
#         print(f"An error occurred: {e}")  #
#         return False

#     return True


# def semantic_search(query: str, index_name) -> str:
#     """
#     Retrieve a response from the Cognitive Search Semantic Search based on user query.

#     Args:
#         query (str): The user's input query.

#     Returns:
#         str: The response from the semantic search.
#     """
#     service_name = os.environ["service_name"]
#     admin_key = os.environ["admin_key"]
#     # service_name = os.environ["AZURE_COGNITIVE_SEARCH_SERVICE_NAME"]
#     # admin_key = os.environ["AZURE_COGNITIVE_SEARCH_API_KEY"]
#     index_name = index_name

#     endpoint = f"https://{service_name}.search.windows.net/"

#     search_client = SearchClient(
#         endpoint=endpoint,
#         index_name=index_name,
#         credential=AzureKeyCredential(admin_key),
#     )

#     results = search_client.search(
#         query_type="semantic",
#         semantic_configuration_name="my-semantic-config",
#         search_text=query,
#         select=["content", "filename", "page_para_slide", "extension"],
#         query_caption="extractive",
#     )

#     data_list = []

#     for result in results:
#         temp_dict = {
#             "content": result["content"],
#             "filename": result["filename"],
#             "page_para_slide": result["page_para_slide"],
#             "extension": result["extension"],
#         }
#         data_list.append(temp_dict)
#     return data_list
