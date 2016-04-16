import web

urls = ( '/', 'index')

app = web.application( urls, globals() )

# neglected to set up template render
render = web.template.render('templates/')


# err: tried to def index()

class index:
    def GET(self):
        # err: forgot to indent
        hero = "You are the hero that gotham deserves."
        # err: forgot how to render templates
        return render.index(greeting = hero)

if __name__ == "__main__":
    app.run()
