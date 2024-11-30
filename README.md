**Language Translator**
**ENGLISH TO TULU LANGUAGE TRANSLATOR **
Tulu is a regional language spoken in parts of Karnataka and Kerala, India. However, it is often underrepresented in language technology platforms. 
This project aims to develop a translator that supports Tulu alongside major languages like English, Kannada, and Hindi, facilitating communication and preservation of the language. By using NLP model techniques, the translator efficiently processes text and provides accurate translations.

1.	**Dataset Preparation:**
•	Extracted and cleaned textual data from en_tr.txt and tulu_tr.txt to create paired English-Tulu translations.
•	Ensured proper alignment between English and Tulu phrases to avoid mismatches.
2.	**Model Implementation:**
•	Built a machine learning pipeline combining TfidfVectorizer for text feature extraction and a KNN classifier for translation.
•	Trained the KNN model using the aligned dataset to map English phrases to their Tulu equivalents.
3.	**Application Development:**
•	Designed and implemented a web-based Tulu Translator application using Streamlit.
o	The app included user inputs for English phrases and displayed corresponding Tulu translations using the trained model.
4.	**Testing and Debugging:**
•	Tested the application with various phrases to ensure accurate translations.
•	Addressed issues such as mismatched translations and improved preprocessing.

The Tulu Language Translation Project successfully demonstrates the practical application of machine learning in language processing.
By creating a bilingual translation model and implementing it in a user-friendly web application, the project enhances accessibility and communication between Tulu and English speakers.
Despite the challenges of dataset alignment and preprocessing, the project achieved meaningful results, paving the way for further developments such as expanding the dataset, supporting additional languages, and refining the model for context-based translations.
 This initiative highlights the potential of AI in preserving regional languages and fostering cross-linguistic communication.
