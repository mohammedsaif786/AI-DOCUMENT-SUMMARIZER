import streamlit as st
from summarizer import summarize_text

st.set_page_config(
    page_title="AI Document Summarizer",
    page_icon="📄",
    layout="wide"
)

# --------- CUSTOM STYLE ---------

st.markdown("""
<style>

.main {
    background-color:#0E1117;
}

h1{
color:#00FFFF;
text-align:center;
}

.summary-box{
background:#1E1E1E;
padding:20px;
border-radius:10px;
}

</style>
""", unsafe_allow_html=True)

# --------- TITLE ---------

st.title("📄 AI Document Summarizer")

st.write(
"Summarize long documents using Artificial Intelligence."
)

# --------- SIDEBAR ---------

st.sidebar.title("⚙️ Settings")

max_len = st.sidebar.slider(
    "Maximum Summary Length",
    50, 300, 120
)

min_len = st.sidebar.slider(
    "Minimum Summary Length",
    10, 100, 30
)

st.sidebar.write("---")

st.sidebar.info(
"This app summarizes long documents using AI."
)

# --------- INPUT SECTION ---------

st.subheader("📝 Enter Your Document")

text = st.text_area(
    "Paste text here",
    height=300,
    placeholder="Paste a long article or document..."
)

# --------- TEXT STATISTICS ---------

if text:

    words = len(text.split())
    chars = len(text)

    col1, col2 = st.columns(2)

    col1.metric("Word Count", words)
    col2.metric("Character Count", chars)

# --------- SUMMARIZE BUTTON ---------

if st.button("🚀 Generate Summary"):

    if text.strip() == "":
        st.warning("Please enter some text first!")

    else:

        with st.spinner("AI is generating summary..."):

            summary = summarize_text(text, max_len, min_len)

        st.success("Summary Generated!")

        st.subheader("📌 Summary")

        st.markdown(
        f'<div class="summary-box">{summary}</div>',
        unsafe_allow_html=True
        )

        # download option
        st.download_button(
            "⬇ Download Summary",
            summary,
            file_name="summary.txt"
        )

# --------- EXTRA SECTION ---------

with st.expander("ℹ️ How this works"):

    st.write(
    """
    This system uses a transformer-based AI model to
    analyze long text and generate a shorter summary.

    The model understands context and extracts
    important information automatically.
    """
    )