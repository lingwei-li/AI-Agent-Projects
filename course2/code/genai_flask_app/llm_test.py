from model import llama3_response, granite_response, mixtral_response

def call_all_models(system_prompt, user_prompt):
    llama_result = llama3_response(system_prompt, user_prompt)
    granite_result = granite_response(system_prompt, user_prompt)
    mixtral_result = mixtral_response(system_prompt, user_prompt)

    print("Llama3 Response:\n",  llama_result.get('response',  str(llama_result)))
    print("\nGranite Response:\n", granite_result.get('response', str(granite_result)))
    print("\nMixtral Response:\n", mixtral_result.get('response', str(mixtral_result)))


# Example call to test all models
call_all_models("You are a helpful assistant who provides concise and accurate answers", "What is the capital of Canada? Tell me a cool fact about it as well")