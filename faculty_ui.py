# project/faculty_ui.py
from flask import Blueprint, render_template, abort
from flask_login import login_required, current_user
from functools import wraps

faculty_ui = Blueprint("faculty_ui", __name__)

# ─────────────────────────────────────────
# Role guard: only allow users with role='faculty'
# ─────────────────────────────────────────
def role_required(required_role):
    def decorator(view_func):
        @wraps(view_func)
        def wrapped(*args, **kwargs):
            if not current_user.is_authenticated:
                abort(401)  # or redirect to login if you prefer

            if getattr(current_user, "role", None) != required_role:
                abort(403)  # Forbidden

            return view_func(*args, **kwargs)
        return wrapped
    return decorator

# ─────────────────────────────────────────
# Faculty dashboard
# ─────────────────────────────────────────
@faculty_ui.route("/faculty/dashboard", methods=["GET"])
@login_required
@role_required("faculty")
def faculty_dashboard():
    # main landing page for faculty
    return render_template("faculty_dashboard.html")

# ─────────────────────────────────────────
# Print exam log
# ─────────────────────────────────────────
@faculty_ui.route("/faculty/print-log", methods=["GET"])
@login_required
@role_required("faculty")
def faculty_print_log():
    # TODO: replace with your real template/logic
    return render_template("print_exam_log.html")

# ─────────────────────────────────────────
# Search appointments
# ─────────────────────────────────────────
@faculty_ui.route("/faculty/search-appointments", methods=["GET"])
@login_required
@role_required("faculty")
def faculty_search_appointments():
    # TODO: replace with your real template/logic
    return render_template("search_appointments.html")
