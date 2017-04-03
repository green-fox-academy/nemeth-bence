class BlogPost:
    authorname = ''
    title = ''
    text =  ''
    publicationDate = ''

    def __init__(self, authorname, title, text, publicationDate):
        self.authorname = authorname
        self.title = title
        self.text = text
        self.publicationDate = publicationDate

BlogPost1 = BlogPost ('John Doe' , 'Lorem Ipsum', 'Lorem ipsum dolor sit amet.', '2000.05.04')
BlogPost2 = BlogPost ('Tim Urban' , 'Wait but why', 'A popular long-form, stick-figure-illustrated blog about almost everything.', '2010.10.10.')
BlogPost3 = BlogPost ('William Turton' , 'One Engineer Is Trying to Get IBM to Reckon With Trump', "Daniel Hanley, a cybersecurity engineer at IBM, doesn’t want to be the center of attention. When I asked to take his picture outside one of IBM’s New York City offices, he told me that he wasn’t really into the whole organizer profile thing.", '2017.03.28.')

print('BlogPost1: ' + BlogPost1.authorname + ', BlogPost1: ' + BlogPost1.title + ', BlogPost1: ' + BlogPost1.text + ', BlogPost1: ' + BlogPost1.publicationDate)
print('BlogPost2: ' + BlogPost2.authorname + ', BlogPost2: ' + BlogPost2.title + ', BlogPost2: ' + BlogPost2.text + ', BlogPost2: ' + BlogPost2.publicationDate)
print('BlogPost3: ' + BlogPost3.authorname + ', BlogPost3: ' + BlogPost3.title + ', BlogPost3: ' + BlogPost3.text + ', BlogPost3: ' + BlogPost3.publicationDate)
