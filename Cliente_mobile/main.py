from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import requests

SERVER_URL = 'http://127.0.0.1:5000'

class FavoritesApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        self.add_input = TextInput(hint_text='Enter image URL', size_hint_y=None, height=40)
        self.add_button = Button(text='Add Favorite', on_press=self.add_favorite, size_hint_y=None, height=40)
        self.update_button = Button(text='Update Favorites', on_press=self.refresh_favorites, size_hint_y=None, height=40)
        self.favorites_list = TextInput(readonly=True, size_hint_y=None, height=400)

        layout.add_widget(self.add_input)
        layout.add_widget(self.add_button)
        layout.add_widget(self.update_button)
        layout.add_widget(self.favorites_list)

        return layout

    def add_favorite(self, instance):
        url = self.add_input.text
        if url:
            try:
                response = requests.post(f'{SERVER_URL}/favorites?format=json', json={'url': url})
                if response.status_code == 200:
                    self.add_input.text = ''
                    self.refresh_favorites()
                else:
                    print(f"Error adding favorite: {response.status_code}")
            except Exception as e:
                print(f"Error adding favorite: {e}")

    def refresh_favorites(self, instance=None):
        try:
            response = requests.get(f'{SERVER_URL}/favorites?format=json')
            if response.status_code == 200:
                favorites = response.json()
                favorites_text = '\n'.join(favorite['url'] for favorite in favorites)
                self.favorites_list.text = favorites_text
            else:
                print(f"Error fetching favorites: {response.status_code}")
        except Exception as e:
            print(f"Error fetching favorites: {e}")

if __name__ == '__main__':
    FavoritesApp().run()
