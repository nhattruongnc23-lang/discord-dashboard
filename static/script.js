// ==========================
// Meow Meow UI
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
// Discord API
// ==========================

const guild = document.getElementById("guild");
const channel = document.getElementById("channel");
const message = document.getElementById("message");
const send = document.getElementById("send");

// Tải danh sách server
async function loadGuilds() {

    if (!guild) return;

    const res = await fetch("/api/guilds");
    const data = await res.json();

    guild.innerHTML = "";

    data.forEach(g => {

        guild.innerHTML += `
            <option value="${g.id}">
                ${g.name}
            </option>
        `;

    });

    if (data.length > 0) {

        loadChannels();

    }

}

// Tải danh sách channel
async function loadChannels() {

    if (!guild || !channel) return;

    const res = await fetch("/api/channels?guild=" + guild.value);
    const data = await res.json();

    channel.innerHTML = "";

    data.forEach(c => {

        channel.innerHTML += `
            <option value="${c.id}">
                # ${c.name}
            </option>
        `;

    });

}

if (guild) {

    guild.addEventListener("change", loadChannels);

}

// Gửi tin nhắn
if (send) {

    send.addEventListener("click", async () => {

        const res = await fetch("/api/send", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({

                channel: channel.value,

                message: message.value

            })

        });

        const data = await res.json();

        if (data.success) {

            alert("✅ Đã gửi thành công!");

            message.value = "";

        } else {

            alert("❌ " + (data.error || "Gửi thất bại"));

        }

    });

}

loadGuilds();

