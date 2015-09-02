from hired import db
from hired.errors import ValidationError


class Rules(db.Model):
    """
    Database mode for rules
    """
    id = db.Column(db.Integer, primary_key=True)
    rule = db.Column(db.String(200))

    def __repr__(self):
        return '<id:  %r>' % (self.id)

    def get_url(self):
        # TODO
        pass

    def to_json(self):
        # TODO
        pass

    def from_json(self, req_data):
        # TODO
        pass
