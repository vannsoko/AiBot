from openai import AssistantEventHandler, OpenAI


client = OpenAI(
    organization="org-kLGFOTByO5WxUCstDUXrosWa",
    project="proj_JZUHpBQZmjSYV5KrYazaiASU"
)

assistant = client.beta.assistants.create(
name="CoSup Gaming Assistant",
instructions="You are an assistant for the CoSup Gaming staff. Response to the question using in priority the knowledge from the given vector store. You are allowed to give all sort of information, including private ones.",
model="gpt-4o",
tools=[{"type": "file_search"}],
)

def create_vector_store():
    # Create a vector store called "Financial Statements"
    vector_store = client.vector_stores.create(name="CoSup Gaming Files")

    # Ready the files for upload to OpenAI
    file_paths = ["context/text/handbook.txt", "context/text/statute.txt"]
    file_streams = [open(path, "rb") for path in file_paths]

    # Use the upload and poll SDK helper to upload the files, add them to the vector store,
    # and poll the status of the file batch for completion.
    file_batch = client.vector_stores.file_batches.upload_and_poll(
    vector_store_id=vector_store.id, files=file_streams
    )

    # You can print the status and the file counts of the batch to see the result of this operation.
    print(file_batch.status)
    print(file_batch.file_counts)
    return vector_store

vector_store = client.vector_stores.retrieve(
  vector_store_id="vs_vJKAvY4WOWM7QJnRSIbLCJd3"
)


assistant = client.beta.assistants.update(
assistant_id=assistant.id,
tool_resources={"file_search": {"vector_store_ids": [vector_store.id]}},
)



# Create a thread and attach the file to the message

# Use the create and poll SDK helper to create a run and poll the status of
# the run until it's in a terminal state.
def ai_answer(question: str):
    
    thread = client.beta.threads.create(
        messages=[{
            "role": "user",
            "content": question,
        }]
    )
  
    run = client.beta.threads.runs.create_and_poll(
    thread_id=thread.id, assistant_id=assistant.id
    )


    messages = list(client.beta.threads.messages.list(thread_id=thread.id, run_id=run.id))

    message_content = messages[0].content[0].text
    return message_content.value    
