
from cassandra.cluster import Cluster
from cassandra.cqlengine import connection

from model.asgs import ASGModel

KEYSPACE = 'security_groups'

cluster = Cluster(contact_points=['docker-desktop'], port=9042)
session = cluster.connect(KEYSPACE)
connection.register_connection('security-groups', session=session)

for r in ASGModel.objects.all():
    print "%s dst=%s:%s log=%s" % (r.name, r.dst, r.dst_port, r.logging)
