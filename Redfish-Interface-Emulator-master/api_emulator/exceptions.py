# Copyright Notice:
# Copyright 2016 Distributed Management Task Force, Inc. All rights reserved.
# License: BSD 3-Clause License. For full text see link: https://github.com/DMTF/Redfish-Interface-Emulator/LICENSE.md

# Exceptions thrown in the Emulator

class ConfigurationError(Exception):
    pass

class StaticLoadError(Exception):
    pass

class CreatePooledNodeError(Exception):
    pass

class RemovePooledNodeError(Exception):
    pass

class OVFParseError(Exception):
    pass

class EventSubscriptionError(Exception):
    pass

