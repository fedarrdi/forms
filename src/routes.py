from flask import render_template, request, redirect, url_for
from models import Form, Response

def register_routes(app):
    @app.route("/")
    def home():
        return render_template("base.html")

    @app.route("/create", methods=["GET", "POST"])
    def create_form():
        if request.method == "POST":
            form_data = {
                "name": request.form["name"],
                "fields": request.form.getlist("fields[]")
            }
            Form.create_form(form_data)
            return redirect(url_for("home"))
        return render_template("form_create.html")

    @app.route("/fill/<form_id>", methods=["GET", "POST"])
    def fill_form(form_id):
        form = Form.get_form(form_id)
        if request.method == "POST":
            response_data = request.form.to_dict()
            Response.submit_response(form_id, response_data)
            return redirect(url_for("home"))
        return render_template("form_fill.html", form=form)

    @app.route("/results/<form_id>")
    def view_results(form_id):
        responses = Response.get_responses(form_id)
        return render_template("form_results.html", responses=responses)

