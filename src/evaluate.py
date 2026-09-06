from datasets import Dataset
from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy, context_precision

def run_ragas_evaluation(query, response, retrieved_contexts, ground_truth=""):
    data = {
        "question": [query],
        "answer": [response],
        "contexts": [retrieved_contexts],
        "ground_truth": [ground_truth if ground_truth else response]
    }
    dataset = Dataset.from_dict(data)
    
    result = evaluate(
        dataset=dataset,
        metrics=[faithfulness, answer_relevancy, context_precision]
    )
    return result