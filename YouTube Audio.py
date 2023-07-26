import pytube
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class UlliyaDownloader(App):
    def build(self):
        # Create GUI elements
        label_title = Label(text='ULLIYA - SONGS DOWNLOADER', font_size=25, bold=True)
        label_url = Label(text='Enter the YouTube video URL:', font_size=18)
        self.input_url = TextInput(multiline=False, size_hint_y=None, height=30, font_size=18)
        button_download = Button(text='Download', font_size=18, background_color=[0, 1, 0, 1])
        button_download.bind(on_press=self.download_audio)

        # Add elements to layout
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(label_title)
        layout.add_widget(label_url)
        layout.add_widget(self.input_url)
        layout.add_widget(button_download)

        return layout

    def download_audio(self, instance):
        # Get the YouTube video URL from input
        url = self.input_url.text

        # Create a YouTube object and get the highest bitrate audio stream
        yt = pytube.YouTube(url)
        audio_streams = yt.streams.filter(only_audio=True).order_by('bitrate').desc()
        audio_stream = audio_streams.first()

        # Download the audio stream with a higher chunk size to improve download speed
        audio_file = audio_stream.download(filename="audio", chunk_size=512 * 512)

        # Display success message
        message = 'Audio downloaded successfully at: {}'.format(audio_file)
        self.input_url.text = message


if __name__ == '__main__':
    UlliyaDownloader().run()
