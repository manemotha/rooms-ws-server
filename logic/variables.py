database_uri = "mongodb://localhost:27017"

# namespaces
unknown_namespace: str = "unknown namespace"

# account & account-dir
account_generated_true: str = "account generated: true"
account_deactivated_true: str = "account deactivate: true"
account_exists_true: str = "account exists: true"
account_exists_false: str = "account exists: false"

# account update
account_updateUsername_exists_true: str = "account updateUsername exists: true"
account_username_updated_true: str = "username updated: true"
account_password_update_true: str = "password updated: true"
account_updatePassword_match_oldPassword: str = "password update: updatePassword match oldPassword"

# access
account_access_granted: str = "access granted"
account_access_denied_password: str = "access denied: incorrect password"
account_access_denied_passwordhash: str = "access denied: password not hashed \"account removed\""
# character
username_unwanted_character: str = "unwanted character in username"

# database
users_table_name: str = "users"
users_database_name: str = "demo"

# rooms
room_generated_true: str = "room generated: true"
room_exists_false: str = "room exists: false"
room_deleted_true: str = "room deleted: true"
room_match_found: str = "room match found: true"

# directory
# accounts parent directory
database_directory = "storage/database"
