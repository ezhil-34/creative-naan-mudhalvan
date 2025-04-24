**Feature      **              |       ** Text used**

    Multimodal Interaction	   |      speech_recognition + pyttsx3,

    Adaptive Questioning       |      langchain.LLMChain + OpenAI,

    Performance Analytics      |      Custom metric tracking,

    Multilingual Support       |      Helsinki-NLP/opus-mt-multi,

    Personality Modes          |      Voice parameter tuning,




**Use Cases:**

  
    Job Seekers: Practice behavioral interviews (STAR method coaching)

    Students: Improve spoken English/Spanish for visa interviews

    Managers: Train for promotion panels with adaptive questioning

    Public Speakers: Reduce filler words ("um", "uh") with live feedback







**Output:**



     ![image](https://github.com/user-attachments/assets/a144b7e1-7884-461d-a234-b815a00072fa)










**Core Features:**

**🎙️ Speech Recognition & Synthesis**

        *Uses speech_recognition for listening & pyttsx3 for natural speech output

        Auto-detects language with langdetect and translates when needed

**🧠 Context-Aware Conversations**

        Maintains conversation history (last 5 exchanges) using deque

        Adapts questions based on dialogue context and personality profile

**📊 Real-Time Analytics**

**Tracks 3 key metrics:**

        Confidence (response length-based)

        Engagement (question frequency)

        Clarity (placeholder)

       Provides instant feedback after each response

**🤖 Dynamic Personality Modes**

**Switch between:**

        professional (slower speech, formal questions)

        friendly (faster pace, casual tone)

        Auto-configures voice parameters (rate, tone)

**🌍 Multilingual Support**

        Uses Helsinki-NLP translation model

        Currently supports English (en) & Spanish (es)

**Dynamic Questions
**

       Based on your previous answer it will automatically generate next question











