
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table

from cassandra.cluster import Cluster

from model.asgs import ASGModel, KEYSPACE

cluster = Cluster(contact_points=['docker-desktop'], port=9042)
session = cluster.connect(KEYSPACE)
connection = connection.register_connection('security-groups', session=session)

for n in ASGModel.objects.all():
    n.delete()
