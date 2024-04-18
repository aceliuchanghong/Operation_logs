import gradio as gr

from Ocr.utils import *

with gr.Blocks() as demo:
    img_file = gr.Image(type="filepath")
    b1 = gr.Button("OCR")
    text = gr.Textbox()
    b1.click(get_text, inputs=img_file, outputs=text)

demo.launch()
