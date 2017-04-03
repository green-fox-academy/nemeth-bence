class PostIt:
    background_color = 'yellow'
    text =  "That's fine!"
    text_color = 'red'

    def __init__(self, background_color, text_color, text):
        self.background_color = background_color
        self.text_color = text_color
        self.text = text

PostIt1 = PostIt ('orange' , 'blue', 'Idea 1')
PostIt2 = PostIt ('pink' , 'black', 'Awesome')
PostIt3 = PostIt ('yellow' , 'green', 'Superb!')

print('PostIt1: ' + PostIt1.background_color + ', PostIt1: ' + PostIt1.text_color + ', PostIt1: ' + PostIt1.text)
print('PostIt2: ' + PostIt2.background_color + ', PostIt2: ' + PostIt2.text_color + ', PostIt2: ' + PostIt2.text)
print('PostIt3: ' + PostIt3.background_color + ', PostIt3: ' + PostIt3.text_color + ', PostIt3: ' + PostIt3.text)
