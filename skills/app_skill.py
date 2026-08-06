from actions.actions import execute


def run(intent):
    app = intent.get("app", "")

    execute(app)

    return True