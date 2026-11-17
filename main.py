from pyscript import document


grade_7 = {
    "Michael Jackson",
    "Beyoncé Giselle Knowles"
}

grade_8 = {
    "Pinkie Pie",
    "佐伊 雅普"
}

grade_9 = {
    "Maeo Maeo",
    "Goyangi Meokda"
}

grade_10 = {
    "AllanEdgar Poe",
    "Simon Mactavish"
}


def add_member_handler(event=None):

    first_name = document.querySelector("#first-name").value.strip()
    last_name = document.querySelector("#last-name").value.strip()

    member_name = f"{first_name} {last_name}".strip().title()

    all_members = (
        grade_7
        | grade_8
        | grade_9
        | grade_10
        | {member_name}
    ) - {""}

    member_count = len(all_members)

    member_display = "".join(
        f'<span class="member-badge">{member}</span>'
        for member in sorted(all_members)
    )

    document.querySelector("#total-output").innerHTML = str(member_count)

    document.querySelector("#member-list-output").innerHTML = member_display

    document.querySelector("#first-name").value = ""
    document.querySelector("#last-name").value = ""