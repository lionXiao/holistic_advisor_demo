import gradio as gr
from api.chat import chat_completion
from api.kb import kb_create_api


class Gradio(object):
    def __init__(self):
        self.select_image_index = 0
        self.file_id_dict = {"海尔烘干机HGS100-356": "cramrsdfc7ucc73pb1t0"}
        self.file_id = ""

    def chat_respond(self, message, chat_history):
        bot_message = chat_completion(message, self.file_id)
        chat_history.append((message, bot_message))
        return "", chat_history

    def kb_create(self, kb_first_title: str, kb_second_title: str, kb_id: str, description: str, user_id: str) -> str:
        check_params = [kb_first_title, kb_second_title, user_id]
        for param in check_params:
            if not param:
                # 返回提示框
                return "请输入完整参数"
        result = kb_create_api(kb_first_title, kb_second_title, kb_id, description, user_id)
        return result

    def item_list_on_select(self, value):
        self.file_id = self.file_id_dict[value]
        print(f"file_id: {self.file_id}, value: {value}")
        return ""

    def launch(self):
        with gr.Blocks() as demo:
            gr.Markdown(
                """
                # 说明书 demo
                """
            )
            with gr.Tab("对话"):
                chatbot = gr.Chatbot()
                chat_dropdown = gr.Dropdown(list(self.file_id_dict.keys()), label="选择电器")
                chat_msg = gr.Textbox(label="输入文字", placeholder="请输入想提问的问题")
                clear = gr.ClearButton([chat_msg, chatbot])
                chat_dropdown.select(fn=self.item_list_on_select, inputs=[chat_dropdown], outputs=[])
                chat_msg.submit(self.chat_respond, [chat_msg, chatbot], [chat_msg, chatbot])

            with gr.Tab("知识库管理"):
                with gr.Tab("创建知识库"):
                    kb_create_first_title_TB = gr.Textbox(label="请输入一级标签")
                    kb_create_scend_title_TB = gr.Textbox(label="请输入二级标签")
                    kb_craete_description_TB = gr.Textbox(label="请输入知识库描述")
                    kb_create_id_TB = gr.Textbox(label="请输入知识库ID(可不填)")
                    kb_create_user_id_TB = gr.Textbox(label="请输入用户ID")
                    kb_create_btn = gr.Button("创建知识库")
                    kb_create_msg = gr.Textbox(label="创建结果")
                    kb_create_btn.click(fn=self.kb_create, inputs=[kb_create_first_title_TB, kb_create_scend_title_TB, kb_create_id_TB, kb_craete_description_TB, kb_create_user_id_TB], outputs=kb_create_msg)
            chat_dropdown.select(fn=self.item_list_on_select, inputs=[chat_dropdown], outputs=[])
            chat_msg.submit(self.chat_respond, [chat_msg, chatbot], [chat_msg, chatbot])
        demo.queue(max_size=10)
        demo.launch(server_name='0.0.0.0', server_port=7860)


if __name__ == "__main__":
    gradio = Gradio()
    gradio.launch()

