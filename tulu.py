import streamlit as st
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import make_pipeline

# Streamlit app configuration
st.set_page_config(page_title="Tulu Translator", page_icon="🌐")

# Function to preprocess text files (remove extra spaces, convert to lowercase)
def preprocess_text_file(file_path):
    cleaned_lines = []
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip().lower()  # Convert to lowercase and remove extra spaces
            if line:  # Only add non-empty lines
                cleaned_lines.append(line)
    
    return cleaned_lines

# Function to load translations from files and clean the data
def load_translation_data(english_file, tulu_file):
    try:
        # Preprocess the files
        english_phrases = preprocess_text_file(english_file)
        tulu_phrases = preprocess_text_file(tulu_file)
        
        # Ensure the number of lines match
        if len(english_phrases) != len(tulu_phrases):
            st.error("Mismatch between the number of English and Tulu phrases.")
            return None, None
        
        return english_phrases, tulu_phrases
    
    except FileNotFoundError as e:
        st.error(f"File not found: {e}")
        return None, None
    except Exception as e:
        st.error(f"Error: {e}")
        return None, None

# Define file paths (ensure these files are in the same directory)
english_file = "en_tr.txt"
tulu_file = "tulu_tr.txt"

# Load translation data
english_phrases, tulu_phrases = load_translation_data(english_file, tulu_file)

# If data loading fails, exit
if english_phrases is None or tulu_phrases is None:
    st.stop()

# Create a KNN model pipeline (TF-IDF + KNN)
vectorizer = TfidfVectorizer()  # Convert text to feature vectors
knn_model = KNeighborsClassifier(n_neighbors=1)  # Use 1 nearest neighbor

# Train the KNN model
X = english_phrases
y = tulu_phrases
knn_model.fit(vectorizer.fit_transform(X), y)

# App interface
st.title("Tulu Translator")
st.write("Translate English phrases to Tulu using K-Nearest Neighbors!")

# Manage input and translation result using session_state
if "input_text" not in st.session_state:
    st.session_state.input_text = ""

# Input from the user
english_input = st.text_input("Enter an English phrase:", value=st.session_state.input_text).strip().lower()

# Save the input text to session_state so it can be reused
st.session_state.input_text = english_input

# Translation output
translation_result = st.empty()  # Placeholder for translation result

# Trigger translation only when the "Translate" button is clicked
if st.button("Translate"):
    if english_input:
        # Predict the Tulu translation for the input English phrase
        predicted_translation = knn_model.predict(vectorizer.transform([english_input]))[0]
        translation_result.write(f"**Tulu Translation:** {predicted_translation}")
    else:
        translation_result.write("Enter an English phrase to see its Tulu translation.")

# Clear button functionality
if st.button("Clear"):
    st.session_state.input_text = ""  # Clears the input field
    translation_result.empty()  # Clears the translation result
