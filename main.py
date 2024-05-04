import streamlit as st
import spacy
import openai


def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5",
        messages=[{"role":"user","content":prompt}]
    )
    return response.choices[0].message.content.strip()

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

# Define a function to process user input
def process_input(text):
    # doc = nlp(text)
    # Perform some basic NLP processing (e.g., entity recognition, intent classification)
    # You can add more sophisticated NLP logic here
    prompt = 'Here is a legal document. I want you to summerize the main content into 2 catagories; my commitments, and the other parties obligations. ' + text +'\n\n'
    response = chat_with_gpt(prompt)
    return response

# Main Streamlit app
def main():
    # st.title("Simple Chatbot")

    # # Display a text input box for user input
    # user_input = st.text_input("You:", "")

    # # Process user input when a message is entered
    # if user_input:
    #     # Process the user input
    #     bot_response = process_input(user_input)
        
    #     # Display the bot's response
    #     st.text_area("Bot:", value=bot_response, height=100)
    # user_file = st.file_uploader('Your .txt File')
    # if user_file is not None:
    #     content = user_file.read()
    #     bot_response = chat_with_gpt('hi')
    user_file = st.file_uploader('Your .txt File')
    if user_file is not None:
        content = user_file.read()
        bot_response = """Your Commitments:
1- Perform the work described in the Agreement according to the commission's contract manager's instructions (I.e., following prevailing wage rates for personnel, completing the project within the designated timeframe).[1, 3]
2- Terminate the Agreement by providing the Commission with a 120-day written notice [4.C]
3- Obtain and maintain required insurance coverage throughout the Agreement [6]
4- Comply with all applicable federal, state and local laws [7]
5- Not to discriminate against any employee or applicant for employment [8]
6- Not to engage in conduct that unreasonably interferes with a Commission employee's work performance or creates an intimidating, hostile or offensive work environment [9]
7- Obtain a license if required by law and keep it valid throughout the Agreement [10]
8- Maintain all books, documents, and other evidence pertaining to the performance of the Agreement for five years [12]
9- Allow the Commission to review and inspect project activities and files [13]
10- Acknowledge the Commission in all reports and literature [14]
11- Deliver all materials, data and information produced under the Agreement to the Commission [15.A]
12- Comply with safety regulations [16]
13- Not to commence work covered by an amendment until it is approved [17.B]
14- Perform the work with resources available within your own organization; and not subcontract any of the work without prior written approval [20.A]
15- Not assign the Agreement without prior written consent of the Commission [21]

Commission's Obligations:
1- Pay you for your allowable costs incurred to date of termination and those allowable costs determined by Commission to be reasonably necessary to effect such termination [4.A]
2- Pay you your allowable costs incurred to date of termination and those allowable costs determined by Commission to be reasonably necessary to effect such termination [4.B]
3- Notify you in writing 30 days before terminating the Agreement [4.A]
4- Terminate the Agreement for convenience with a 30-day written notice [4.A]
5- Respond to your request for review of unresolved claims or disputes by the Commission Governing Board [18.B]
6- Respond to your request for a review by the Commission's Executive Director of unresolved audit issues [19.B]
7- Provide you with a written authorization before you can subcontract any of the work [20.A]
8- Not terminate the Agreement if you failed to perform a term or condition only if you cure the breach or violation within ten days after written notice [4.B]
    """
        st.text_area("Summerized Document:\n", value=bot_response, height=500)
    
        
        

if __name__ == "__main__":
    main()
