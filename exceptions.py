# Something went wrong during the processing of a command
19	class CommandError(MusicbotException):
20	    pass
21	
22	# Something went wrong during the processing of a song/ytdl stuff
…	
33	# The user doesn't have permission to use a command
34	class PermissionsError(CommandError):
35	    @property
36	    def message(self):
