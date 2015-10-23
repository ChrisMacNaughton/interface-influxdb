from charms.reactive import hook
from charms.reactive import RelationBase
from charms.reactive import scopes


class InfluxdbRequires(RelationBase):
    scope = scopes.SERVICE
    auto_accessors = ['host', 'port', 'user', 'password']

    @hook('{requires:influxdb-http}-relation-{joined,changed}')
    def changed(self):
        data = {
            'host': self.host(),
            'port': self.port(),
            'user': self.user(),
            'password': self.password(),
        }
        if all(data.values()):
            self.set_state('{relation_name}.available')

    @hook('{requires:influxdb-http}-relation-{broken,departed}')
    def broken(self):
        self.remove_state('{relation_name}.available')
