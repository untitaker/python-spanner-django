# Copyright 2020 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd

from django.db.backends.base.introspection import (
    BaseDatabaseIntrospection, TableInfo,
)


class DatabaseIntrospection(BaseDatabaseIntrospection):
    def get_table_list(self, cursor):
        """Return a list of table and view names in the current database."""
        # The second TableInfo field is 't' for table or 'v' for view.
        return [TableInfo(row[0], 't') for row in cursor.list_tables()]