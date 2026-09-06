import streamlit as st
from src.generator import get_rag_chain
from src.evaluate import run_ragas_evaluation

st.set_page_config(page_title="GenAI RAG & Evaluator", layout="wide")

st.title("🤖 GenAI RAG Pipeline with Automated RAGAS Evaluation")
st.write("Interact with your custom knowledge base and view real-time hallucination & relevance metrics.")

@st.cache_resource
def load_chain():
    try:
        return get_rag_chain()
    except Exception as e:
        return None, None

chain, retriever = load_chain()

query = st.text_input("Ask a question about your ingested documents:")

if query:
    if not chain:
        st.error("Vector database not found or OpenAI Key missing. Run `python src/ingest.py` first.")
    else:
        with st.spinner("Generating answer and fetching context..."):
            # Retrieve context docs manually for evaluation display
            retrieved_docs = retriever.invoke(query)
            retrieved_contexts = [doc.page_content for doc in retrieved_docs]
            
            # Generate response
            response = chain.invoke(query)

        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("💡 Generated Answer")
            st.write(response)
            
            st.subheader("📚 Retrieved Context Chunks")
            for i, doc in enumerate(retrieved_docs):
                with st.expander(f"Chunk {i+1}"):
                    st.write(doc.page_content)

        with col2:
            st.subheader("📊 RAGAS Evaluation Metrics")
            if st.button("Run Evaluation Metrics"):
                with st.spinner("Calculating Faithfulness & Relevance..."):
                    eval_results = run_ragas_evaluation(query, response, retrieved_contexts)
                    st.metric(label="Faithfulness", value=f"{eval_results['faithfulness']:.2f}")
                    st.metric(label="Answer Relevancy", value=f"{eval_results['answer_relevancy']:.2f}")
                    st.metric(label="Context Precision", value=f"{eval_results['context_precision']:.2f}")