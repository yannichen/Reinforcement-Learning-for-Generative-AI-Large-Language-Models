from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from langchain.llms import HuggingFacePipeline
from peft import PeftModel




# Original Llama
access_token = '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'
model_id = 'meta-llama/Llama-2-7b-chat-hf'

tokenizer = AutoTokenizer.from_pretrained(model_id, token = access_token)
model_llama = AutoModelForCausalLM.from_pretrained(
    model_id,
    token = access_token
)

pipe_llama = pipeline(
    "text-generation",
    model = model_llama,
    tokenizer = tokenizer,
    max_new_tokens = 128
)

llm_llama = HuggingFacePipeline(pipeline = pipe_llama)



# Tuned Llama
model_tuned = PeftModel.from_pretrained(model_llama, 'adapters/Llama')

pipe_tuned = pipeline(
    "text-generation",
    model = model_tuned,
    tokenizer = tokenizer,
    max_new_tokens = 128
)

llm_tuned = HuggingFacePipeline(pipeline = pipe_tuned)



# Prompt Optimizer
BPO_model_path = "THUDM/BPO"
BPO_tokenizer = AutoTokenizer.from_pretrained(BPO_model_path)
BPO_model = AutoModelForCausalLM.from_pretrained(BPO_model_path)

model_BPO_tuned = PeftModel.from_pretrained(BPO_model,'adapters/BPO')

pipe_BPO_tuned = pipeline(
    "text-generation",
    model = model_BPO_tuned,
    tokenizer = BPO_tokenizer,
    max_new_tokens = 128
)

BPO_tuned = HuggingFacePipeline(pipeline = pipe_BPO_tuned)


# Model dictionary
models = {
    'Llama2'            : llm_llama,
    'Llama2 - Tuned'    : llm_tuned,
    'Prompt Optimizer'  : BPO_tuned
}

print(list(models.keys()))