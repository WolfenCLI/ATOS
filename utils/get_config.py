import yaml

with open('config/config.yml', 'r+') as f: config = yaml.safe_load(f)

### System
debug_mode                          = config["system"]["debug"]

### File paths
tournoi_path                        = config["paths"]["tournoi"]
participants_path                   = config["paths"]["participants"]
waiting_list_path                   = config["paths"]["waiting_list"]
stream_path                         = config["paths"]["stream"]
stagelist_path                      = config["paths"]["stagelist"]
auto_mode_path                      = config["paths"]["auto_mode"]
ranking_path                        = config["paths"]["ranking"]

### Locale
language                            = config["system"]["language"]

### Discord prefix
bot_prefix                          = config["discord"]["prefix"]

### Auto-mode
auto_mode                           = config["system"]["auto_mode"]

### Bulk-mode
bulk_mode                           = config["system"]["bulk_mode"]

### Use guild name?
use_guild_name                      = config["system"]["use_guild_name"]

#### Discord IDs
guild_id                            = config["discord"]["guild"]

### Server channels
blabla_channel_id                   = config["discord"]["channels"]["blabla"]
annonce_channel_id                  = config["discord"]["channels"]["annonce"]
check_in_channel_id                 = config["discord"]["channels"]["check_in"]
inscriptions_channel_id             = config["discord"]["channels"]["inscriptions"]
scores_channel_id                   = config["discord"]["channels"]["scores"]
stream_channel_id                   = config["discord"]["channels"]["stream"]
queue_channel_id                    = config["discord"]["channels"]["queue"]
tournoi_channel_id                  = config["discord"]["channels"]["tournoi"]
resultats_channel_id                = config["discord"]["channels"]["resultats"]
roles_channel_id                    = config["discord"]["channels"]["roles"]
to_channel_id                       = config["discord"]["channels"]["to"]

### Info, non-interactive channels
deroulement_channel_id              = config["discord"]["channels"]["deroulement"]
faq_channel_id                      = config["discord"]["channels"]["faq"]

### Server categories
tournoi_cat_id                      = config["discord"]["categories"]["tournoi"]
winner_cat_id                       = config["discord"]["categories"]["winner"]
looser_cat_id                       = config["discord"]["categories"]["looser"]

### Role IDs
challenger_id                       = config["discord"]["roles"]["challenger"]
to_id                               = config["discord"]["roles"]["to"]
streamer_id                         = config["discord"]["roles"]["streamer"]

### Custom emojis
server_logo                         = config["discord"]["emojis"]["logo"]

#### Challonge
challonge_user                      = config["challonge"]["user"]

### Tokens
bot_secret                          = config["discord"]["secret"]
challonge_api_key                   = config["challonge"]["api_key"]
