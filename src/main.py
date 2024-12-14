from fasthtml.common import *
app,rt = fast_app()

#if you run this python file, a server will start 
#this is the home 
@rt('/')
def get(): return Div(P('Hello World!'), hx_get="/change")

# an example 'get' linking the hx_get 
@rt('/change')
def get(): return P('Nice to be here!', hx_get='/')

# simple wrapper to run web server locally
serve()