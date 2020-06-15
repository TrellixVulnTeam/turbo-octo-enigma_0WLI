from blog import Blog

MENU_PROMPT = 'Enter "c" to create a blog, "l" to list blogs, "r" to read one,"p" to create a post, or "q" to quit'

blogs = dict()  # blog_name : blog_object


def menu():
    # show the user the available blog
    # let the user make a choice from shown menu
    # make an action with that choice
    # eventually exit

    print_blogs()
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()
        selection = input(MENU_PROMPT)


def print_blogs():
    for key, blog in blogs.items():
        print('- {}'.format(blog))


def ask_create_blog(name_of_author, new_blog_title):
    title = input('what would you like to title this blog post? ')
    author = input('what is your name? ')

    blogs[title] = Blog(title, author)


def ask_read_blog():
    requested_blog = input('what is the blog you would like to read? ')
    print(requested_blog)


def ask_create_post():
    requested_blog = input('what is the blog you would like to read? ')
    # post title and post content
    # create a new post specified in the title
