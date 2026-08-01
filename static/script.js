// ============================================================
//                  MEOW MEOW CONTROL PANEL
// ============================================================

// ==========================
// Sidebar
// ==========================

const menuBtn = document.getElementById("menu-toggle");
const sidebar = document.getElementById("sidebar");

if (menuBtn && sidebar) {

    menuBtn.addEventListener("click", () => {

        sidebar.classList.toggle("open");

    });

}

document.addEventListener("click", (e) => {

    if (
        window.innerWidth <= 768 &&
        sidebar &&
        sidebar.classList.contains("open") &&
        !sidebar.contains(e.target) &&
        !menuBtn.contains(e.target)
    ) {

        sidebar.classList.remove("open");

    }

});

// ==========================
// Thành phần Dashboard
// ==========================

const guildList = document.getElementById("guild-list");
const channelList = document.getElementById("channel-list");

const messageBox = document.getElementById("message");
const sendBtn = document.getElementById("send");
const statusBox = document.getElementById("send-status");

let selectedGuild = "";
let selectedChannel = "";

// ==========================
// Hiển thị thông báo
// ==========================

function showStatus(text, type) {

    if (!statusBox) return;

    statusBox.className = "";

    statusBox.classList.add(type);

    statusBox.innerHTML = text;

    setTimeout(() => {

        statusBox.className = "";

        statusBox.innerHTML = "";

    }, 3000);

}

// ==========================
// Tải Server
// ==========================

async function loadGuilds() {

    guildList.innerHTML = "Đang tải máy chủ...";

    try {

        const res = await fetch("/api/guilds");

        const guilds = await res.json();

        guildList.innerHTML = "";

        if (guilds.length === 0) {

            guildList.innerHTML = "Không có máy chủ.";

            return;

        }

        guilds.forEach((guild, index) => {

            const item = document.createElement("div");

            item.className = "list-item";

            item.innerHTML = "🖥 " + guild.name;

            item.onclick = () => {

                selectGuild(guild.id, item);

            };

            guildList.appendChild(item);

            if (index === 0) {

                item.classList.add("active");

                selectedGuild = guild.id;

                loadChannels(guild.id);

            }

        });

    }

    catch {

        guildList.innerHTML = "❌ Không thể tải danh sách máy chủ.";

    }

}

// ==========================
// Chọn Server
// ==========================

function selectGuild(id, element) {

    selectedGuild = id;

    document
        .querySelectorAll("#guild-list .list-item")
        .forEach(item => {

            item.classList.remove("active");

        });

    element.classList.add("active");

    loadChannels(id);

}

// ==========================
// Tải Channel
// ==========================

async function loadChannels(guildId) {

    channelList.innerHTML = "Đang tải kênh...";

    try {

        const res = await fetch("/api/channels?guild=" + guildId);

        const channels = await res.json();

        channelList.innerHTML = "";

        if (channels.length === 0) {

            channelList.innerHTML = "Không có kênh.";

            return;

        }

        channels.forEach(channel => {

            const item = document.createElement("div");

            item.className = "list-item";

            item.innerHTML = "💬 #" + channel.name;

            item.onclick = () => {

                selectChannel(channel.id, item);

            };

            channelList.appendChild(item);

        });

    }

    catch {

        channelList.innerHTML = "❌ Không thể tải kênh.";

    }

}

// ==========================
// Chọn Channel
// ==========================

function selectChannel(id, element) {

    selectedChannel = id;

    document
        .querySelectorAll("#channel-list .list-item")
        .forEach(item => {

            item.classList.remove("active");

        });

    element.classList.add("active");

}

// ==========================
// Gửi thông báo
// ==========================

async function sendMessage() {

    if (!selectedChannel) {

        showStatus("❌ Vui lòng chọn một kênh.", "error");

        return;

    }

    if (!messageBox.value.trim()) {

        showStatus("❌ Nội dung không được để trống.", "error");

        return;

    }

    sendBtn.disabled = true;

    sendBtn.innerHTML = "⏳ Đang gửi...";

    try {

        const res = await fetch("/api/send", {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify({

                channel: selectedChannel,

                message: messageBox.value

            })

        });

        const data = await res.json();

        if (data.success) {

            messageBox.value = "";

            showStatus("✅ Đã gửi thông báo thành công.", "success");

        } else {

            showStatus(

                "❌ " + (data.error || "Gửi thất bại."

