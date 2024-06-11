import gradio as gr
import os

path = r"C:\迅雷下载"


def get_files(path, suffix):
    files_with_suffix = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(suffix) or file.endswith('mkv'):
                files_with_suffix.append(os.path.join(root, file))
    return files_with_suffix


def create_app():
    files = get_files(path, 'mp4')
    with gr.Blocks(title="视频下载") as demo:
        with gr.Row():
            choose = gr.Dropdown(choices=files)
            button = gr.Button(value='下载', variant='primary')
        with gr.Row():
            output = gr.Video(label="下载文件")
        button.click(fn=lambda x: x, inputs=choose, outputs=output)
    return demo


if __name__ == '__main__':
    app = create_app()
    app.launch(server_name="0.0.0.0", server_port=9000, share=False)
