import logging

import gradio as gr
from predict import transcribe
from app_utils import save_to_text

css = "footer {display: none !important;} #sp-gradio-container {min-height: 0px !important;}"

def show_download_button(dummy: str = 'show'):
    return gr.update(visible=True)

with gr.Blocks(css=css) as demo:

    gr.HTML(
        """
            <div style="text-align: center; max-width: 700px; margin: 0 auto;">
            <div
                style="
                display: inline-flex;
                align-items: center;
                gap: 0.8rem;
                font-size: 1.75rem;
                "
            >
                <h1 style="font-weight: 900; margin-bottom: 7px; line-height: normal;">
                Transcription
                </h1>
            </div>
            <p style="margin-bottom: 10px; font-size: 94%">
                Faster-Whisper with CTranslate2
            </p>
        """
    )

    audio_input: gr.Audio = gr.Audio(label='Input', type='filepath')
    with gr.Row(equal_height=False):

        with gr.Column(variant='compact'):
            with gr.Row():
                audio_button: gr.Button = gr.Button(value='Transcribe')
                audio_download_button: gr.Button = gr.Button(value='Download Transcript')
            audio_output: gr.Textbox = gr.Textbox(show_label=True, label='Transcript', visible=True)
            audio_obj: gr.File = gr.File(label='Output File', visible=False)

    audio_button.click(transcribe, audio_input, audio_output)
    audio_download_button.click(save_to_text, inputs=[audio_output, gr.Textbox(value='transcript', visible=False)], outputs=audio_obj)
    audio_download_button.click(show_download_button, outputs=audio_obj)


if __name__ == "__main__":
    logging.basicConfig(format="[%(asctime)s] %(levelname)s: %(message)s")

    demo.launch(
        server_name="0.0.0.0",
        server_port=8080
    )
