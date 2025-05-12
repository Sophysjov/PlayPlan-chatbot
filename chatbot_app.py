import streamlit as st

# Chatbot-klasse
class Chatbot:
    def __init__(self):
        # Foruddefinerede svar baseret på nøgleord
        self.responses = {
            "hej": "Hej! Hvordan kan jeg hjælpe dig?",
            "hvordan": "Jeg er her for at hjælpe dig med sportsplanlægning. Hvad har du brug for?",
            "login": "For at logge ind, klik på login-knappen og indtast dine oplysninger.",
            "farvel": "Farvel! Hav en god dag!",
        }

    def get_response(self, user_input):
        # Gør input småt og tjek for nøgleord
        user_input = user_input.lower()
        for keyword, response in self.responses.items():
            if keyword in user_input:
                return response
        return "Beklager, jeg forstod ikke dit spørgsmål. Kan du prøve igen?"

# Initialiser chatbotten
chatbot = Chatbot()

# Streamlit UI
st.title("PlayPlan Chatbot")
st.write("Velkommen til PlayPlan Chatbot! Stil et spørgsmål, og få et svar.")

# Input fra brugeren
user_input = st.text_input("Skriv din besked her:")

# Hvis der er input, vis chatbot-svar
if user_input:
    response = chatbot.get_response(user_input)
    st.write(f"**Chatbot:** {response}")
    