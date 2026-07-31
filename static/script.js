async function loadGuilds() {
    try {
        const response = await fetch("/api/guilds");
        const guilds = await response.json();

        const select = document.getElementById("guild");
        select.innerHTML = "";

        guilds.forEach(guild => {
            const option = document.createElement("option");
            option.value = guild.id;
            option.textContent = guild.name;
            select.appendChild(option);
        });

        await loadChannels();

    } catch (err) {
        alert("Lỗi loadGuilds: " + err);
    }
}

async function loadChannels() {
    try {
        const guild = document.getElementById("guild").value;


        if (!guild) return;

        const response = await fetch("/api/channels?guild=" + guild);
        const channels = await response.json();


        const select = document.getElementById("channel");
        select.innerHTML = "";

        channels.forEach(channel => {
            const option = document.createElement("option");
            option.value = channel.id;
            option.textContent = "#" + channel.name;
            select.appendChild(option);
        });

    } catch (err) {
        alert("Lỗi loadChannels: " + err);
    }
}

window.onload = function () {
    document.getElementById("guild").addEventListener("change", loadChannels);
    loadGuilds();
}; 

document.getElementById("send").addEventListener("click", async () => {

    const channel = document.getElementById("channel").value;
    const message = document.getElementById("message").value;

    if (!channel || !message) {
        alert("Vui lòng chọn channel và nhập nội dung.");
        return;
    }

    const response = await fetch("/api/send", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            channel: channel,
            message: message
        })
    });

    const result = await response.json();

    if (result.success) {
        alert("✅ Đã gửi thành công!");
        document.getElementById("message").value = "";
    } else {
        alert("❌ Gửi thất bại!");
    }

});
