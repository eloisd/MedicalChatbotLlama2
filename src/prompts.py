prompt_template="""
Use the following pieces of information to answer the user's question.
If you don't know the answer, just say that you don't know, don't try to make up an answer.

Context: {context}
Question: {question}

Only return the helpful answer below and nothing else.
Helpful answer:
"""

promp_question_template = """
Give me a detailed description of what is acne. 
Give me possible causes and concequences. 
And after a theorical part, give an explaning example that 9 years old child could understand.
"""