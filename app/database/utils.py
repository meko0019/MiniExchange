from sqlalchemy.exc import ResourceClosedError

from app.database import db, MetadataModel

def delete_all_rows(app):
    """Delete all instances without dropping the tables."""
    with app.app_context():
        try:
            for tbl in reversed(MetadataModel.metadata.sorted_tables):
                db.session.execute(tbl.delete())
            db.session.commit()
        except ResourceClosedError:
            pass