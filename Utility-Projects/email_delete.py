#All the imports usage are listed below
import imaplib #An import from imaplib, used to connect and operate on the mail server through IMAP
import email #An import from email, used to work with email messages
from email.header import decode_header #An import from email.header, used to decode encoded header text
import getpass #An import from getpass, used to read the password without showing it on screen


def connect_to_email(server, username, password): #this function connects to the IMAP server and logs in
    try:
        mail = imaplib.IMAP4_SSL(server)
        mail.login(username, password)
        print(f"\nConnected as: {username}")
        return mail
    except imaplib.IMAP4.error as e:
        print(f"\nAuthentication error: {e}")
        print("Tip: for Gmail, use an 'App Password' instead of your regular password.")
        return None
    except Exception as e:
        print(f"\nConnection error: {e}")
        return None


def decode_text(text): #this function decodes encoded email header text
    if text is None:
        return ""

    decoded_parts = decode_header(text)
    result = ""

    for part, charset in decoded_parts: #Create a loop, who will pass through each decoded part and rebuild the text
        if isinstance(part, bytes):
            try:
                result += part.decode(charset or "utf-8", errors="replace")
            except (LookupError, UnicodeDecodeError):
                result += part.decode("utf-8", errors="replace")
        else:
            result += part

    return result


def get_email_body(msg): #this function extracts the plain text body from an email message
    body = ""

    if msg.is_multipart():
        # Create a loop, who will pass through every part of the multipart message
        for part in msg.walk():
            content_type = part.get_content_type()
            content_disposition = str(part.get("Content-Disposition", ""))

            # Extract plain text parts that are not attachments
            if content_type == "text/plain" and "attachment" not in content_disposition:
                try:
                    charset = part.get_content_charset() or "utf-8"
                    payload = part.get_payload(decode=True)
                    if payload:
                        body += payload.decode(charset, errors="replace")
                except Exception:
                    pass

            # Also extract HTML parts that are not attachments
            elif content_type == "text/html" and "attachment" not in content_disposition:
                try:
                    charset = part.get_content_charset() or "utf-8"
                    payload = part.get_payload(decode=True)
                    if payload:
                        body += payload.decode(charset, errors="replace")
                except Exception:
                    pass
    else:
        # Handle single-part messages
        try:
            charset = msg.get_content_charset() or "utf-8"
            payload = msg.get_payload(decode=True)
            if payload:
                body = payload.decode(charset, errors="replace")
        except Exception:
            pass

    return body


def quote_imap_string(value): #this function escapes a value as an IMAP quoted string
    escaped_value = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped_value}"'.encode("utf-8")


def search_and_delete_emails(mail, keyword, imap_server, username, password): #this function searches and deletes emails, using server-side IMAP operations
    # Enable UTF-8 search support when available
    try:
        mail.enable("UTF8=ACCEPT")
    except Exception:
        pass

    # Select the inbox
    status, _ = mail.select("INBOX")

    if status != "OK":
        print("Could not open the inbox.")
        return mail

    print(f"\nSearching on the mail server for: '{keyword}'...")

    # Search for the keyword in the subject OR body
    search_term = quote_imap_string(keyword)

    status, data = mail.uid(
        "SEARCH",
        None,
        "OR",
        "SUBJECT",
        search_term,
        "BODY",
        search_term
    )

    if status != "OK":
        print("Error while searching for emails.")
        return mail

    # The server returns only message UIDs, not the entire emails
    matched_uids = data[0].split() if data and data[0] else []

    if not matched_uids:
        print(f"No emails found containing '{keyword}'.")
        return mail

    print(f"\n{len(matched_uids)} email(s) found.")
    print("The script will not download every email, making the process much faster.")

    confirmation = input(
        "\nDo you want to delete these emails? type YES to confirm: "
    ).strip().lower()

    if confirmation not in {"yes", "y", "sim", "s"}:
        print("\nOperation cancelled.")
        return mail

    # Reconnect before deletion in case the previous search took too long
    print("\nReconnecting before deletion...")

    try:
        mail.close()
    except Exception:
        pass

    try:
        mail.logout()
    except Exception:
        pass

    mail = connect_to_email(imap_server, username, password)

    if mail is None:
        print("Could not reconnect to the mail server.")
        return None

    status, _ = mail.select("INBOX")

    if status != "OK":
        print("Could not open the inbox after reconnecting.")
        return mail

    print("\nDeleting emails in batches...")

    deleted_count = 0
    failed_count = 0
    batch_size = 500

    # Create a loop, who will mark emails as deleted in groups instead of one at a time
    for start_index in range(0, len(matched_uids), batch_size):
        current_batch = matched_uids[
            start_index:start_index + batch_size
        ]

        # Create an IMAP UID set, for example: 123,124,125
        uid_set = b",".join(current_batch)

        status, _ = mail.uid(
            "STORE",
            uid_set,
            "+FLAGS.SILENT",
            "\\Deleted"
        )

        if status == "OK":
            deleted_count += len(current_batch)
        else:
            failed_count += len(current_batch)

        print(
            f"   Processed {min(start_index + batch_size, len(matched_uids))}"
            f"/{len(matched_uids)}...",
            end="\r"
        )

    print()

    # Permanently remove messages marked as deleted
    if deleted_count > 0:
        status, _ = mail.expunge()

        if status != "OK":
            print("Could not complete the final deletion.")
        else:
            print(f"{deleted_count} email(s) deleted successfully.")

    if failed_count > 0:
        print(f"{failed_count} email(s) could not be deleted.")

    return mail


def display_servers(): #this function displays a list of common IMAP servers for the user to choose from
    servers = {
        "1": ("imap.gmail.com",          "Gmail"),
        "2": ("imap-mail.outlook.com",   "Outlook / Hotmail"),
        "3": ("imap.yahoo.com",          "Yahoo"),
        "4": ("imap.mail.me.com",        "iCloud"),
        "5": ("imap.zoho.com",           "Zoho Mail"),
    }

    print("\nAvailable email servers:")
    print("=" * 55)
    for key, (server, name) in servers.items(): #Create a loop, who will print every available server option
        print(f"  [{key}] {name} ({server})")
    print(f"  [6] Other (enter manually)")
    print("=" * 55)

    return servers


def help_menu(): #Create a help menu, explaining how to use the app
    print("=" * 55)
    print("                    HELP MENU")
    print("=" * 55)
    print("This program searches for and deletes emails on an")
    print("IMAP mail server, based on a keyword.")
    print()
    print("STEPS:")
    print("  1. Choose the mail server")
    print("  2. Log in with your email and password")
    print("  3. Type a keyword to search for")
    print("  4. Confirm the deletion of the emails found")
    print()
    print("COMMANDS (during search):")
    print("  EXIT   -> close the program")
    print("=" * 55)


def main_menu(): #Give the option to the user, to start or access help_menu
    print("=" * 55)
    print("        DELETE EMAILS BY KEYWORD")
    print("=" * 55)
    while True: #Create a loop, who will ask the user to start or access the help menu
        choice = input("Type [S] to start or [H] for help:").upper()
        if choice == "S":
            break
        if choice == "H":
            help_menu()


def main():
    main_menu()

    # Display server options and get the user's choice
    servers = display_servers()
    choice = input("\nChoose a server (1-6): ").strip()

    if choice in servers:
        imap_server = servers[choice][0]
        print(f"   Server selected: {imap_server}")
    elif choice == "6":
        # Allow the user to enter a custom IMAP server address
        imap_server = input("   Enter the IMAP server address: ").strip()
    else:
        print("Invalid option!")
        return

    # Collect login credentials from the user
    username = input("\nEnter your email address: ").strip()
    password = input("Enter your password (or app password): ")

    # Attempt to connect to the mail server
    mail = connect_to_email(imap_server, username, password)
    if mail is None:
        return

    try:
        # Create a loop, who will let the user perform multiple searches in one session
        while True:
            keyword = input(
                "\nEnter the word or phrase to search for "
                "(or 'exit' to quit): "
            ).strip()

            if keyword.lower() in ["exit", "quit", "q"]:
                break

            if not keyword:
                print("Please enter a valid word or phrase.")
                continue

            # Search for and delete emails matching the keyword
            search_and_delete_emails(mail, keyword, imap_server, username, password)

    finally:
        # Always close the connection when done
        try:
            mail.close()
            mail.logout()
        except Exception:
            pass

        print("\nConnection closed. Goodbye!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        print("Programa interrompido pelo usuario.")
