from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task="text-generation",
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_token=100
    )
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("what is the capital of india?")

print(result.content)


# After this file run the mention model will be downloaded on your local machine
# through this we will get the responce of our questions.
# by using this code we can download this type of models from hugging face plateform and run on local computer.