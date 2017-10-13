       self.owner_id = config.get('Permissions', 'OwnerID', fallback=ConfigDefaults.owner_id)
66	        self.command_prefix = config.get('Chat', 'CommandPrefix', fallback=ConfigDefaults.command_prefix)
67	        self.bound_channels = config.get('Chat', 'BindToChannels', fallback=ConfigDefaults.bound_channels)
