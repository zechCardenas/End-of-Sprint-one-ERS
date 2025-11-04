# project/student_ui.py
from flask import Blueprint, render_template, abort
from flask_login import login_required, current_user
from functools import wraps

student_ui = Blueprint("student_ui", __name__)

# ─────────────────────────────────────────
# Role guard: only allow users with role='student'
# ─────────────────────────────────────────
def role_required(required_role):
    def decorator(view_func):
        @wraps(view_func)
        def wrapped(*args, **kwargs):
            # Must be logged in
            if not current_user.is_authenticated:
                # you could redirect to login instead of abort if your app prefers
                abort(401)

            # Must match required role
            if getattr(current_user, "role", None) != required_role:
                abort(403)  # Forbidden

            return view_func(*args, **kwargs)
        return wrapped
    return decorator

# ─────────────────────────────────────────
# Student dashboard (landing after login)
# ─────────────────────────────────────────
@student_ui.route("/student/dashboard", methods=["GET"])
@login_required
@role_required("student")
def student_dashboard():
    # Renders your student dashboard template
    # (this is the file you showed me earlier)
    return render_template("dashboard.html")

# ─────────────────────────────────────────
# Make an appointment
# ─────────────────────────────────────────
@student_ui.route("/student/exams", methods=["GET"])
@login_required
@role_required("student")
def student_exams():
    # TODO: real template; temporary stub keeps things working
    return render_template("schedule_exam.html")

# ─────────────────────────────────────────
# View my appointments
# ─────────────────────────────────────────
@student_ui.route("/student/appointments", methods=["GET"])
@login_required
@role_required("student")
def student_appointments():
    # TODO: real template; temporary stub keeps things working
    return render_template("appointments.html")


