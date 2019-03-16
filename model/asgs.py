
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
import uuid

KEYSPACE = 'security_groups'


class ASGModel(Model):
    __keyspace__ = KEYSPACE
    __connection__ = 'security-groups'
    __table_name__ = 'asg'
    id = columns.UUID(primary_key=True, default=uuid.uuid4)
    name = columns.Text(index=True)
    org = columns.Text(default='')
    space = columns.Text(default='')
    dst = columns.Text()
    protocol = columns.Text()
    dst_port = columns.Text()
    logging = columns.Boolean(default=False)
