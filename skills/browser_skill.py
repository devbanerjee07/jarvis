from actions.actions import execute


def run(intent):
    website = intent.get("website", "")

    execute(website)

    return True