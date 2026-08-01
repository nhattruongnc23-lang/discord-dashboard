# ============================================================
#                  MEOW MEOW CONTROL PANEL
# ------------------------------------------------------------
# Chức năng:
# Các API phục vụ Dashboard.
# ============================================================

from flask import Blueprint, jsonify, request

from bot.client import get_guilds, get_channels, send_message

# ==========================
# Blueprint
# ==========================

api = Blueprint("api", __name__)

# ==========================
# Danh sách máy chủ
# ==========================

@api.route("/api/guilds")
def api_guilds():

    return jsonify(get_guilds())

# ==========================
# Danh sách kênh
# ==========================

@api.route("/api/channels")
def api_channels():

    guild_id = request.args.get("guild")

    if not guild_id:
        return jsonify([])

    return jsonify(get_channels(guild_id))

# ==========================
# Gửi tin nhắn
# ==========================

@api.route("/api/send", methods=["POST"])
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
