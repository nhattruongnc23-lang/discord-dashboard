from flask import Blueprint, render_template, jsonify, request
from bot.client import get_guilds, get_channels, send_message

main = Blueprint("main", __name__)


@main.route("/")
def dashboard():
    return render_template("dashboard.html")


@main.route("/api/guilds")
def api_guilds():
    return jsonify(get_guilds())


@main.route("/api/channels")
def api_channels():
    guild_id = request.args.get("guild")

    if not guild_id:
        return jsonify([])

    return jsonify(get_channels(guild_id))

@main.route("/api/send", methods=["POST"])
def api_send():
    data = request.get_json()

    channel_id = data.get("channel")
    message = data.get("message")

    if not channel_id or not message:
        return jsonify({
            "success": False,
            "error": "Thiếu dữ liệu."
        })

    ok = send_message(channel_id, message)

    return jsonify({
        "success": ok
    })
