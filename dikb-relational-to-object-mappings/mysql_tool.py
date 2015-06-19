from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

"""sqlalchemy engine params"""
#engine = create_engine('mysql://root:5bboys@localhost/dikbEvidence')
engine = create_engine('mysql://root:5bboys@localhost/dikbEvidenceTest')
Base = declarative_base(engine)

"""dikbEvidence Table class representation for sqlalchemy"""
class ChemicalTable(Base):
    __tablename__ = 'Chemical'
    __table_args__ = {'autoload':True}

class DrugTable(Base):
    __tablename__ = 'Drugs'
    __table_args__ = {'autoload':True}

class MetaboliteTable(Base):
    __tablename__ = 'Metabolite'
    __table_args__ = {'autoload':True}

class AssertionTable(Base):
    __tablename__ = 'Assertions'
    __table_args__ = {'autoload':True}

    def create(self, obj, slot, value, assert_class):
        self.object = obj
        self.slot = slot
        self.value = value
        self._name = "_".join([obj, slot, value])
        self.assert_class = assert_class
        self.assert_by_default = "0"
        self.ready_for_classification = "0"
        self.evidence_rating = "none_assigned"

class EvidenceTable(Base):
    __tablename__ = 'Evidence'
    __table_args__ = {'autoload':True}

    def create(self, pointer, quote, evType, reviewer, timestamp, **kwargs):
        self.doc_pointer = pointer
        self.quote = quote
        self.evidence_type = evType
        self.reviewer = reviewer
        self.timestamp = timestamp
        for key in kwargs:
            setattr(self,key,kwargs[key])
        self.assumptions = []

    def add_assumptions(self, assumptions):
        self.assumptions = assumptions

class EvidenceMapTable(Base):
    __tablename__ = 'Evidence_map'
    __table_args__ = {'autoload':True}


class AssumptionMapTable(Base):
    __tablename__ = 'Assumption_map'
    __table_args__ = {'autoload':True}

"""Make enzymes easier to access, though still just
    loaded from a text file"""
def get_enzymes():
    try:
        fr = open("data/enzymes")
        text = fr.read()
        return text.split("\n")
    except IOError, err:
        warning(" ".join(["Could not open file containing enzyme names:",os.getcwd(),"data/enzymes", 
                          "Please make sure this file exists. Returning None"]), 1)
        return None


"""A test request class for debugging rpy script render calls"""
class TestRequest:
    def __init__(self, args):
        self.args = args

"""Get a sqlalchemy session"""
def load_session():
    metadata = Base.metadata
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

"""Save new data to db"""
def flush_session(session):
    pass
