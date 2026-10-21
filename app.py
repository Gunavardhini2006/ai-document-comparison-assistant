import streamlit as st
from document_reader import extract_text_from_pdf
from comparison import compare_documents
from report_generator import generate_docx_report

# Configure the Streamlit page layout
st.set_page_config(
    page_title="AI Document Comparison Assistant",
    page_icon="📄",
    layout="wide"
)

# Application Header & Instructions
st.title("📄 AI Document Comparison Assistant")
st.markdown("""
Welcome! Upload two PDF documents (such as policies, syllabi, contracts, or project specs) 
to automatically extract, analyze, and compare their text contents using Gemini[cite: 1, 2].
""")

# Sidebar for file uploaders
st.sidebar.header("Upload Documents")
uploaded_file_a = st.sidebar.file_uploader("Upload Document A (PDF)", type=["pdf"])
uploaded_file_b = st.sidebar.file_uploader("Upload Document B (PDF)", type=["pdf"])

compare_button = st.sidebar.button("Compare Documents", type="primary")

# Main logic when button is clicked
if compare_button:
    if not uploaded_file_a or not uploaded_file_b:
        st.error("⚠️ Please upload both Document A and Document B before clicking compare.")
    else:
        with st.spinner("🔄 Extracting text and analyzing documents with Gemini... Please wait."):
            
            # 1. Extract text from Document A
            text_a, err_a = extract_text_from_pdf(uploaded_file_a)
            if err_a:
                st.error(f"Document A Error: {err_a}")
                st.stop()
            
            # 2. Extract text from Document B
            text_b, err_b = extract_text_from_pdf(uploaded_file_b)
            if err_b:
                st.error(f"Document B Error: {err_b}")
                st.stop()
            
            # 3. Send texts to Gemini for comparison
            comparison_result, err_llm = compare_documents(text_a, text_b)
            if err_llm:
                st.error(f"Comparison Error: {err_llm}")
                st.stop()
            
            # Save results in Streamlit session state so they persist on the screen
            st.session_state["comparison_result"] = comparison_result
            st.session_state["doc_a_name"] = uploaded_file_a.name
            st.session_state["doc_b_name"] = uploaded_file_b.name

# Display results if they exist in session state
if "comparison_result" in st.session_state:
    st.success("✅ Comparison completed successfully!")
    
    # Create tabs for structured viewing as required by the brief
    tab1, tab2 = st.tabs(["📊 Comparison Results", "ℹ️ About Files"])
    
    with tab1:
        st.subheader("Analysis & Findings")
        st.markdown(st.session_state["comparison_result"])
        
    with tab2:
        st.write(f"**Document A Filename:** {st.session_state['doc_a_name']}")
        st.write(f"**Document B Filename:** {st.session_state['doc_b_name']}")

    # Download Report Section
    st.divider()
    st.subheader("📥 Download Report")
    
    docx_buffer = generate_docx_report(
        st.session_state["doc_a_name"],
        st.session_state["doc_b_name"],
        st.session_state["comparison_result"]
    )
    
    st.download_button(
        label="Download Comparison Report (.docx)",
        data=docx_buffer,
        file_name="AI_Document_Comparison_Report.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )