# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ListEnvironmentsPayload(Model):
    """Represents the payload to list environments owned by a user.

    :param lab_id: The resource Id of the lab
    :type lab_id: str
    """

    _attribute_map = {
        'lab_id': {'key': 'labId', 'type': 'str'},
    }

    def __init__(self, *, lab_id: str=None, **kwargs) -> None:
        super(ListEnvironmentsPayload, self).__init__(**kwargs)
        self.lab_id = lab_id
