# uv Environment Setup

## uv pakage installed with configration:

### 1. first command for Initialize project:
```python
uv init --package uv_project 
```

### 2. second command for create virtual environment:
```python
uv venv   # for create virtual environment.
```

#### 3. and then run for active project(virtual environment) :

``` 
.venv\Scripts\activate

or

ctrl + shift + p
```


### and then change script:
first_project.main:hello:
- uv_project  --> folder name
- main  --> file name
- hello --> function name


------

# LiteLLM :
CrewAI ne ab LiteLLM use karna shuru kar diya hai. LiteLLM ek tool hai jo CrewAI ko bohot sare LLM providers ke saath connect karne mein madad karta hai. Ye ek bridge ki tarah kaam karta hai, jisse CrewAI alag-alag LLM models ko asani se use kar sake. Ye flexibility deta hai ki har use case ke liye sabse acha model choose kiya ja sake.

Phir bhi, CrewAI abhi bhi LangChain tools ke saath compatible hai. Matlab, agar aap LangChain ke tools apne CrewAI agents mein use karte the, toh wo abhi bhi kaam karega aur agents ki capabilities ko improve karega.

LiteLLM ek Python SDK hai jo 100 se zyada LLMs ke saath kaam karna simple banata hai. Ye ek uniform interface deta hai, consistent output format banata hai, aur built-in retry aur fallback features ke sath aata hai. Ye developers ke liye helpful hai jo multiple LLMs ke sath kaam karte hain, jaise OpenAI, Anthropic, HuggingFace, Azure, aur dusre providers.

**Asaan alfaaz mein:**  
CrewAI ne LiteLLM introduce kiya hai jo bohot sare AI models ke saath kaam karne mein madad karta hai. Lekin LangChain tools ka support abhi bhi hai, toh dono ka faida utha sakte ho.


### 1. litellm installation command:
```python
 uv add litellm 
```

### 2. then take response from model using litellm :
```python
from litellm import completion

def gemini():
    response = completion(
        model="gemini/gemini-1.5-flash",
        messages=[{ "content": "Hello, how are you?","role": "user"}]
    )

    print(response)

```

## integrate langchain project using uv:

#### 1. install langchain google genai:
```python
uv add langchain_google_genai
```

### 2. then take response from model using langchain_google_genai :
```python
def langchain():
    model = ChatGoogleGenerativeAI (
    model="gemini-1.5-flash",
    temperature=0.9,
    )
    response = model.invoke("Which specific Mercedes model is considered one of the best?")
    print(response.content)
```


--------

# **CrewAi Installation Process:**

 ## First step :
  To install Visual Studio Microsoft C++ Build Tools.
 
 ## Second step :
 To install crewai run this command:
 ```python
 pip install --upgrade crewai crewai-tools      # for latest version
 ```

 ## Third step :
 To Verify whether Crewai is installed:
 ```python
 crewai --version
 pip freeze | findstr crewai
 ```

## Fourth step :
To Create CrewAi Project:
```python
crewai create crew crewai_installation  #(crewai_installation) its a project name
```
## Fifth step :
To Execute your CrewAI project :
```python
 crewai run    # For Run your project.
```


------------
Dono commands ka **clear** farq ye hai:  

### **1. Simple Project (`crew`)**
```sh
crewai create crew <project-name>
```
Ye command ek **basic CrewAI project** banati hai, jo manually configure karne ke liye zyada flexible hota hai. Is project mein sirf **basic files aur setup** hota hai, jisme tum agents aur workflows **apne hisaab se manually define** karte ho.  

**Use case:** Agar tum ek **custom CrewAI project** banana chahte ho jisme tum **apne agents, tasks aur workflows khud setup** karo, to ye best hai.  

---

### **2. Flow-Based Project (`flow`)**
```sh
crewai create flow <project-name>
```
Ye command ek **pre-structured workflow-based CrewAI project** banati hai. Isme kuch **pre-defined agents aur workflows** hote hain, jinka structure pehle se bana hota hai. Tumhe bas chhoti chhoti cheezein customize karni parti hain.  

**Use case:** Agar tum ek **automated flow chahte ho** jisme pehle se bana banaya system ho, aur sirf chhoti modifications karni ho, to ye best hai.  

---

### **Asaan lafzon mein farq:**  
- **"crew" wala project blank aur basic hota hai**, jisme tum apni marzi se sab kuch define karte ho.  
- **"flow" wala project ek pre-made setup hota hai**, jo ek structured system ke sath aata hai.  

Agar tum **scratch se build** karna chahte ho to `crew` use karo. Agar tum **pehle se bana banaaya flow chahte ho** to `flow` use karo.