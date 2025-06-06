import speech_recognition as sr
from transformers import pipeline
import pyttsx3
from langdetect import detect
import time
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from collections import deque

class DynamicAICoach:
    def __init__(self, language="en", personality="professional"):
        # Core components
        self.recognizer = sr.Recognizer()
        self.language = language
        self.personality = personality
        self.tts = pyttsx3.init()
        
        # Adaptive conversation memory (last 5 exchanges)
        self.conversation = deque(maxlen=5)
        
        # Dynamic analysis models
        self.translator = pipeline("translation", 
                                 model="Helsinki-NLP/opus-mt-multi")
        self.llm = OpenAI(temperature=0.7, max_tokens=200)
        
        # Performance metrics
        self.metrics = {
            "confidence": [],
            "engagement": [],
            "clarity": []
        }
        
        # Configure voice personality
        self._configure_voice()

    def _configure_voice(self):
        voices = self.tts.getProperty('voices')
        if self.language == 'es':
            self.tts.setProperty('voice', voices[1].id)
        if self.personality == "friendly":
            self.tts.setProperty('rate', 180)
        else: # professional
            self.tts.setProperty('rate', 150)

    def dynamic_speak(self, text):
        """Adaptive speech with conversational pacing"""
        print(f"\nAI [{self.personality}]: {text}")
        
        # Dynamic pacing based on sentence complexity
        pause = min(1.0, max(0.3, len(text.split())*0.1))
        chunks = [text[i:i+100] for i in range(0, len(text), 100)]
        
        for chunk in chunks:
            self.tts.say(chunk)
            self.tts.runAndWait()
            time.sleep(pause)

    def dynamic_listen(self):
        """Adaptive listening with noise handling"""
        with sr.Microphone() as source:
            print("\n[Listening...]")
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            
            try:
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=15)
                text = self.recognizer.recognize_google(audio)
                print(f"You: {text}")
                
                # Dynamic translation
                if detect(text) != self.language:
                    translated = self.translator(text, tgt_lang=self.language)[0]['translation_text']
                    print(f"(Translated: {translated})")
                    return translated
                return text
                
            except sr.WaitTimeoutError:
                self.dynamic_speak("I didn't hear your response. Shall we continue?")
                return None
            except Exception as e:
                print(f"Error: {str(e)}")
                return None

    def analyze_interaction(self, text):
        """Real-time multimodal analysis"""
        # Dynamic confidence scoring (0-1)
        confidence = min(1.0, max(0.1, len(text.split())/50)) # Simplified
        
        # Engagement detection (questions/statements ratio)
        engagement = 0.5 + (text.count('?')*0.1)
        
        # Update running metrics
        self.metrics["confidence"].append(confidence)
        self.metrics["engagement"].append(engagement)
        self.metrics["clarity"].append(0.7) # Placeholder
        
        return {
            "confidence": f"{confidence*100:.1f}%",
            "engagement": "High" if engagement > 0.7 else "Medium",
            "key_terms": text.split()[:3] # First 3 words as sample
        }

    def generate_dynamic_response(self, user_input):
        """Context-aware response generation"""
        # Update conversation history
        self.conversation.append(f"User: {user_input}")
        
        template = """Conversation Context (last 3 exchanges):
        {context}
        
        As a {personality} interviewer, considering:
        - Key metrics: {metrics}
        - Current language: {language}
        
        Generate:
        1. Brief analysis of last response
        2. Personalized feedback
        3. Natural follow-up question
        
        Structure your response with:
        [Analysis]...
        [Feedback]...
        [Question]..."""
        
        prompt = PromptTemplate(
            template=template,
            input_variables=["context", "personality", "metrics", "language"]
        )
        
        chain = LLMChain(llm=self.llm, prompt=prompt)
        return chain.run(
            context="\n".join(list(self.conversation)[-3:]),
            personality=self.personality,
            metrics=str(self.metrics),
            language=self.language
        )

    def conduct_session(self):
        """Fully dynamic interview flow"""
        self.dynamic_speak(f"Starting {self.personality} interview practice in {self.language}.")
        
        # Dynamic first question based on personality
        first_question = {
            "professional": "Walk me through your most challenging project.",
            "friendly": "Tell me about a work experience you're proud of!"
        }.get(self.personality)
        
        while True:
            # Generate and ask dynamic question
            if len(self.conversation) == 0:
                question = first_question
            else:
                response = self.generate_dynamic_response(user_input)
                question = response.split("[Question]")[-1].strip()
            
            self.dynamic_speak(question)
            self.conversation.append(f"AI: {question}")
            
            # Get user response
            user_input = self.dynamic_listen()
            if not user_input:
                continue
            if "stop" in user_input.lower():
                break
                
            # Real-time analysis
            analysis = self.analyze_interaction(user_input)
            print(f"\n[Real-time Analysis] {analysis}")
            
            # Generate and deliver dynamic feedback
            response = self.generate_dynamic_response(user_input)
            for part in ["Analysis", "Feedback", "Question"]:
                if f"[{part}]" in response:
                    self.dynamic_speak(response.split(f"[{part}]")[1].split("[")[0].strip())
            
        # Session summary
        avg_conf = sum(float(m[:-1]) for m in self.metrics["confidence"])/len(self.metrics["confidence"])
        self.dynamic_speak(f"Session complete! Your average confidence was {avg_conf:.1f}%")

if __name__ == "__main__":
    # Try: personality="friendly" or language="es"
    coach = DynamicAICoach(language="en", personality="professional")
    coach.conduct_session()