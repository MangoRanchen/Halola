from discord import User as discord_User
6	
7	
8	class PermissionsDefaults:
9	    perms_file = 'config/permissions.ini'
10	
11	    CommandWhiteList = set()
12	    CommandBlackList = set()
13	    IgnoreNonVoice = set()
14	    GrantToRoles = set()
15	    UserList = set()
