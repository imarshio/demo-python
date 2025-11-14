import threading


class AClass:

    pg_db = None
    _init_lock = threading.Lock()

    @classmethod
    def default_db(cls):
        if cls.pg_db is None:
            with cls._init_lock:
                if cls.pg_db is None:
                    cls.pg_db = "a db"
        return cls.pg_db