"""_summary_
     # Gradio 
        https://gradio.app/             
        https://github.com/gradio-app/gradio     
        
        
Returns:
    _type_: _description_
"""
import gradio as gr

def greet(name):
    return "Hello " + name + " !"

demo = gr.Interface(fn=greet, inputs="text", outputs="text")


if __name__ == "__main__":
    demo.launch(share=True)
