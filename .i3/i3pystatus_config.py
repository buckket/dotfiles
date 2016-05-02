from i3pystatus import Status

status = Status(standalone=True)

status.register("clock",
    format="%a %d.%m.%Y %T",)

status.register("pomodoro",
    sound="/home/loom/.i3/bleep_normal.wav",)

status.register("load",
    format="{avg1}",)

status.register("temp",
    format="{temp:.0f}°C",)

status.register("battery",
    format="B{status}/{consumption:.2f}W {percentage:.2f}% {remaining:%E%hh:%Mm}",
    alert=True,
    alert_percentage=5,
    status={
        "DIS": "⌄",
        "CHR": "⌃",
        "FULL": "⌆",
    },)

status.register("network",
    interface="enp0s25",
    format_up="E⌃",
    format_down="E⌄")

status.register("network",
    interface="wlp3s0",
    dynamic_color=False,
    format_up="W⌃ {essid} ({quality:.0f}%)",
    format_down="W⌄",)

status.register("disk",
    path="/home/buckket",
    format="⌂ {avail}G",)

status.register("pulseaudio",
        format="♪ {volume}%",)

status.register("keyboard_locks",
    format="{caps}",
    caps_off="",)

status.run()

