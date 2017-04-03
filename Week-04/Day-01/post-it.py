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

print('PostIt1: '+ 'orange ' + 'blue ' + 'Idea 1')
print('PostIt2: '+ 'pink ' + 'black ' + 'Awesome')
print('PostIt3: '+ 'yellow ' + 'green ' + 'Superb!')
