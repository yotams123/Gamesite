import website.templates

app = website.templates.create_app()

if __name__ == '__main__':
    app.run(debug=True)
