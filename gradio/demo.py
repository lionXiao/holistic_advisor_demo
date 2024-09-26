import gradio as gr
from api import chat_completion


class Gradio(object):
    def __init__(self):
        self.select_image_index = 0
        self.file_id_dict = {"海尔烘干机HGS100-356": "cramrsdfc7ucc73pb1t0"}
        self.file_id = ""

    def chat_respond(self, message, chat_history):
        bot_message = chat_completion(message, self.file_id)
        chat_history.append((message, bot_message))
        return "", chat_history

    def item_list_on_select(self, value):
        self.file_id = self.file_id_dict[value]
        print(f"file_id: {self.file_id}, value: {value}")
        return ""

    def launch(self):
        with gr.Blocks() as demo:
            chatbot = gr.Chatbot()
            dropdown = gr.Dropdown(list(self.file_id_dict.keys()), label="选择电器")
            msg = gr.Textbox(label="输入文字", placeholder="请输入想提问的问题")
            clear = gr.ClearButton([msg, chatbot])
            dropdown.select(fn=self.item_list_on_select, inputs=[dropdown], outputs=[])
            msg.submit(self.chat_respond, [msg, chatbot], [msg, chatbot])

        demo.queue(max_size=10)
        demo.launch(server_name='0.0.0.0', server_port=7860)


if __name__ == "__main__":
    gradio = Gradio()
    gradio.launch()

